import streamlit as st
import requests
from PIL import Image

# Title of the app
st.title("Conversational Image & Text to Text Converter")

# Introductory message to guide the user
st.write("You can upload an image or enter text to start a conversation!")

# Create an expandable section for uploading images
with st.expander("Upload an image"):
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Text input option
user_text_input = st.text_area("Enter text here:")

# If an image or text is provided, enable processing
if uploaded_file or user_text_input:
    
    # If the image is uploaded, show it in the app
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        image_bytes = uploaded_file.getvalue()

    # Button to submit both image and text for processing
    if st.button("Submit"):
        try:
            # API URL (replace with your actual API endpoint)
            api_url = "https://your-api.com/process"

            # Prepare the data for the API request
            data = {}
            files = {}
            
            if uploaded_file:
                files['file'] = image_bytes  # Send the image to the API

            if user_text_input:
                data['text'] = user_text_input  # Send the text input to the API

            # Make the API call
            response = requests.post(api_url, files=files, data=data)

            # Check if the request was successful
            /*if response.status_code == 200:
                api_response = response.json()
                extracted_text = api_response.get("text", "")
                
                st.write("### API Response")
                st.text(extracted_text)

            else:
                st.error(f"Error: {response.status_code} - {response.text}")*

        except Exception as e:
            st.error(f"An error occurred: {e}")

else:
    st.write("Upload an image or enter text to proceed!")
