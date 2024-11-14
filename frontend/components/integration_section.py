import streamlit as st

def integration_section():
    st.markdown("""
        <style>
            .integration-container {
                background-color: #1A1B1E;
                padding: 60px 40px;
                border-radius: 20px;
                margin: 20px 0;
            }
            .integration-header {
                color: #ffffff;
                margin-bottom: 40px;
            }
            .integration-subheader {
                color: #9BA1A6;
                font-size: 1.2rem;
                margin-bottom: 30px;
            }
            .integration-title {
                font-size: 3rem;
                font-weight: bold;
                margin-bottom: 20px;
                line-height: 1.2;
            }
            .app-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
                gap: 20px;
                justify-content: end;
                max-width: 600px;
                margin-left: auto;
            }
            .app-icon {
                background: white;
                border-radius: 15px;
                padding: 15px;
                aspect-ratio: 1;
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .app-icon img {
                width: 100%;
                height: 100%;
                object-fit: contain;
            }
            .integration-content {
                display: grid;
                grid-template-columns: 1fr 1fr;
                align-items: center;
                gap: 40px;
            }
            @media (max-width: 768px) {
                .integration-content {
                    grid-template-columns: 1fr;
                }
                .app-grid {
                    margin: 0 auto;
                }
            }
        </style>
        
        <div class="integration-container">
            <div class="integration-content">
                <div>
                    <div class="integration-header">
                        <div class="integration-subheader">10+ indian apps</div>
                        <div class="integration-title">Sync your food & grocery orders, workouts, medical reports, steps & more</div>
                    </div>
                </div>
                <div class="app-grid">
                    <div class="app-icon">
                        <img src="assets/Apple_Health.webp" alt="Apple Health">
                    </div>
                    <div class="app-icon">
                        <img src="frontend/assets/bigbasket.webp" alt="Bigbasket">
                    </div>
                    <div class="app-icon">
                        <img src="frontend/assets/Blinkit.webp" alt="Blinkit">
                    </div>
                    <div class="app-icon">
                        <img src="frontend/assets/cultfit.webp" alt="Cultfit">
                    </div>
                    <div class="app-icon">
                        <img src="frontend/assets/strava.webp" alt="Strava">
                    </div>
                    <div class="app-icon">
                        <img src="frontend/assets/swiggy.webp" alt="Swiggy">
                    </div>
                    <div class="app-icon">
                        <img src="frontend/assets/zepto.jpg" alt="Zepto">
                    </div>
                    <div class="app-icon">
                        <img src="frontend/assets/zomato.webp" alt="Zomato">
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)