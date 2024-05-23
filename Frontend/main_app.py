import streamlit as st
import APICalls


# FUNCTIONS
def toMarkdownPoints(beers):
    s = ""
    for beer in beers:
        s += "- " + str(beer) + "\n"
    return s


# STREAMLIT UI  
st.title('Home')
bars = [(0, "Koffer"), (1, "BrewgleBar")]

for key, bar in bars:
    with st.container(border=True):
        st.subheader(bar)
        beers = APICalls.getAllBeers(key)
        beers = toMarkdownPoints(beers)

        with st.expander("See beer list 🍻"):
            st.markdown(beers)

