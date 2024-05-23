import streamlit as st

options = st.multiselect(
    "What is your top 5 beer",
    options=['Beer1', 'Beer2', 'Beer3'])

st.write(options)