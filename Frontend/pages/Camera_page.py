import streamlit as st

st.title('Please take your picture 📷')
picture = st.camera_input(label="Camera:", 
                          label_visibility='hidden')

if picture is not None:
    st.switch_page("pages/Questions.py")