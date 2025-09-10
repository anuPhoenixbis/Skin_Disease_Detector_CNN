"""
Enhanced Streamlit app for Skin Disease Detection using CNN
Main application entry point with clean UI layout
"""

import streamlit as st
from pathlib import Path

# Import our custom modules
from config.settings import *
from styles.custom_css import inject_custom_css, inject_light_theme_css
from utils.model_utils import load_model, load_class_names, predict_image
from utils.image_utils import validate_uploaded_file, preprocess_image_bytes
from utils.ui_components import create_header, create_stats_sidebar, create_results_display
from services.gemini_service import get_preventive_measures_from_gemini

def main():
    # Page config
    st.set_page_config(
        page_title="AI Skin Disease Detection",
        page_icon="🏥",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize theme in session state
    if 'theme_selector' not in st.session_state:
        st.session_state.theme_selector = 'Dark'

    # Inject CSS based on theme
    if st.session_state.theme_selector == 'Light':
        inject_light_theme_css()
    else:
        inject_custom_css()

    # Create header
    create_header()
    
    # Initialize other session state
    if 'prediction_history' not in st.session_state:
        st.session_state.prediction_history = []
    
    # Create sidebar with stats (which includes the theme selector)
    create_stats_sidebar()
    
    # Load model and classes
    try:
        with st.spinner("🔄 Loading AI model..."):
            class_names = load_class_names()
            model = load_model()
        st.success("✅ AI Model loaded successfully!")
        
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        st.stop()
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    # File upload section
    with col1:
        st.markdown("""
        <div class="medical-card">
            <h3>📤 Upload Medical Image</h3>
            <p>Please upload a clear image of the skin condition for analysis</p>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=SUPPORTED_FORMATS,
            help=f"Supported formats: {', '.join(SUPPORTED_FORMATS)}. Max size: {MAX_FILE_SIZE//1024//1024}MB"
        )
        
        if uploaded_file is not None:
            is_valid, message = validate_uploaded_file(uploaded_file)
            
            if not is_valid:
                st.error(f"❌ {message}")
                st.stop()
            
            image_bytes = uploaded_file.read()
            st.markdown('<div class="image-preview">', unsafe_allow_html=True)
            st.image(image_bytes, caption="📸 Uploaded Image", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Analysis section
    with col2:
        if uploaded_file is not None:
            st.markdown("""
            <div class="medical-card">
                <h3>🔬 AI Analysis</h3>
                <p>Click the button below to start the medical image analysis</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🚀 Analyze Image", key="analyze_btn"):
                result = perform_analysis(model, image_bytes, class_names)
                if result:
                    create_results_display(result, image_bytes)

def perform_analysis(model, image_bytes, class_names):
    """Perform the complete analysis pipeline"""
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # Step 1: Preprocessing
        status_text.text("🔄 Preprocessing image...")
        progress_bar.progress(25)
        
        # Step 2: Model inference
        status_text.text("🧠 Running AI analysis...")
        progress_bar.progress(50)
        
        result = predict_image(model, image_bytes, class_names)
        
        # Step 3: Severity calculation
        status_text.text("📊 Computing severity...")
        progress_bar.progress(75)
        
        from utils.model_utils import compute_severity
        severity = compute_severity(result["confidence"], result["disease"])
        
        # Step 4: Getting recommendations
        status_text.text("💡 Generating recommendations...")
        progress_bar.progress(90)
        
        measures = get_preventive_measures_from_gemini(
            result["disease"], result["confidence"], image_bytes
        )
        
        progress_bar.progress(100)
        status_text.text("✅ Analysis complete!")
        
        # Store in session history
        st.session_state.prediction_history.append({
            'disease': result["disease"],
            'confidence': result["confidence"],
            'severity': severity
        })
        
        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()
        
        return {**result, 'severity': severity, 'measures': measures}
        
    except Exception as e:
        st.error(f"❌ Analysis failed: {e}")
        return None

if __name__ == "__main__":
    main()