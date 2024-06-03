import streamlit as st
import APICalls

def get_all_beer_names():
    return APICalls.getAllBeerNames()

def setBeerRecommendation(beer):
    st.session_state.beer = beer

def on_submit(car, beers):
    st.session_state.car = car
    st.session_state.top_beers = beers

if "submitted_questions" not in st.session_state:
    st.session_state.submitted_questions = False

st.header("Please answer these questions for a better result")
with st.container():
    with st.form("Questions_form"):
        st.write("What are your top 3 beers?")

        beers = st.multiselect(
            label="Choose beers",
            options=get_all_beer_names())
        
        st.write("Are you with the car?")
        car = st.radio("Ready to act responsible?",
                        ["Yes", "No"],
                        captions = ['Drive save', 'Drink save'])

        # Every form must have a submit button.
        st.session_state.submitted_questions = st.form_submit_button("Submit")

        if st.session_state.submitted_questions and len(beers) >= 3:
            on_submit(car, beers)
        else:
            st.error('Please submit more beer for a better result')