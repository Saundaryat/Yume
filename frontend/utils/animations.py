import json
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def display_exercise_animations(excercises_result):
    excercises_data = json.loads(excercises_result)
    for exercise, lottie_file in [("cycling", "cycling.json"), ("swimming", "swimming.json"), ("running", "running.json")]:
        if exercise in excercises_data:
            st.markdown(f"**{exercise.capitalize()}**: {excercises_data[exercise]}")
            st_lottie(load_lottie_file(f"frontend/animation/{lottie_file}"), height=150, width=150)
