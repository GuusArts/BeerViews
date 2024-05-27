import streamlit as st

options = st.multiselect(
    "What is your top 5 beer",
    options=st.session_state.bar['beer_ids'])

st.write(options)