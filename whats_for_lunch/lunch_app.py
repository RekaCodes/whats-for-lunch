# import libraries
import streamlit as st
st.set_page_config(layout="wide")

import pandas as pd
import numpy as np
import datetime as dt
import random

import plotly.express as px
import plotly.graph_objects as go

# import data
from restaurants import list, df



# build app

def main():

    ### Variables ###
    filter_cuisine = 'American'
    filter_fast = 0
    filter_dine_in = 0

    ### Sidebar ###

    select_cuisine = st.sidebar.selectbox("Cuisine:",
    ('American', 'Asian', 'Fast Food', 'French', 'Greek', 'Italian', 'Mexican')
    )
    st.sidebar.write('You selected', select_cuisine)
    filter_cuisine = select_cuisine

    check_fast = st.sidebar.checkbox("In a hurry?")
    if check_fast:
        st.sidebar.write("Get it fast.")
        filter_fast = 1

    check_dine_in = st.sidebar.checkbox("Dining In?")
    if check_dine_in:
        st.sidebar.write("I'll get your table ready.")
        filter_dine_in = 1


    
    ### Webpage ###
    st.title("What's for lunch?")
        
    st.write("Just press the button below to choose a restaurant.")

    if st.button('Choose Restaurant'):        
        restaurant = random.choice(list)
        st.write(restaurant)


    ### Expand for more options ###
    with st.beta_expander("Click for more options."):
        st.table(data=df[
            (df['cuisine'] == filter_cuisine)])

if __name__ == '__main__':
    main()
