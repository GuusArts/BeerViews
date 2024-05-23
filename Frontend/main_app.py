import streamlit as st
from Backend.Main_appController import main_appController

container = st.container(border=True)
container.write("This is inside the container")