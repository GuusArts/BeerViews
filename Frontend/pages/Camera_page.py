import streamlit as st

st.header(f"Welcome to the {st.session_state.bar['name']}", divider='gray')
st.subheader('Please take your picture 📷')

picture = st.camera_input(label="Camera:", 
                          label_visibility='hidden')

if picture is not None:
    st.switch_page("pages/Questions.py")