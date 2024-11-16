import streamlit as st

def hero_section():
    st.markdown(
        """
        <style>
            /* Hero section styles */
            .hero-container {
                display: flex;
                justify-content: center;
                align-items: center;
                # height: calc(80vh - 80px);
                height: 60vh;
                background: linear-gradient(90deg, #00BFA5 0%, #FFEB3B 100%);
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
                background: linear-gradient(90deg, #00BFA5 0%, #FFEB3B 100%);
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
        </style>
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