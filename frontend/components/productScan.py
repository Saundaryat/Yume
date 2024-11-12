import streamlit as st
import requests
from utils.animations import load_lottie_file, display_exercise_animations

def scan_tab(user_id, BASE_URL):
    st.header("Analyze Product & Burn Calories")
    uploaded_file = st.file_uploader("Upload an image for product analysis", type=["jpg", "png", "jpeg"])
    
    if st.button("Analyze Product"):
        if uploaded_file and user_id:
            # Retrieve the Firebase ID token from session state
            id_token = st.session_state.get("id_token")
            if not id_token:
                st.error("User is not authenticated.")
                return

            # Set up headers with the token
            headers = {"Authorization": f"Bearer {id_token}"}

            # Prepare files and data for the request
            files = {'image_file': uploaded_file.getvalue()}
            data = {'user_id': user_id}

            # Send the request to the backend with the headers
            response = requests.post(f"{BASE_URL}/analyze_product", headers=headers, files=files, data=data)
            
            if response.status_code == 200:
                result = response.json()
                st.subheader("Analysis Result")
                st.markdown(result['result']['health_recommendation'])
                st.image(uploaded_file)
                display_exercise_animations(result['result']['excercises_result'])
            else:
                st.error(f"Error {response.status_code}: {response.text}")
