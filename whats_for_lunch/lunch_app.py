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
    df = pd.read_csv('whats_for_lunch/local_restaurants.csv')
    df.style.hide_index()

    ### Variables ###
    filter_cuisine = 'American'



    ### Webpage ###
    
    st.markdown("#")
    st.title("What's for lunch?")
    st.markdown("#")

    select_cuisine = st.selectbox("Choose cuisine and press Select Restaurant:",
    ('American', 'Asian', 'BBQ', 'Fast Food', 'French', 'Italian', 
    'Irish Pub', 'Mediterranean', 'Mexican', 'Pizza')
    )
    filter_cuisine = select_cuisine

    
    filtered_list = df[
        (df['cuisine']==filter_cuisine)
    ]['restaurants'].unique()

    if st.button('Select Restaurant'):        
        restaurant = random.choice(filtered_list)
        menu = df[df['restaurants']==restaurant]['menu'].tolist()[0]
        address= df[df['restaurants']==restaurant]['address'].tolist()[0]
        phone= df[df['restaurants']==restaurant]['phone'].tolist()[0]
        for_maps = "_".join(address.split())
        city = df[df['restaurants']==restaurant]['city'].tolist()[0]
        state = df[df['restaurants']==restaurant]['state'].tolist()[0]


        map_search= f'https://www.google.com/maps/search/{restaurant}+{city}+{state}'
        gmaps = "_".join(map_search.split())

        st.markdown("#")
        col1, col2 = st.beta_columns(2)

        with col1:
            st.title(restaurant)
            st.write(f"[Click to view menu.]({menu})")
        with col2:
            st.markdown('**Details from Google Maps:**')
            st.write(address)
            st.write(phone)
            st.write(f"[See in Google Maps.]({gmaps})")

        st.markdown("#")
        with st.beta_expander(f"Click for other {select_cuisine} options."):
                other_restauarants = df[
                    (df['cuisine'] == filter_cuisine)][['restaurants', 'menu']]
                other_restauarants.set_index('restaurants', inplace=True)
                other_restauarants.rename(columns={'menu':""}, inplace=True)
                st.dataframe(data=other_restauarants)
               
    else:
        st.title("")
    

if __name__ == '__main__':
    main()
