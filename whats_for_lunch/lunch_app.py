# import libraries
import streamlit as st
st.set_page_config(layout="centered")

import pandas as pd
import numpy as np
import datetime as dt
import random

import plotly.express as px
import plotly.graph_objects as go

# import data
# from restaurants import list, df



# build app

def main():

    df = pd.read_csv('local_restaurants.csv')
    df.style.hide_index()

    ### Variables ###
    filter_cuisine = 'American'
    filter_fast = 0
    filter_dine_in = 0

 
    ### Webpage ###
    

    st.title("What's for lunch?")
    

    select_cuisine = st.selectbox("Choose your cuisine:",
    ('American', 'Asian', 'BBQ', 'Fast Food', 'French', 'Italian', 
    'Irish Pub', 'Mediterranean', 'Mexican', 'Pizza')
    )
    filter_cuisine = select_cuisine
    

    filtered_list = df[
        (df['cuisine']==filter_cuisine)
    ]['restaurants'].unique()


    # st.write("Just press the button below to choose a restaurant.")

    if st.button('Choose Restaurant'):        
        restaurant = random.choice(filtered_list)
        st.write(restaurant)
    else:
        st.write("")


    ### Expand for more options ###
    with st.beta_expander(f"Click for other {select_cuisine} options."):
        st.dataframe(data=df[
            (df['cuisine'] == filter_cuisine)]['restaurants'])

if __name__ == '__main__':
    main()
