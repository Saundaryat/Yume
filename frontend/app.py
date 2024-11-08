import streamlit as st
import json
from components.introduction import home_intro
from components.home import user_home_tab
from components.productScan import scan_tab
from components.profile import dashboard_tab
from components.calorie import calorie_intake_tab
from utils.styles import apply_custom_styles
from utils.animations import load_lottie_file



with open('config/config.json', 'r') as config_file:
    config = json.load(config_file)

BASE_URL = config['BASE_URL']


def main():
    global BASE_URL
    
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
        user_id = st.sidebar.text_input("Enter your YuMe User ID")

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

if __name__ == "__main__":
    main()