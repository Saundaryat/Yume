import streamlit as st
from components.landing_page.appIntegrationSection import integration_section
from components.landing_page.footerSection import footer_section
from components.landing_page.indianContext import indian_context
from components.landing_page.stepsSection import steps_section
from components.landing_page.heroSection import hero_section
from components.landing_page.landingPageStyling import landing_page_styling

def home_intro():
    landing_page_styling()

    hero_section()

    steps_section()

    integration_section()

    indian_context()

    footer_section()
