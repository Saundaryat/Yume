import streamlit as st

def home_intro():
    # Update CSS styling
    st.markdown(
        """
        <style>
            .section-container {
                padding: 3rem 2rem;
                background-color: white;
                margin-bottom: 3rem;
                text-align: center;
            }
            .title {
                font-size: 3.5rem;
                color: #1E1E1E;
                text-align: center;
                font-weight: 800;
                margin-bottom: 0.5rem;
            }
            .subheader {
                font-size: 1.8rem;
                color: #666;
                text-align: center;
                margin-bottom: 2rem;
                font-weight: 400;
            }
            .stats-container {
                display: flex;
                justify-content: center;
                gap: 2rem;
                margin: 3rem 0;
            }
            .stat-item {
                text-align: center;
            }
            .stat-number {
                font-size: 2.5rem;
                color: #0066EE;
                font-weight: 700;
            }
            .stat-label {
                color: #666;
                font-size: 1.2rem;
            }
            .steps-container {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 2rem;
                margin: 3rem 0;
            }
            .step-item {
                text-align: center;
                padding: 2rem;
            }
            .step-number {
                font-size: 2rem;
                color: #0066EE;
                font-weight: 700;
                margin-bottom: 1rem;
            }
            .step-title {
                font-size: 1.5rem;
                color: #1E1E1E;
                font-weight: 600;
                margin-bottom: 1rem;
            }
            .step-description {
                color: #666;
                font-size: 1.1rem;
                line-height: 1.6;
            }
            .cta-button {
                background-color: #0066EE;
                color: white;
                padding: 1rem 3rem;
                font-size: 1.3rem;
                font-weight: 600;
                border-radius: 8px;
                border: none;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .cta-button:hover {
                background-color: #0052CC;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Hero Section
    st.markdown("<div class='section-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>#1 Health Tracking App</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subheader'>Reach your goals with YuMe</h2>", unsafe_allow_html=True)
    
    # Stats Section
    st.markdown(
        """
        <div class='stats-container'>
            <div class='stat-item'>
                <div class='stat-number'>3.7M+</div>
                <div class='stat-label'>Active Users</div>
            </div>
            <div class='stat-item'>
                <div class='stat-number'>18M+</div>
                <div class='stat-label'>Products Database</div>
            </div>
            <div class='stat-item'>
                <div class='stat-number'>35+</div>
                <div class='stat-label'>Connected Apps</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Steps Section
    st.markdown("<h2 style='text-align: center; font-size: 2rem; margin: 3rem 0;'>Hit your health goals in 1-2-3</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='steps-container'>
            <div class='step-item'>
                <div class='step-number'>1</div>
                <div class='step-title'>Track Everything</div>
                <div class='step-description'>Track nutrition, fitness & wellness with our smart AI-powered tools</div>
            </div>
            <div class='step-item'>
                <div class='step-number'>2</div>
                <div class='step-title'>Get Insights</div>
                <div class='step-description'>Receive personalized analysis and recommendations based on your data</div>
            </div>
            <div class='step-item'>
                <div class='step-number'>3</div>
                <div class='step-title'>Achieve Results</div>
                <div class='step-description'>Build healthy habits and reach your goals with our guidance</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # CTA Button
    if st.button("Start Your Journey Today", key="start_button", type="primary"):
        st.session_state["show_homepage"] = False