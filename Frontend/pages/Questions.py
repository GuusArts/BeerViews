import streamlit as st
import APICalls

def get_all_beer_names():
    return APICalls.getAllBeerNames()

def setBeerRecommendation(beer):
    st.session_state.beer = beer


st.header("Please answer these questions for a better result")
with st.container():
    with st.form("Questions_form"):
        st.write("What are your top beers?")

        options = st.multiselect(
            label="Choose beers",
            options=get_all_beer_names())
        
        st.write("Are you with the car?")
        car = st.radio("Ready to act responsible?",
                        ["Yes", "No"],
                        captions = ['Drive save', 'Drink save'])

        # Every form must have a submit button.
        st.form_submit_button("Submit")