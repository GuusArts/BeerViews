import streamlit as st
import APICalls

def get_all_beer_names():
    return APICalls.getAllBeerNames()


st.header("Please answer these questions for a better result")
with st.form("my_form"):
    st.write("What is your top 5 beer?")

    options = st.multiselect(
        label="Choose 5 beers",
        options=get_all_beer_names())

    # Every form must have a submit button.
    st.form_submit_button("Submit")