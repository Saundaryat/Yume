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
            .food-tracking-container::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.5); 
                z-index: 1;
            }
            .food-tracking-content {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                position: relative;
                z-index: 2;
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
            <div class="food-tracking-content">
                <h1>The Indian Context!</h1>
                <p>The only health app that caters to 1000+ Indian foods</p>
                <p>Take a picture of your curries  </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )