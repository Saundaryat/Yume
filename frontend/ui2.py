import streamlit as st
import requests
from PIL import Image

# Title of the app
st.title("Image to Text Converter via API")

# File uploader for images
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])

# If an image file is uploaded
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to bytes for API call
    image_bytes = uploaded_file.getvalue()

    # API URL (replace with your actual API endpoint)
    api_url = "https://your-api.com/extract-text"

    # Prepare the file for API request
    files = {"file": image_bytes}

    # Button to trigger text extraction from the API
    if st.button("Extract Text"):
        try:
            # Make the API call
            response = requests.post(api_url, files={"file": uploaded_file})

            # Check for successful response
            if response.status_code == 200:
                extracted_text = response.json().get("text", "")
                st.write("### Extracted Text")
                st.text(extracted_text)
            else:
                st.error(f"Error: {response.status_code} - {response.text}")

        except Exception as e:
            st.error(f"An error occurred: {e}")
 