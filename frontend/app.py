import streamlit as st
import pyrebase
import json
from components.introduction import home_intro
from components.home import user_home_tab
from components.productScan import scan_tab
from components.profile import dashboard_tab
from components.calorie import calorie_intake_tab
from utils.styles import apply_custom_styles

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Load the application configuration
with open('config/config.json', 'r') as config_file:
    config = json.load(config_file)
BASE_URL = config['BASE_URL']

def login_ui():
    st.title("Firebase Authentication in Streamlit")
    choice = st.selectbox("Login or Signup", ["Login", "Signup"])
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type="password")

    if choice == "Signup":
        if st.button("Create Account"):
            try:
                user = auth.create_user_with_email_and_password(email, password)
                st.success("Account created successfully! Please log in.")
            except Exception as e:
                st.error(e)
    elif choice == "Login":
        if st.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state["authenticated"] = True
                st.session_state["user"] = user
                # Store the Firebase ID token
                st.session_state["id_token"] = user["idToken"]
                st.session_state["user_id"] = email  
                st.success("Login successful!")
            except Exception as e:
                st.error(e)


def main_app():
    # Apply custom styles
    apply_custom_styles()

    # Initialize session state for homepage if not already set
    if "show_homepage" not in st.session_state:
        st.session_state["show_homepage"] = True

    # Show the introductory home page or main interface based on session state
    if st.session_state["show_homepage"]:
        home_intro()  # Display home_intro component
    else:
        # Sidebar setup and main functionality display
        st.sidebar.title("YuMe")
        st.sidebar.write("Welcome to the User Dashboard")
        
        # Use email as the user_id
        user_id = st.sidebar.text_input("YuMe User ID", value=st.session_state.get("user_id", ""))
        
        # Navigation options
        menu = ["User Home", "Analyze Product", "User Profile", "Calorie Intake"]
        choice = st.sidebar.selectbox("Navigation", menu)

        # Display tabs based on choice
        if choice == "User Home":
            user_home_tab(user_id, BASE_URL)
        elif choice == "Analyze Product":
            scan_tab(user_id, BASE_URL)
        elif choice == "User Profile":
            dashboard_tab(user_id, BASE_URL)
        elif choice == "Calorie Intake":
            calorie_intake_tab(user_id, BASE_URL)

def main():
    # Check if the user is authenticated
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        login_ui()
    else:
        main_app()

if __name__ == "__main__":
    main()
