import streamlit as st
import APICalls

# FUNCTIONS
@st.cache_data
def get_all_beer_names():
    return APICalls.getAllBeerNames()

def setBeerRecommendation(beer):
    st.session_state.beer = beer

def on_submit(car, top_beers, worst_beers):
    return APICalls.getRecommendedBeer(car, top_beers, worst_beers)

def get_beer(scores):
    indexes = []
    beer_names = st.session_state.bar.get('beer_names', [])

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

# Fetch beer names once and cache the result
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
        st.write("What are your least favorite beers?")
        worst_beers = st.multiselect(
            label="Choose beers",
            key='Worst',
            options=beer_names)
        
        st.write('')
        st.write("Are you with the car🚗?")
        car = st.radio("Ready to act responsible?",
                        ["Yes", "No"],
                        captions=['Drive safe', 'Drink safe'])

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")

        if submitted and len(top_beers) >= 3:
            with st.spinner("Fetching recommendations..."):
                scores = on_submit(car, top_beers, worst_beers)
                st.session_state.recommended_beers = get_beer(scores)
        elif submitted:
            st.error('Please submit more beer for a better result')

if st.session_state.recommended_beers:
    st.write(sorted(st.session_state.recommended_beers, key=lambda x: x[1], reverse=True))