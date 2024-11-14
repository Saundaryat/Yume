import streamlit as st
import pyrebase
import json
from components.intro2 import home_intro
from components.home import user_home_tab
from components.productScan import scan_tab
from components.profile import dashboard_tab
from components.calorie import calorie_intake_tab
from utils.styles import apply_custom_styles

st.set_page_config(layout="wide")

# Firebase configuration
firebase_config = {
    "apiKey": "AIzaSyCFtq_XY0b2RNCgXjp5Zdn_AdQlQuVk1iU",
    "authDomain": "yume-f1311.firebaseapp.com",
    "databaseURL": "https://yume-f1311-default-rtdb.firebaseio.com",
    "storageBucket": "yume-f1311.firebasestorage.app",
    "messagingSenderId": "314253158282",
    "appId": "1:314253158282:web:aa317ab11045cdb79e0a73"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Load the application configuration
with open('config/config.json', 'r') as config_file:
    config = json.load(config_file)
BASE_URL = config['BASE_URL']

def login_ui():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if not st.session_state["authenticated"]:
        st.title("Welcome to YuMe!")
        st.write("Let your journey begin")
        email = st.text_input("Enter your email")
        password = st.text_input("Enter your password", type="password")

        login_clicked = st.button("Login")
        signup_clicked = st.button("Signup")

        if login_clicked:
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state["authenticated"] = True
                st.session_state["user"] = user
                st.session_state["id_token"] = user["idToken"]
                st.session_state["user_id"] = email  
                st.session_state["show_success"] = True
            except Exception as e:
                st.session_state["show_success"] = False
                st.error("Invalid email or password. If you don't have an account, please sign up.")

        if signup_clicked:
            try:
                user = auth.create_user_with_email_and_password(email, password)
                st.success("Account created successfully! Please log in.")
            except Exception as e:
                if "EMAIL_EXISTS" in str(e):
                    st.error("This email is already registered. Please log in instead.")
                elif "INVALID_EMAIL" in str(e):
                    st.error("Please enter a valid email address.")
                elif "WEAK_PASSWORD" in str(e):
                    st.error("Password is too weak. Please enter a stronger password.")
                else:
                    st.error("An error occurred during signup. Please try again.")

    if st.session_state.get("show_success"):
        st.success("Login successful!")
        st.session_state["show_success"] = False  # Reset the success message

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
    if not st.session_state.get("authenticated"):
        login_ui()
    else:
        main_app()

if __name__ == "__main__":
    main()