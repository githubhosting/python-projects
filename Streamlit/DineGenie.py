import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('DineGenie')
st.subheader("Discover your next craving")

categories = ['American', 'Chinese', 'North Indian', 'Italian', 'South Indian']

food = ["Rolls", "Burger", "Pizza", "Biryani", "Pasta", "Sandwich", "Roti Curry"]

sides = ["Fries", "Salad", "Noodles", "Rice", "Soup", "Bread", "Chips", "Sauce", "Dessert", "Ice Cream", "Beverages"]

random_food = np.random.choice(food)
random_side = np.random.choice(sides)

st.write("Spin the wheel to discover your next craving")
my_bar = st.progress(0)
if st.button('Spin'):
    em = st.empty()
    for i in range(100):
        rnd_food = np.random.choice(food)
        em.markdown(f"**{rnd_food}**")
        time.sleep(0.1)
        my_bar.progress(i + 1)

    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)
    st.subheader(f" You can have {random_food} with {random_side}")
