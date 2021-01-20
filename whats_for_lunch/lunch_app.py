# import libraries
import streamlit as st
st.set_page_config(layout="centered")

import pandas as pd
import numpy as np
import datetime as dt
import random


# build app

def main():

    ### data ###
    df = pd.read_csv('local_restaurants.csv')
    df.style.hide_index()

    ### Variables ###
    filter_cuisine = 'American'
    filter_fast = 0
    filter_dine_in = 0

 
    ### Sidebar ###

    st.sidebar.title("What's for lunch?")

    select_cuisine = st.sidebar.selectbox("Choose your cuisine:",
    ('American', 'Asian', 'BBQ', 'Fast Food', 'French', 'Italian', 
    'Irish Pub', 'Mediterranean', 'Mexican', 'Pizza')
    )
    filter_cuisine = select_cuisine



    ### Webpage ###
    
    st.markdown("#")
    # st.title("What's for lunch?")
    st.markdown("#")
    
    # st.markdown("#")
    container_restaurant = st.beta_container()


    
    filtered_list = df[
        (df['cuisine']==filter_cuisine)
    ]['restaurants'].unique()

    # st.dataframe(data=df)

    if st.sidebar.button('Select Restaurant'):        
        restaurant = random.choice(filtered_list)
        menu = df[df['restaurants']==restaurant]['menu'].tolist()[0]
        
        container_restaurant.title(restaurant)
        container_restaurant.write("---")
        container_restaurant.write(f"[Click to view menu.]({menu})")
        st.markdown("#")
        with st.beta_expander(f"Click for other {select_cuisine} options."):
                other_restauarants = df[
                    (df['cuisine'] == filter_cuisine)][['restaurants', 'menu']]
                other_restauarants.set_index('restaurants', inplace=True)
                other_restauarants.rename(columns={'menu':""}, inplace=True)
                st.dataframe(data=other_restauarants)
               
    else:
        container_restaurant.header("Choose cuisine and press Select Restaurant.")
        container_restaurant.write("---")

    st.markdown("#")

    st.write()
    

if __name__ == '__main__':
    main()
