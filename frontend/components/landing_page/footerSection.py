import streamlit as st

def footer_section():
    st.markdown(
        """
        <style>
        .footer {
            text-align: center;
            padding: 20px;
            background-color: #f8f9fa;
            margin: 0;
            position: relative;  /* Changed from fixed */
            width: 100%;
            background: linear-gradient(90deg, #FF9800 0%, #FFEB3B 100%);
        }
        .footer p {
            margin: 0;
            color: #6c757d;
            font-size: 16px;
        }
        /* Remove the Streamlit container modifications since we want normal scrolling */
        </style>
        <div class="footer">
            <p>Made with ❤️ by Aaradhya and Saundarya</p>
        </div>
        """,
        unsafe_allow_html=True
    )