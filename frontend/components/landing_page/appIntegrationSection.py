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
                        <img src="https://imgs.search.brave.com/GQYluAKjnWv2lfkt46qbKIxonCvOxwuZ92uDiqfYijs/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4w/Lmljb25maW5kZXIu/Y29tL2RhdGEvaWNv/bnMvYXBwbGUtYXBw/cy8xMDAvQXBwbGVf/SGVhbHRoLTUxMi5w/bmc" alt="Apple Health">
                    </div>
                    <div class="app-icon">
                        <img src="https://imgs.search.brave.com/NSj9YltVJwkOVhVJE-EN5-1AntN5l_pCRXCphO0ei9U/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMueW91cnN0b3J5/LmNvbS9jcy9pbWFn/ZXMvY29tcGFuaWVz/L2xvZ29zQzAyMTU3/NTk3ODM2MDQxM3Bu/Zz9mbT1hdXRvJmFy/PTE6MSZtb2RlPWZp/bGwmZmlsbD1zb2xp/ZCZmaWxsLWNvbG9y/PWZmZiZmb3JtYXQ9/YXV0byZ3PTE5MjAm/cT03NQ.jpeg" alt="Bigbasket">
                    </div>
                    <div class="app-icon">
                        <img src="https://imgs.search.brave.com/W4KY9ODWNi9ZoKk-zhbeAJ0gDhJWwuCLBDtvpuo-tHQ/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy8y/LzJhL0JsaW5raXQt/eWVsbG93LXJvdW5k/ZWQuc3Zn" alt="Blinkit">
                    </div>
                    <div class="app-icon">
                        <img src="https://imgs.search.brave.com/Ca4wh3YNSrTyG7WsGzaV50xpl1V3JqtFX0nsSSdTcvI/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cHJvZC53ZWJzaXRl/LWZpbGVzLmNvbS82/MTkxZGM1MTMwNjg3/ZDcwN2NiYzMyZjYv/NjJkNmFjNThmNDdm/MzczYjVjNWVlNzRi/X2N1bHQlMjBmaXQl/MjBsb2dvLnN2Zw" alt="Cultfit">
                    </div>
                    <div class="app-icon">
                        <img src="https://imgs.search.brave.com/8zLE3YYkt-eoFpScM95jh7FAC6wYtUzdHnbuv4ue_nE/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9zdHls/ZXMucmVkZGl0bWVk/aWEuY29tL3Q1XzJ0/bnZoL3N0eWxlcy9j/b21tdW5pdHlJY29u/XzlvMGd5b2Foc29y/YzEucG5n" alt="Strava">
                    </div>
                    <div class="app-icon">
                        <img src="https://imgs.search.brave.com/m7KG0aucC3wnM6fPRajXSVB-rbIQIwlms2hWMjOPjKo/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9vcHBv/c2l0ZWhxLmNvbS9z/dGF0aWMvMmU0MWFi/Njg4MjcxY2JjMTBl/NzcwYzg0NDIyZjJj/ODAvYTJiNjEvMF9t/ZWRpdW1jYXJkc19z/d2lnZ3lfOGFmMTYy/NTkwYi5wbmc" alt="Swiggy">
                    </div>
                    <div class="app-icon">
                        <img src="https://imgs.search.brave.com/svR3KzlQ1D28yjChZFMGSWH2lIjUKRNKa4E5gyFVZuo/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9wbGF5/LWxoLmdvb2dsZXVz/ZXJjb250ZW50LmNv/bS90anpLMC1UQ2tY/QjF6eGttaVJyNVdO/R0p4UXk4N3MxUmRC/eDEwbnFMYmR4UklI/N2JQV3hUa0hfWWlV/TWJZUEZSZm1qNz13/MjQwLWg0ODAtcnc.jpeg" alt="Zepto">
                    </div>
                    <div class="app-icon">
                        <img src="https://imgs.search.brave.com/EiPGbT-yduFZv7dDkET-TpVAKmTMg3zuw1jeAIRGxgE/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/aWNvbnNjb3V0LmNv/bS9pY29uL2ZyZWUv/cG5nLTI1Ni9mcmVl/LXpvbWF0by1sb2dv/LWljb24tZG93bmxv/YWQtaW4tc3ZnLXBu/Zy1naWYtZmlsZS1m/b3JtYXRzLS1mb29k/LWNvbXBhbnktYnJh/bmQtZGVsaXZlcnkt/YnJhbnMtbG9nb3Mt/aWNvbnMtMTYzNzY0/NC5wbmc_Zj13ZWJw/Jnc9MjU2" alt="Zomato">
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)