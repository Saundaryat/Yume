import streamlit as st

def landing_page_styling():
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
        </style>
        """,
        unsafe_allow_html=True
    )