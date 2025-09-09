"""
Configuration settings and constants for the skin disease detection app
"""

from pathlib import Path
import streamlit as st
import os

# Model and file paths
IMAGE_SIZE = (224, 224)
MODEL_DIR = Path("models")
MODEL_H5 = MODEL_DIR / "best_model.h5"
MODEL_PKL = MODEL_DIR / "best_model.pkl"
CLASSES_JSON = MODEL_DIR / "classes.json"

# File validation settings
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
SUPPORTED_FORMATS = ['jpg', 'jpeg', 'png']

# Severity thresholds
THRESHOLD_MILD = float(st.secrets.get("THRESHOLD_MILD", 0.45)) if "THRESHOLD_MILD" in st.secrets else 0.45
THRESHOLD_SEVERE = float(st.secrets.get("THRESHOLD_SEVERE", 0.80)) if "THRESHOLD_SEVERE" in st.secrets else 0.80

# High-risk diseases (can be loaded from secrets)
HIGH_RISK_DISEASES = st.secrets.get("HIGH_RISK_DISEASES", [])

# API Keys
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY"))
WEIGHTS_URL = st.secrets.get("WEIGHTS_URL") or os.environ.get("WEIGHTS_URL")