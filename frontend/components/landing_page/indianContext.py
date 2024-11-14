import streamlit as st

def indian_context():
    st.markdown(
        """
        <style>
            /* Food tracking section styles */
            .food-tracking-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 90vh;
                color: white;
                padding: 20px;
                background: url('https://i.ibb.co/mN7bTMx/indian-context.webp');
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                background-repeat: no-repeat;
                position: relative;
                overflow: hidden;
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
        <div class="food-tracking-container">
            <h1>The Indian Context!</h1>
            <p>The first food app that caters to 1000+ Indian foods</p>
            <p>Take a picture of your curries </p>
        </div>
        """,
        unsafe_allow_html=True
    )