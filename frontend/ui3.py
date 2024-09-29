import streamlit as st
from PIL import Image

# Title of the app
st.title("Conversational Image & Text to Text Converter")

# Introductory message to guide the user
st.write("You can upload an image or enter text to start a conversation!")

# Create an expandable section for uploading images
with st.expander("Upload an image"):
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Create a row for text input and the submit button
col1, col2 = st.columns([3, 1])  # Adjust column widths as needed

with col1:
    user_text_input = st.text_area("Enter text here:")

with col2:
    submit_button = st.button("Submit")

# Placeholder for API response
response_placeholder = st.empty()

# If an image or text is provided, enable processing
if uploaded_file or user_text_input:
    
    # If the image is uploaded, show it in the app
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    # Process when the submit button is clicked
    if submit_button:
        if uploaded_file:
            # Simulate response for image input
            dummy_extracted_text = "Dummy text extracted from the uploaded image."
            response_placeholder.write("### API Response for Image")
            response_placeholder.text(dummy_extracted_text)

        if user_text_input:
            # Simulate response for text input
            dummy_response_text = f"You entered: {user_text_input}. This is a simulated response."
            response_placeholder.write("### API Response for Text")
            response_placeholder.text(dummy_response_text)

        # Automatically scroll down to the response area
        response_placeholder.markdown("---")  # Adds a horizontal line for separation
        st.experimental_rerun()  # Rerun the app to focus on the response area

else:
    st.write("Upload an image or enter text to proceed!")
