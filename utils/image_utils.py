"""
Image processing and validation utilities
"""

import io
import numpy as np
from PIL import Image
from typing import Tuple

from config.settings import MAX_FILE_SIZE, SUPPORTED_FORMATS, IMAGE_SIZE

def validate_uploaded_file(uploaded_file) -> Tuple[bool, str]:
    """Validate uploaded file size and format"""
    if uploaded_file is None:
        return False, "No file uploaded"
    
    if uploaded_file.size > MAX_FILE_SIZE:
        return False, f"File size ({uploaded_file.size/1024/1024:.1f}MB) exceeds limit ({MAX_FILE_SIZE/1024/1024}MB)"
    
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension not in SUPPORTED_FORMATS:
        return False, f"Unsupported format. Please use: {', '.join(SUPPORTED_FORMATS)}"
    
    return True, "Valid file"

def preprocess_image_bytes(image_bytes: bytes) -> np.ndarray:
    """Preprocess image bytes for model prediction"""
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize(IMAGE_SIZE)
    arr = np.asarray(img).astype("float32") / 255.0
    return arr

def image_file_to_base64(image_bytes: bytes) -> str:
    """Convert image bytes to base64 string"""
    import base64
    return base64.b64encode(image_bytes).decode("utf-8")