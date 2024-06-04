import streamlit as st
import APICalls
import numpy as np

def get_all_beer_names():
    return APICalls.getAllBeerNames()

def setBeerRecommendation(beer):
    st.session_state.beer = beer

def on_submit(car, top_beers, lowest_beer:False):
    return APICalls.getRecommendedBeer(car, top_beers, lowest_beer)

def get_beer(scores):
    indexes = []
    beer_names = st.session_state.bar['beer_names'] # Example list, replace with your actual data

    # Ensure session state contains the bar data
    if 'bar' not in st.session_state or 'beer_names' not in st.session_state.bar:
        st.error("Bar data not found in session state.")
        return []

    try:
        for beer in st.session_state.bar['beer_names']:
            if beer in beer_names:
                indexes.append(beer_names.index(beer))
            else:
                st.warning(f"Beer {beer} not found in the list of beer names.")
        return [(beer_names[i], scores[i]) for i in indexes]

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []



if "submitted_questions" not in st.session_state:
    st.session_state.submitted_questions = False

if "recommended_beers" not in st.session_state:
    st.session_state.recommended_beers = []

beer_names = get_all_beer_names()

st.header("Please answer these questions for a better result")
with st.container():
    with st.form("Questions_form"):
        st.write("What are your top 3 beers🍻?")
        top_beers = st.multiselect(
            label="Choose beers",
            key='Top',
            options=beer_names)
        
        st.write('')
        st.write("What are your least favorite beer?")
        worst_beers = st.multiselect(
            label="Choose beers",
            key='Worst',
            options=beer_names)
        
        st.write('')
        st.write("Are you with the car🚗?")
        car = st.radio("Ready to act responsible?",
                        ["Yes", "No"],
                        captions = ['Drive save', 'Drink save'])

        # Every form must have a submit button.
        st.session_state.submitted_questions = st.form_submit_button("Submit")

        if st.session_state.submitted_questions and len(top_beers) >= 3:
            scores = on_submit(car, top_beers, worst_beers)
            st.session_state.recommended_beers = get_beer(scores)
        else:
            st.error('Please submit more beer for a better result')
st.write(sorted(st.session_state.recommended_beers, key=lambda x: x[1])[::-1])