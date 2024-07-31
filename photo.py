import streamlit as st
from PIL import Image
import google.generativeai as genai

# Directly set the API key
GOOGLE_API_KEY = "AIzaSyCdrkERQkN2Lrgd4YZTH9_QZq8XAtLtGxM"
genai.configure(api_key=GOOGLE_API_KEY)

# Function to load OpenAI model and get responses
def get_gemini_response(input_text, image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, image])
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

# If the submit button is clicked
if submit:
    if input_text or image:
        response = get_gemini_response(input_text, image)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please provide input text or upload an image.")
