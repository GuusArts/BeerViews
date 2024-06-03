import streamlit as st
import APICalls

def get_all_beer_names():
    return APICalls.getAllBeerNames()

def setBeerRecommendation(beer):
    st.session_state.beer = beer

def on_submit(car, top_beers, lowest_beer:False):
    st.session_state.recommended_beers = APICalls.getRecommendedBeer(car, top_beers, lowest_beer)

if "submitted_questions" not in st.session_state:
    st.session_state.submitted_questions = False

if "recommended_beers" not in st.session_state:
    st.session_state.recommended_beers = []

st.header("Please answer these questions for a better result")
with st.container():
    with st.form("Questions_form"):
        st.write("What are your top 3 beers🍻?")
        top_beers = st.multiselect(
            label="Choose beers",
            key='Top',
            options=get_all_beer_names())
        
        st.write('')
        st.write("What are your least favorite beer?")
        worst_beers = st.multiselect(
            label="Choose beers",
            key='Worst',
            options=get_all_beer_names())
        
        st.write('')
        st.write("Are you with the car🚗?")
        car = st.radio("Ready to act responsible?",
                        ["Yes", "No"],
                        captions = ['Drive save', 'Drink save'])

        # Every form must have a submit button.
        st.session_state.submitted_questions = st.form_submit_button("Submit")

        if st.session_state.submitted_questions and len(top_beers) >= 3:
            on_submit(car, top_beers, worst_beers)
        else:
            st.error('Please submit more beer for a better result')
st.header(st.session_state.recommended_beers)