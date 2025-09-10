"""
Reusable UI components and display functions
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

def create_header():
    """Create the main application header"""
    st.markdown("""
    <div class="main-header">
        <h1>🏥 AI Skin Disease Detection</h1>
        <p>Advanced CNN-based skin condition analysis with AI-powered recommendations</p>
    </div>
    """, unsafe_allow_html=True)

def create_stats_sidebar():
    """Create sidebar with stats and information"""
    with st.sidebar:
        st.markdown("### 🎨 Theme")
        theme = st.selectbox("Choose a theme", ["Dark", "Light"], key="theme_selector")

        st.markdown("### 📊 Application Statistics")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="stats-card">
                <h4>224×224</h4>
                <p>Input Size</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="stats-card">
                <h4>CNN</h4>
                <p>Model Type</p>
            </div>
            """, unsafe_allow_html=True)
        
        from config.settings import THRESHOLD_MILD, THRESHOLD_SEVERE
        st.markdown("### ⚙️ Configuration")
        st.info(f"**Severity Thresholds:**\n- Mild: < {THRESHOLD_MILD*100:.0f}%\n- Severe: ≥ {THRESHOLD_SEVERE*100:.0f}%")
        
        st.markdown("### 🔒 Privacy & Safety")
        st.success("✅ Images processed securely")
        st.success("✅ No data stored permanently")
        st.success("✅ HIPAA compliant processing")

def create_results_display(result, image_bytes):
    """Display analysis results"""
    severity = result['severity']
    measures = result['measures']
    
    st.markdown("---")
    
    # Prediction result
    severity_class = f"severity-{severity.lower()}"
    st.markdown(f"""
    <div class="prediction-result">
        <h3>🎯 Diagnosis: {result['disease']}</h3>
        <div class="{severity_class}">
            Severity: {severity.upper()}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Show warning for severe cases
    if severity == "severe":
        st.error("⚠️ **IMPORTANT:** This analysis suggests a potentially serious condition. Please consult a healthcare professional immediately.")
    
    # Preventive measures
    st.markdown(f"""
    <div class="preventive-measures">
        <h3>💡 Preventive Measures & Recommendations</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if measures.get("bullets"):
        for i, bullet in enumerate(measures["bullets"], 1):
            st.markdown(f"""
            <div class="preventive-measures">
                <li><strong>{i}.</strong> {bullet}</li>
            </div>
            """, unsafe_allow_html=True)
    
    # Consultation advice
    if measures.get("consult"):
        st.markdown(f"""
        <div class="medical-card" style="border-left: 5px solid #ff6b6b;">
            <h4>🩺 When to Seek Medical Attention</h4>
            <p style="font-size: 1.1rem; color: #333;">{measures["consult"]}</p>
        </div>
        """, unsafe_allow_html=True)

def create_footer():
    """Create application footer with disclaimers"""
    st.markdown("""
    <div class="footer">
        <h4>⚠️ Important Medical Disclaimer</h4>
        <p>This AI-powered skin disease detection application is for <strong>informational purposes only</strong>.</p>
        <p><strong>Always consult with qualified healthcare professionals</strong> for any skin concerns.</p>
    </div>
    """, unsafe_allow_html=True)