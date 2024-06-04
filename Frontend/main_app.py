import streamlit as st
import APICalls
from concurrent.futures import ThreadPoolExecutor

# FUNCTIONS
@st.cache_data
def getBars():
    return APICalls.getAllBars()

@st.cache_data
def get_beer_data(beer_ids):
    # Assume APICalls.getBeersData(beer_ids) fetches data for multiple beers at once
    return APICalls.getBeersData(beer_ids)

# STREAMLIT UI
bar = None
beer_info = None

if bar is None:
    st.session_state.bar = None

if beer_info is None:
    st.session_state.beer_info = None

bars = getBars()
st.title('Home')

# Using ThreadPoolExecutor to fetch beer data concurrently
def fetch_beer_data_concurrently(beer_ids):
    with ThreadPoolExecutor() as executor:
        beer_data_list = list(executor.map(APICalls.getBeerData, beer_ids))
    return beer_data_list

for bar in bars:
    with st.container(border=True):
        name_col, button_col = st.columns([3,1])
        beer_names = []

        with name_col:
            st.subheader(bar['name'])

        with st.expander("See beer list 🍻"):
            beer_data_list = fetch_beer_data_concurrently(bar['beer_ids'])
            for beer_data in beer_data_list:
                col1, col2 = st.columns([3, 1])  # Adjust the width ratio as needed

                with col1:
                    beer_names.append(beer_data['name'])
                    st.write(beer_data['name'])

                with col2:
                    if st.button("Chat with me", key=beer_data['id']):
                        st.session_state.beer = beer_data
                        st.switch_page(r"pages\Chatbot_page.py")
        
        with button_col:
            if st.button("I am at this bar!", key=bar['id']):
                bar.update({'beer_names':beer_names})
                st.session_state.bar = bar
                st.switch_page(r"pages\Camera_page.py")