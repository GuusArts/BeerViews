import streamlit as st
import APICalls


# FUNCTIONS
def getBars():
    return APICalls.getAllBars()

def get_beer_data(id):
    beer = APICalls.getBeerData(id)
    return beer


# STREAMLIT UI  
bar = None
beer_info = None

if bar is None:
    st.session_state.bar = None

if beer_info is None:
    st.session_state.beer_info = None

bars = getBars()
st.title('Home')

for bar in bars:
    with st.container(border=True):
        name_col, button_col = st.columns([3,1])
        beer_names = []

        with name_col:
            st.subheader(bar['name'])

        with st.expander("See beer list 🍻"):
            for beer_id in bar['beer_ids']:
                beer_data = get_beer_data(beer_id)
                col1, col2 = st.columns([3, 1])  # Adjust the width ratio as needed

                with col1:
                    beer_names.append(beer_data['name'])
                    st.write(beer_data['name'])

                with col2:
                    if st.button("Chat with me", key=beer_id):
                        st.session_state.beer = beer_data 
                        st.switch_page(r"pages\Chatbot_page.py")
        
        with button_col:
            if st.button("I am at this bar!", key=bar['id']):
                bar.update({'beer_names':beer_names})
                st.session_state.bar = bar
                st.switch_page(r"pages\Camera_page.py")