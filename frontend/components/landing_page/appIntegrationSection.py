import streamlit as st

def integration_section():
    st.markdown("""
        <style>
            .integration-container {
                background-color: #1A1B1E;
                padding: 20px;  /* Reduced padding for mobile */
                border-radius: 20px;
                margin: 20px 0;
            }
            .integration-title {
                font-size: 2rem;  /* Smaller font size for mobile */
                font-weight: bold;
                margin-bottom: 20px;
                line-height: 1.3;
            }
            .integration-content {
                display: grid;
                grid-template-columns: 1fr;  /* Single column by default */
                gap: 30px;
            }
            .app-grid {
                display: grid;
                grid-template-columns: repeat(2, 1fr);  /* 2 columns by default */
                gap: 15px;  /* Reduced gap for mobile */
                margin: 0 auto;
                max-width: 100%;  /* Full width on mobile */
            }
            .app-icon {
                padding: 10px;  /* Reduced padding for mobile */
            }
            
            /* Desktop styles */
            @media (min-width: 768px) {
                .integration-container {
                    padding: 60px 40px;
                }
                .integration-content {
                    grid-template-columns: 1fr 1fr;
                }
                .integration-title {
                    font-size: 3rem;
                }
                .app-grid {
                    grid-template-columns: repeat(4, 1fr);
                    gap: 20px;
                    max-width: 600px;
                    margin-left: auto;
                }
                .app-icon {
                    padding: 15px;
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