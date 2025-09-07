"""
Gemini AI service for generating preventive measures and recommendations
"""

import os
from typing import Dict, Any
import streamlit as st

from config.settings import GEMINI_API_KEY
from utils.image_utils import image_file_to_base64

def get_preventive_measures_from_gemini(disease: str, confidence: float, image_bytes: bytes) -> Dict[str, Any]:
    """Get preventive measures from Gemini AI"""
    if GEMINI_API_KEY:
        try:
            import google.generativeai as genai
            genai.configure(api_key=GEMINI_API_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            Disease predicted: {disease} (confidence: {confidence*100:.1f}%)
            
            Provide exactly 3 preventive measures (one sentence each) and advice on when to see a doctor.
            Format:
            1. [preventive measure]
            2. [preventive measure] 
            3. [preventive measure]
            When to see a doctor: [advice]
            """
            
            response = model.generate_content(prompt)
            text = response.text
            
            lines = [line.strip() for line in text.split('\n') if line.strip()]
            bullets = []
            consult_line = ""
            
            for line in lines:
                if line.startswith(('1.', '2.', '3.')):
                    bullets.append(line[2:].strip())
                elif 'doctor' in line.lower():
                    consult_line = line.replace('When to see a doctor:', '').strip()
            
            if bullets:
                return {
                    "via": "gemini",
                    "bullets": bullets,
                    "consult": consult_line,
                    "advice_text": " ".join(bullets) + " " + consult_line
                }
                
        except Exception as e:
            st.warning(f"Gemini API call failed: {e}")
    
    return get_fallback_measures()

def get_fallback_measures() -> Dict[str, Any]:
    """Return fallback preventive measures"""
    return {
        "via": "fallback",
        "bullets": [
            "Keep the area clean and dry; wash gently with mild soap.",
            "Avoid scratching or picking at the area to reduce infection risk.",
            "Use gentle, fragrance-free moisturizers and avoid known irritants."
        ],
        "consult": "Consult a healthcare professional if symptoms worsen or persist.",
        "advice_text": "Keep the area clean and dry. Avoid scratching. Use gentle moisturizers."
    }