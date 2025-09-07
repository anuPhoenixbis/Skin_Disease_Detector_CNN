"""
Custom CSS styling for the application
"""

import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        padding-top: 2rem;
    }
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Styling */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
    }
    
    .main-header h1 {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .main-header p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
        font-weight: 400;
    }
    
    /* Card Styling */
    .medical-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        color: black;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .medical-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
    }
    
    /* Upload Area Styling */
    .upload-area {
        border: 3px dashed #667eea;
        border-radius: 15px;
        padding: 3rem 2rem;
        text-align: center;
        background: linear-gradient(45deg, rgba(102, 126, 234, 0.05), rgba(118, 75, 162, 0.05));
        transition: all 0.3s ease;
        margin: 1rem 0;
    }
    
    .upload-area:hover {
        border-color: #764ba2;
        background: linear-gradient(45deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        transform: scale(1.02);
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Prediction Results */
    .prediction-result {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(240, 147, 251, 0.3);
    }
    
    .prediction-result h3 {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    /* Severity Badges */
    .severity-mild {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: green;
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        font-weight: 600;
        display: inline-block;
        margin: 0.5rem;
        box-shadow: 0 4px 15px rgba(79, 172, 254, 0.3);
    }
    
    .severity-moderate {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: yellow;
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        font-weight: 600;
        display: inline-block;
        margin: 0.5rem;
        box-shadow: 0 4px 15px rgba(250, 112, 154, 0.3);
    }
    
    .severity-severe {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
        color: red;
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        font-weight: 600;
        display: inline-block;
        margin: 0.5rem;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    /* Preventive Measures */
    .preventive-measures {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 5px solid #667eea;
    }
    
    .preventive-measures h3 {
        color: #667eea;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .preventive-measures ul {
        list-style: none;
        padding: 0;
    }
    
    .preventive-measures li {
        background: white;
        margin: 0.5rem 0;
        padding: 1rem;
        color: black;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        border-left: 4px solid #667eea;
        transition: transform 0.2s ease;
    }
    
    .preventive-measures li:hover {
        transform: translateX(5px);
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .css-1d391kg .css-1v0mbdj {
        color: white;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Success/Error Messages */
    .stSuccess {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        border-radius: 10px;
    }
    
    .stError {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
        color: white;
        border-radius: 10px;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: white;
        border-radius: 10px;
    }
    
    /* Loading Spinner */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    
    /* Footer */
    .footer {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-top: 3rem;
        border: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    /* Image Preview */
    .image-preview {
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        overflow: hidden;
        margin: 1rem 0;
    }
    
    /* Confidence Gauge */
    .confidence-container {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    
    /* Stats Cards */
    .stats-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.6));
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .stats-card h4 {
        color: #667eea;
        font-weight: 700;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }
    
    .stats-card p {
        color: #666;
        font-size: 0.9rem;
    }
    
    /* Hide Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    </style>
    """, unsafe_allow_html=True)
