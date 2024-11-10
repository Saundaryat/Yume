import streamlit as st
import requests
import random

def user_home_tab(user_id, BASE_URL):
    st.header("Welcome to Your Home Page")
    
    # Motivational quotes
    motivational_quotes = [
        "You can do it!", "Keep pushing forward!", 
        "Every step counts.", "Believe in yourself!",
    ]
    st.write(random.choice(motivational_quotes))
    
    # Calendar input to select a date
    selected_date = st.date_input("Select a Date to View Insights")
    if st.button("Get Insights"):
        if not user_id:
            st.error("Please enter your User ID.")
        else:
            data = {'timestamp': selected_date.isoformat()}
            id_token = st.session_state.get("id_token")
            if not id_token:
                st.error("User is not authenticated.")
                return
            headers = {"Authorization": f"Bearer {id_token}"}

            response = requests.post(f"{BASE_URL}/analyze_meal_habits/{user_id}",  headers=headers, json=data)
            if response.status_code == 200:
                result = response.json()
                st.success("Meal habits analyzed successfully!")
                st.markdown(result['analysis'])
            else:
                st.error(f"Error {response.status_code}: {response.text}")
