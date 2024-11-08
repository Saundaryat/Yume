import streamlit as st

def home_intro():
    st.title("Welcome to YuMe")
    st.subheader("Your Personalized Health and Wellness Companion")
    
    st.markdown(
        """
        **YuMe** is designed to help you monitor your nutrition, track your calorie intake, and analyze products to guide you on your health journey. Here’s what you can do with YuMe:
        
        - **Analyze Products:** Upload images of products to receive real-time ingredient analysis and tailored feedback.
        - **Track Your Progress:** Monitor your health goals, track calories, and receive insights based on your food consumption.
        - **Personalized Recommendations:** Based on your health records and preferences, get customized recommendations for better health.

        With YuMe, take control of your health journey through simple, intuitive tools designed to empower you. Ready to explore?
        """
    )

    # Button to proceed to main functionality
    if st.button("Start Exploring YuMe"):
        st.session_state["show_homepage"] = False  # Set to show main interface
