import streamlit as st
from components.integration_section import integration_section

def home_intro():
    st.markdown(
        """
        <style>
            /* Override Streamlit's default container padding */
            .st-emotion-cache-1jicfl2 {
                width: 100%;
                padding: 0 !important;
                min-width: auto;
                max-width: initial;
            }
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            
            /* Hero section styles */
            .hero-container {
                display: flex;
                justify-content: center;
                align-items: center;
                # height: calc(80vh - 80px);
                height: 60vh;
                background: linear-gradient(90deg, #FF9800 0%, #FFEB3B 100%);
                color: white;  /* Making text white for better contrast */
            }
            .content {
                text-align: center;
                max-width: 600px;
                padding: 20px;
            }
            .content h2 {
                font-size: 36px;
                margin-bottom: 10px;
                color: white;  /* Ensuring all text is white */
                text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);  /* Optional: adds subtle text shadow */
            }
            /* Button styles */
            .button-container {
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%;
            }
            .stButton {
                display: flex !important;
                justify-content: center !important;
                width: auto !important;
                white-space: nowrap !important;
                background: linear-gradient(90deg, #FF9800 0%, #FFEB3B 100%);
                padding-bottom: 20vh;
            }
            .stButton > button {
                padding: 12px 24px !important;
                background-color: #4CAF50 !important;
                border-radius: 4px !important;
                width: auto !important;
                background: white !important;  /* Changed to white */
                color: #FF9800 !important;  /* Using the gradient start color */
                border: none !important;
                font-weight: bold !important;
            }
            .stButton > button:hover {
                background-color: #45a049 !important;
                background: rgba(255, 255, 255, 0.9) !important;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
            }
            
            /* Steps section styles */
            .steps-container {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                padding: 80px 20px;
                background-color: #fff;
                box-sizing: border-box;
            }
            .step {
                display: flex;
                align-items: center;
                margin-bottom: 40px;
                max-width: 984px;
                width: 100%;
            }
            .step-number {
                font-size: 48px;
                font-weight: 700;
                margin-right: 20px;
                color: #0066EE;
            }
            .step-content {
                text-align: left;
            }
            .step-content h2 {
                font-size: 32px;
                margin-top: 0;
                color: #000;
                font-weight: 600;
                margin-bottom: 16px;
            }
            .step-content p {
                font-size: 18px;
                margin-bottom: 0;
                color: #8E8E93;
                line-height: 1.6;
            }
            
            /* Apps section styles */
            .apps-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                background-color: #1D1D1D;
                color: #fff;
                padding: 3rem;
                min-height: 100vh;
            }
            .app-grid {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 20px;
                max-width: 800px;
                margin: 0 auto;
            }
            .app-grid img {
                width: 100px;
                height: 100px;
                object-fit: contain;
                border-radius: 15px;
                background-color: white;
                padding: 10px;
            }
            .apps-container h1 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            .apps-container h2 {
                font-size: 2rem;
                margin-bottom: 2rem;
            }
            
            /* Food tracking section styles */
            .food-tracking-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 90vh;
                background: linear-gradient(90deg, #FF9800 0%, #FFEB3B 100%);
                color: white;
                padding: 20px;
            }
            .food-tracking-container h1 {
                font-size: 3rem;
                margin-bottom: 1rem;
            }
            .food-tracking-container p {
                font-size: 1.5rem;
                margin-bottom: 2rem;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Hero Section
    st.markdown(
        """
        <div class="hero-container">
            <div class="content">
                <h2>Reach your goals</h2>
                <h2>With YuMe  </h2>
                <h6>Build healthy habits with the all-in-one food, exercise, and calorie tracker</h6>
                <div class="button-container">
        """,
        unsafe_allow_html=True
    )
    
    if st.button("START TODAY", key="start_button", type="primary"):
        st.session_state["show_homepage"] = False

    st.markdown("</div></div></div>", unsafe_allow_html=True)

    # Steps Section
    st.markdown(
        """
        <div class="steps-container">
            <div class="step">
                <div class="step-number">1</div>
                <div class="step-content">
                    <h2>Track your diet, workouts & progress</h2>
                    <p>Track your calories and macros, get personalized insights, and reach your goals.</p>
                </div>
            </div>
            <div class="step">
                <div class="step-number">2</div>
                <div class="step-content">
                    <h2>Understand what works</h2>
                    <p>Gain insights into your daily patterns and make positive changes for lasting success</p>
                </div>
            </div>
            <div class="step">
                <div class="step-number">3</div>
                <div class="step-content">
                    <h2>Upload your medical records, and goals</h2>
                    <p>Share your medical records and goals for custom-built recommendations that fits your bodies needs</p>
                </div>
            </div>
            <div class="step">
                <div class="step-number">4</div>
                <div class="step-content">
                    <h2>Decode the truth about packaged foods</h2>
                    <p>Take a picture of any packaged food item and get detailed nutrition analysis tailored to you</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Apps Integration Section
    integration_section()


    # Food Tracking Section
    st.markdown(
        """
        <div class="food-tracking-container">
            <h1>The Indian Context!</h1>
            <p>The first food app that caters to 1000+ Indian foods</p>
            <p>Take a picture of your curries </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        .footer {
            text-align: center;
            padding: 20px;
            background-color: #f8f9fa;
            margin: 0;
            position: relative;  /* Changed from fixed */
            width: 100%;
        }
        .footer p {
            margin: 0;
            color: #6c757d;
            font-size: 16px;
        }
        /* Remove the Streamlit container modifications since we want normal scrolling */
        </style>
        <div class="footer">
            <p>Made with ❤️ by Aaradhya and Saundarya</p>
        </div>
        """,
        unsafe_allow_html=True
    )