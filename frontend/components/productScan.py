import streamlit as st
import requests
from utils.animations import load_lottie_file, display_exercise_animations

def scan_tab(user_id, BASE_URL):
    st.header("Analyze Product & Burn Calories")
    uploaded_file = st.file_uploader("Upload an image for product analysis", type=["jpg", "png", "jpeg"])
    
    if st.button("Analyze Product"):
        if uploaded_file and user_id:
            files = {'image_file': uploaded_file.getvalue()}
            response = requests.post(f"{BASE_URL}/analyze_product", files=files, data={'user_id': user_id})
            if response.status_code == 200:
                result = response.json()
                st.subheader("Analysis Result")
                st.markdown(result['result']['health_recommendation'])
                st.image(uploaded_file)
                display_exercise_animations(result['result']['excercises_result'])
            else:
                st.error(f"Error {response.status_code}: {response.text}")
