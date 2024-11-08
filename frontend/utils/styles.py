import streamlit as st

def apply_custom_styles():
    st.markdown(
        """
        <style>
        body {background-color: #f7f9fc; font-family: 'Poppins', sans-serif;}
        .stButton button {background-color: #4CAF50; color: white; border-radius: 12px;}
        .stButton button:hover {background-color: #45a049;}
        </style>
        """, unsafe_allow_html=True
    )
