import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="Image Background")

st.write("## Remove Background from your Image ##")
st.write(
    "Try uploading an image to watch the background removed quickly"
)

st.sidebar.write("## Upload and Download :gear:")

MAX_FILE_SIZE = 5*1024*1024 #5mb

#download the image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    bytes_im = buf.getvalue()
    return bytes_im

def fix_Image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("New Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download New image", convert_image(fixed), "new.png", "image/png")

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an Image", type=["png","jpg","jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded image size is too large")
    else:
        fix_Image(upload=my_upload)
else:
    fix_Image("naruto.jpg")