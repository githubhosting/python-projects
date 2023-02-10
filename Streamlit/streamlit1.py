import streamlit as st
import numpy as np
import pandas as pd

st.title("My First Streamlit app")

button = st.button('Click me')
if button:
    st.write("You clicked me")
else:
    st.write("You didn't click me")

st.text_input("Input a nuber to be squared", key="y")
y = st.session_state.y
if y:
    st.write(y, "Square is: ", int(y) ** 2)

choice = st.radio("Select a number", [1, 2, 3, 4, 5])
st.write("You selected", choice)

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")
st.subheader('Raw data')
st.write(data)
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)
st.subheader('Map of all pickups')
st.map(data)
hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)