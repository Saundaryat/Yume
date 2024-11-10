import streamlit as st
import requests

def calorie_intake_tab(user_id, BASE_URL):
    st.header("Calorie Intake Calculator")
    uploaded_file = st.file_uploader("Upload an image of your meal", type=["jpg", "png", "jpeg"])
    meal_type = st.selectbox("Select Meal Type", ["Breakfast", "Lunch", "Dinner", "Snacks"])

    if st.button("Add Meal") and uploaded_file:
        files = {'image_file': uploaded_file.getvalue()}
        id_token = st.session_state.get("id_token")
        if not id_token:
            st.error("User is not authenticated.")
            return
        headers = {"Authorization": f"Bearer {id_token}"}
        response = requests.post(f"{BASE_URL}/calculate_calories", headers=headers, files=files, data={'user_id': user_id, 'meal_type': meal_type})
        if response.status_code == 200:
            result = response.json()
            st.subheader("Calorie Calculation Result")
            st.markdown(result['result']['health_recommendation'])
            st.image(uploaded_file)
        else:
            st.error(f"Error {response.status_code}: {response.text}")
