"""
Model loading, prediction, and related utility functions
"""

import json
import pickle
import numpy as np
from pathlib import Path
from typing import Dict, Any, List
import streamlit as st

from config.settings import MODEL_DIR, MODEL_H5, MODEL_PKL, CLASSES_JSON, THRESHOLD_MILD, THRESHOLD_SEVERE, HIGH_RISK_DISEASES, WEIGHTS_URL

def ensure_model_dir():
    """Ensure model directory exists"""
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

def download_file(url: str, dest_path: Path):
    """Download file from URL"""
    import requests
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(dest_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return dest_path

@st.cache_resource
def load_class_names() -> List[str]:
    """Load class names from JSON file"""
    if CLASSES_JSON.exists():
        with open(CLASSES_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                if "classes" in data and isinstance(data["classes"], list):
                    return data["classes"]
                try:
                    return [data[str(i)] for i in range(len(data))]
                except Exception:
                    return list(data.values())
            elif isinstance(data, list):
                return data
    return []

@st.cache_resource
def load_model():
    """Load the trained model"""
    ensure_model_dir()
    try:
        import tensorflow as tf
    except ImportError as e:
        try:
            import tensorflow_cpu as tf
        except ImportError:
            st.error(f"Could not import TensorFlow. Details: {e}")
            st.stop()

    # Try loading existing model
    if MODEL_H5.exists():
        try:
            model = tf.keras.models.load_model(str(MODEL_H5), compile=False)
            return model
        except Exception as e:
            st.warning(f"Failed to load {MODEL_H5}: {e}")

    # Try downloading model
    if WEIGHTS_URL:
        try:
            download_file(WEIGHTS_URL, MODEL_H5)
            model = tf.keras.models.load_model(str(MODEL_H5), compile=False)
            return model
        except Exception as e:
            st.warning(f"Failed to download/load model from WEIGHTS_URL: {e}")

    # Try pickle format
    if MODEL_PKL.exists():
        try:
            with open(MODEL_PKL, "rb") as f:
                model = pickle.load(f)
            return model
        except Exception as e:
            st.warning(f"Failed to unpickle {MODEL_PKL}: {e}")

    raise FileNotFoundError("No model artifact found.")

def predict_image(model, image_bytes: bytes, class_names: List[str]) -> Dict[str, Any]:
    """Make prediction on image"""
    from utils.image_utils import preprocess_image_bytes
    
    x = preprocess_image_bytes(image_bytes)
    x_batch = np.expand_dims(x, axis=0)
    
    preds = model.predict(x_batch)
    if isinstance(preds, (list, tuple)):
        preds = preds[0]
    preds = np.asarray(preds).reshape(-1)
    
    s = float(np.sum(preds))
    if s <= 0:
        probs = np.ones_like(preds) / len(preds)
    else:
        probs = preds / s

    top_idx = int(np.argmax(probs))
    top_conf = float(probs[top_idx])
    if class_names and len(class_names) > top_idx:
        top_label = class_names[top_idx]
    else:
        top_label = str(top_idx)

    probs_map = {}
    for i, p in enumerate(probs):
        name = class_names[i] if (class_names and i < len(class_names)) else str(i)
        probs_map[name] = float(p)

    return {
        "class_id": top_idx,
        "disease": top_label,
        "confidence": top_conf,
        "probabilities": probs_map,
    }

def compute_severity(confidence: float, disease_name: str, high_risk_diseases: List[str] = None) -> str:
    """Compute severity level based on confidence and disease type"""
    if high_risk_diseases is None:
        high_risk_diseases = HIGH_RISK_DISEASES
    
    if disease_name in high_risk_diseases:
        return "severe"
    if confidence < THRESHOLD_MILD:
        return "mild"
    if confidence < THRESHOLD_SEVERE:
        return "moderate"
    return "severe"