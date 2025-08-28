import streamlit as st
from PIL import Image
import google.generativeai as genai
import io

# Configure API key
GOOGLE_API_KEY = "AIzaSyCdrkERQkN2Lrgd4YZTH9_QZq8XAtLtGxM"
genai.configure(api_key=GOOGLE_API_KEY)

# Function to load Gemini model and get responses
def get_gemini_response(input_text, image=None):
    model = genai.GenerativeModel("gemini-1.5-flash")

    parts = []
    if input_text:
        parts.append(input_text)

    if image:
        # Convert PIL image to bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format="PNG")
        img_bytes = img_byte_arr.getvalue()

        parts.append({
            "mime_type": "image/png",
            "data": img_bytes
        })

    response = model.generate_content(parts)
    return response.text

# Streamlit UI
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")

input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

if st.button("Tell me about the image"):
    if input_text or image:
        try:
            response = get_gemini_response(input_text, image)
            st.subheader("The Response is")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please provide input text or upload an image.")
