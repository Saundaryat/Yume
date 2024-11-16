import streamlit as st

def steps_section():
    st.markdown(
        """
        <style>
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
        </style>
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