import streamlit as st

st.title('')

with st.container(border=True):
    st.write('Find the perfect beer:')
    if st.button('Press to start'):
        st.switch_page(r'pages/Camera_page.py')