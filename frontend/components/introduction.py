import streamlit as st

def home_intro():
    # CSS styling for the main container and sections
    st.markdown(
        """
        <style>
            .section-container {
                padding: 2rem;
                background-color: #f9f9f9;
                border-radius: 10px;
                box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
                margin-bottom: 2rem;
                transition: transform 0.3s;
            }
            .section-container:hover {
                transform: scale(1.02);
            }
            .title {
                font-size: 2.5rem;
                color: #2C3E50;
                text-align: center;
                font-weight: 700;
                margin-bottom: 1rem;
            }
            .subheader {
                font-size: 1.5rem;
                color: #34495E;
                text-align: center;
                margin-bottom: 2rem;
            }
            .section-heading {
                font-size: 2rem;
                color: #1ABC9C;
                font-weight: 600;
                margin-top: 2rem;
                text-align: left;
            }
            .section-content {
                font-size: 1.2rem;
                color: #2C3E50;
                line-height: 1.6;
                margin-top: 1rem;
            }
            .section-divider {
                height: 2px;
                background-color: #16A085;
                margin: 2rem 0;
                border-radius: 5px;
            }
            .start-button {
                display: block;
                margin: 2rem auto;
                padding: 1rem 2rem;
                font-size: 1.2rem;
                background-color: #1ABC9C;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                text-align: center;
            }
            .start-button:hover {
                background-color: #16A085;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Welcome Section
    st.markdown("<div class='section-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Welcome to YuMe</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subheader'>Your Personalized Health and Wellness Companion</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Divider
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    # "Learn What Works" Section
    st.markdown("<div class='section-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-heading'>Learn What Works</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p class='section-content'>
        Personalized nutrition insights reveal what's working so you can make smarter choices.
        Track your health goals, calorie intake, and nutritional insights with YuMe's intuitive interface.
        </p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Divider
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    # "Analyze Products" Section
    st.markdown("<div class='section-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-heading'>Analyze Products</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p class='section-content'>
        Upload images of products to receive real-time ingredient analysis and tailored feedback. 
        YuMe helps you make informed decisions about the products you consume.
        </p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Divider
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    # "Personalized Recommendations" Section
    st.markdown("<div class='section-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-heading'>Personalized Recommendations</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p class='section-content'>
        Based on your health records and preferences, get customized recommendations for better health.
        YuMe empowers you with tools to make sustainable health choices.
        </p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Final Start Button
    if st.button("Start Exploring YuMe", key="start_button"):
        st.session_state["show_homepage"] = False  # Switch to main interface