import streamlit as st
import requests

def dashboard_tab(user_id, BASE_URL):
    st.header("User Profile")
    uploaded_doc = st.file_uploader("Upload the health record document", type=["txt"])
    
    if st.button("Upload Health Record") and uploaded_doc:
        files = {'file': ('health_record.txt', uploaded_doc.getvalue(), 'text/plain')}
        response = requests.post(f"{BASE_URL}/health_record/", files=files, data={'user_id': user_id})
        if response.status_code == 200:
            st.success(f"Document '{uploaded_doc.name}' uploaded successfully!")
            st.markdown(uploaded_doc.getvalue().decode('utf-8'))
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    
    user_preferences = st.text_input("Enter Your Preferences (e.g., vegan, keto, etc.)")
    if st.button("Add Preferences") and user_preferences:
        data = {'user_id': user_id, 'preferences': user_preferences}
        response = requests.post(f"{BASE_URL}/preferences/", json=data)
        if response.status_code == 200:
            st.success(f"Preferences '{user_preferences}' added successfully!")
        else:
            st.error(f"Error {response.status_code}: {response.text}")
