import streamlit as st
from PIL import Image
import util

st.title("AI Managed Traffic System")

photo = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

background_image = ".\\desk.jpg"  # Replace with the path to your background image
background_css = """
    <style>
       [data-testid="stAppViewContainer"]{
           background-image: linear-gradient(to right top, #051937, #004d7a, #008793, #00bf72, #a8eb12);
       }
    </style>
"""
st.markdown(background_css, unsafe_allow_html=True)

def run(photo):
    util.load(photo)
    # print(obj1)
    util.show_box(photo)
    total_weight =  util.pred(photo)
    util.time_pred(total_weight)

if st.button('Upload'):
    image = Image.open(photo)
    # st.image(image, caption="Uploaded Image", use_column_width=True)
    run('WhatsApp Image 2023-10-14 at 9.32.03 AM.jpeg')

