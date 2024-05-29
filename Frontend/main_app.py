import streamlit as st
import APICalls


# FUNCTIONS
def toMarkdownPoints(beers):
    s = ""
    for beer in beers:
        s += "- " + str(beer) + "\n"
    return s

def getBars():
    return APICalls.getAllBars()

def getBeerName(id):
    beer = APICalls.getBeerData(id)
    return beer['name']


# STREAMLIT UI  
bar = None

if bar is None:
    st.session_state.bar = None

bars = getBars()
st.title('Home')

for bar in bars:
    with st.container(border=True):
        st.subheader(bar['name'])
        beer_names = []
        
        for beer_id in bar['beer_ids']:
            beer_names.append(getBeerName(beer_id))
        beers = toMarkdownPoints(beer_names)

        with st.expander("See beer list 🍻"):
            st.markdown(beers)

        if st.button("I am at this bar!", key=bar['id']):
            bar.update({'beer_names':beer_names})
            st.session_state.bar = bar
            st.switch_page(r"pages\Camera_page.py")