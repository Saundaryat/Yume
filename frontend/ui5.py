import streamlit as st
import requests

def scan_tab(user_id):
    uploaded_file = st.file_uploader("Upload an image for product analysis", type=["jpg", "png", "jpeg"])

    if st.button("Analyze Product"):
        if uploaded_file is None:
            st.error("Please upload an image.")
        elif not user_id:
            st.error("Please enter your User ID.")
        else:
            try:
                files = {
                    'image_file': uploaded_file.getvalue(),
                }
                data = {
                    'user_id': user_id
                }
                api_url = "http://localhost:5001/analyze_product"
                response = requests.post(api_url, files=files, data=data)

                if response.status_code == 200:
                    result = response.json()
                    st.write("### Analysis Result")
                    st.markdown(result['result']['health_recommendation'])
                    st.image(uploaded_file)
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

def dashboard_tab(user_id):
    st.write("Welcome to the User Dashboard")
    
    ### Upload Health Record
    uploaded_doc = st.file_uploader("Upload the health record document", type=["txt"])
    if st.button("Upload Health Record"):
        if uploaded_doc is None:
            st.error("Please upload the doc.")
        elif not user_id:
            st.error("Please enter your User ID.")
        else:
            try:
                files = {
                    'file': ('health_record.txt', uploaded_doc.getvalue(), 'text/plain'),
                }
                data = {
                    'user_id': user_id
                }
                api_url = "http://localhost:5001/health_record/"
                response = requests.post(api_url, files=files, data=data)

                if response.status_code == 200:
                    st.success(f"Document '{uploaded_doc.name}' uploaded successfully!")
                    st.text("Uploaded file content:")
                    st.markdown(uploaded_doc.getvalue().decode('utf-8'))
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

    ### Add User Preferences    
    user_preferences = st.text_input("Enter Your Preferences: vegan? keto? looking to lose weight? etc.\n\n"
                                     "Also what is your activity level? sedentary, active, very active?")
    if st.button("Add Your Preferences"):
        if user_preferences is None:
            st.error("Please enter your preferences.")
        elif not user_id:
            st.error("Please enter your User ID.")
        else:
            try:
                data = {
                    'user_id': user_id,
                    'preferences': user_preferences
                }
                headers = {'Content-Type': 'application/json'}
                api_url = "http://localhost:5001/preferences/"
                response = requests.post(api_url, json=data, headers=headers)

                if response.status_code == 200:
                    st.success(f"Preferences '{user_preferences}' added successfully!")
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

def calorie_intake_tab(user_id):
    st.write("Calorie Intake Calculator")
    
    # Image uploader for meal data
    uploaded_file = st.file_uploader("Upload an image of your meal", type=["jpg", "png", "jpeg"])
    
    # Input for meal type
    meal_type = st.selectbox("Select Meal Type", ["Breakfast", "Lunch", "Dinner", "Snacks"])
    
    if st.button("Add Meal"):
        if uploaded_file is None:
            st.error("Please upload an image of your meal.")
        elif not user_id:
            st.error("Please enter your User ID.")
        else:
            try:
                files = {
                    'image_file': uploaded_file.getvalue(),
                }
                data = {
                    'user_id': user_id,
                    'meal_type': meal_type
                }
                
                # API URL for calorie calculation (update with actual API endpoint)
                api_url = "http://localhost:5001/calculate_calories"
                response = requests.post(api_url, files=files, data=data)
                
                if response.status_code == 200:
                    result = response.json()
                    st.write("### Calorie Calculation Result")
                    st.markdown(result['result']['health_recommendation'])
                    st.image(uploaded_file)
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

def main():
    st.title("YuMe")
    
    user_id = st.text_input("Enter your User ID")

    tab1, tab2, tab3 = st.tabs(["Scan", "Dashboard", "Calorie Intake"])
    
    with tab1:
        scan_tab(user_id)
    
    with tab2:
        dashboard_tab(user_id)

    with tab3:
        calorie_intake_tab(user_id)

if __name__ == "__main__":
    main()
