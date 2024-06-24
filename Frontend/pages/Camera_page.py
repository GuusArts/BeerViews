import os
import cv2
import numpy as np
import streamlit as st
from deepface import DeepFace

st.header(f"Welcome to the {st.session_state.bar['name']}", divider='gray')
st.subheader('Please take your picture 📷')

picture = st.camera_input(label="Camera:", 
                          label_visibility='hidden')

if picture:
    # Read the file bytes
    file_bytes = np.asarray(bytearray(picture.read()), dtype=np.uint8)

    # Decode the file bytes to an image
    picture = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    cv2.imwrite(r'Brewgle\Frontend\Images\Picture1.jpg', picture)

    objs = DeepFace.analyze(
        img_path = r'Brewgle\Frontend\Images\Picture1.jpg', 
        actions = ['emotion'],
        enforce_detection = False
    )
    
    st.session_state.emotion = objs[0]['dominant_emotion']
    os.remove(r'Brewgle\Frontend\Images\Picture1.jpg')
    
    st.switch_page("pages/Questions.py")