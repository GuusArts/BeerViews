import streamlit as st

options = st.multiselect(
    "What is your top 5 beer")

st.write("You selected:", options)