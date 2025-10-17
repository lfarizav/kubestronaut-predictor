import streamlit as st
import requests
import json
import time
import os

# Set the page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Certified Kubestronaut Result Predictor",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add title and description
st.title("Certified Kubestronaut Result Predictor")
st.markdown(
    """
    <p style="font-size: 18px; color: gray;">
        A demonstration project for real-time Kubestronaut Results Predictor using Machine Learning, FastAPI, and Streamlit.
    </p>
    """,
    unsafe_allow_html=True,
)

# Create a two-column layout
col1, col2 = st.columns(2, gap="large")

# Input form
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Theory hours slider
    st.markdown(f"<p><strong>Theory hours:</strong> <span id='theory-hours-value'></span></p>", unsafe_allow_html=True)
    theory_hours = st.slider("", 1, 2000, 1152, 1, label_visibility="collapsed", key="theory_hours")
    st.markdown(f"<script>document.getElementById('theory-hours-value').innerText = '{theory_hours} theory_hours';</script>", unsafe_allow_html=True)

    # Laboratory hours slider
    st.markdown(f"<p><strong>Laboratory hours:</strong> <span id='lab-hours-value'></span></p>", unsafe_allow_html=True)
    lab_hours = st.slider("", 1, 2000, 1152, 1, label_visibility="collapsed", key="lab_hours")
    st.markdown(f"<script>document.getElementById('lab-hours-value').innerText = '{lab_hours} lab_hours';</script>", unsafe_allow_html=True)

    # number_full_exam_done and cncf_try_numbers: in two columns
    number_full_exam_done, cncf_try_numbers = st.columns(2)
    with number_full_exam_done:
        st.markdown("<p><strong>Number mockup full exams done</strong></p>", unsafe_allow_html=True)
        number_full_exam_done = st.selectbox("", options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], index=8, label_visibility="collapsed")
    
    with cncf_try_numbers:
        st.markdown("<p><strong>How Many real CNCF Exams Has You Failed</strong></p>", unsafe_allow_html=True)
        cncf_try_numbers = st.selectbox("", options=[1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], index=5, label_visibility="collapsed")
    
    # Location dropdown
    st.markdown("<p><strong>Location region of the Kubestronaut candidate</strong></p>", unsafe_allow_html=True)
    location = st.selectbox("", options=["Urban", "Suburban", "Rural", "Waterfront", "Mountain"], index=1, label_visibility="collapsed")
    
    # Year Built slider
    st.markdown(f"<p><strong>Kubestronaut's birth year:</strong> <span id='born_year-value'></span></p>", unsafe_allow_html=True)
    born_year = st.slider("", 1950, 2025, 1990, 1, label_visibility="collapsed", key="born_year")
    st.markdown(f"<script>document.getElementById('born_year-value').innerText = '{born_year} born_year';</script>", unsafe_allow_html=True)
    
    # Selfassesment dropdown
    st.markdown("<p><strong>Selfassessment of the Kubestronaut candidate</strong></p>", unsafe_allow_html=True)
    selfassessment = st.selectbox("", options=["Good", "Excelent", "Fair", "Poor"], index=1, label_visibility="collapsed")
    
    # Predict button
    predict_button = st.button("Predict Kubestronaut Results", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Results section
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h2>Certified Kubestronaut Results</h2>", unsafe_allow_html=True)
    
    # If button is clicked, show prediction
    if predict_button:
        # Show loading spinner
        with st.spinner("Calculating prediction..."):
            # Prepare data for API call
            api_data = {
                "theory_hours": theory_hours,
                "lab_hours": lab_hours,
                "number_full_exam_done": number_full_exam_done,
                "cncf_try_numbers": cncf_try_numbers,
                "location": location.lower(),
                "born_year": born_year,
                "selfassessment": selfassessment.lower()
            }
            
            try:
                # Get API endpoint from environment variable or use default
                api_endpoint = os.getenv("API_URL", "http://localhost:8000")
                predict_url = f"{api_endpoint.rstrip('/')}/predict"
                
                st.write(f"Connecting to API at: {predict_url}")
                
                # Make API call to FastAPI backend
                response = requests.post(predict_url, json=api_data)
                response.raise_for_status()  # Raise exception for bad status codes
                prediction = response.json()
                
                # Store prediction in session state
                st.session_state.prediction = prediction
                st.session_state.prediction_time = time.time()
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to API: {e}")
                st.warning("Using mock data for demonstration purposes. Please check your API connection.")
                # For demo purposes, use mock data if API fails
                st.session_state.prediction = {
                    "predicted_final_result": 0.9,
                    "confidence_interval": [0, 1],
                    "features_importance": {
                        "theory_hours": 1152,
                        "lab_hours": 1152,
                        "selfassessment": "Poor",
                        "number_full_exam_done": 5
                    },
                    "prediction_time": "0.12 seconds"
                }
                st.session_state.prediction_time = time.time()
    
    # Display prediction if available
    if "prediction" in st.session_state:
        pred = st.session_state.prediction
        
        # Format the predicted final_result
        formatted_final_result = "${:,.0f}".format(pred["predicted_final_result"])
        st.markdown(f'<div class="prediction-value">{formatted_final_result}</div>', unsafe_allow_html=True)
        
        # Display confidence score and model used
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown('<div class="info-card">', unsafe_allow_html=True)
            st.markdown('<p class="info-label">Confidence Score</p>', unsafe_allow_html=True)
            st.markdown('<p class="info-value">92%</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col_b:
            st.markdown('<div class="info-card">', unsafe_allow_html=True)
            st.markdown('<p class="info-label">Model Used</p>', unsafe_allow_html=True)
            st.markdown('<p class="info-value">XGBoost</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Display final_result range and prediction time
        col_c, col_d = st.columns(2)
        with col_c:
            st.markdown('<div class="info-card">', unsafe_allow_html=True)
            st.markdown('<p class="info-label">Certified Kubestronaut</p>', unsafe_allow_html=True)
            lower = "${:,.1f}".format(pred["confidence_interval"][0])
            upper = "${:,.1f}".format(pred["confidence_interval"][1])
            st.markdown(f'<p class="info-value">{lower} - {upper}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col_d:
            st.markdown('<div class="info-card">', unsafe_allow_html=True)
            st.markdown('<p class="info-label">Prediction Time</p>', unsafe_allow_html=True)
            st.markdown('<p class="info-value">0.12 seconds</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Top factors
        st.markdown('<div class="top-factors">', unsafe_allow_html=True)
        st.markdown("<p><strong>Top Factors Affecting the Final Result:</strong></p>", unsafe_allow_html=True)
        st.markdown("""
        <ul>
            <li>Layer 8 error</li>
            <li>Model drift</li>
        </ul>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        # Display placeholder message
        st.markdown("""
        <div style="display: flex; height: 300px; align-items: center; justify-content: center; color: #6b7280; text-align: center;">
            Fill out the form and click "Predict Kubestronaut Results" to see the estimated Kubestronaut results.
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Add footer
st.markdown("<hr>", unsafe_allow_html=True)  # Add a horizontal line for separation
st.markdown(
    """
    <div style="text-align: center; color: gray; margin-top: 20px;">
        <p><strong>Built with love for MLOps testing</strong></p>
        <p>by <a href="https://delaparlaalcluster.org" target="_blank">De la parla al cluster</a></p>
    </div>
    """,
    unsafe_allow_html=True,
)

