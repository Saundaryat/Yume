import streamlit as st
import requests

def dashboard_tab(user_id, BASE_URL):
    st.header("User Profile")
    uploaded_doc = st.file_uploader("Upload the health record document", type=["txt"])
    
    if st.button("Upload Health Record") and uploaded_doc:
        files = {'file': ('health_record.txt', uploaded_doc.getvalue(), 'text/plain')}
        # Retrieve the Firebase ID token from session state
        id_token = st.session_state.get("id_token")
        if not id_token:
            st.error("User is not authenticated.")
            return
        # Set up headers with the token
        headers = {"Authorization": f"Bearer {id_token}"}
        response = requests.post(f"{BASE_URL}/health_record/",  headers=headers, files=files, data={'user_id': user_id})
        if response.status_code == 200:
            st.success(f"Document '{uploaded_doc.name}' uploaded successfully!")
            st.markdown(uploaded_doc.getvalue().decode('utf-8'))
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    
    user_preferences = st.text_input("Enter Your Preferences (e.g., vegan, keto, etc.)")
    if st.button("Add Preferences") and user_preferences:
        data = {'user_id': user_id, 'preferences': user_preferences}
        id_token = st.session_state.get("id_token")
        if not id_token:
            st.error("User is not authenticated.")
            return
        # Set up headers with the token
        headers = {"Authorization": f"Bearer {id_token}"}
        response = requests.post(f"{BASE_URL}/preferences/",  headers=headers, json=data)
        if response.status_code == 200:
            st.success(f"Preferences '{user_preferences}' added successfully!")
        else:
            st.error(f"Error {response.status_code}: {response.text}")
