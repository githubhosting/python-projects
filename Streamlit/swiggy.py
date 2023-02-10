import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd
import time
import streamlit as st

# Used headers/agent as the request timed out and asking for agent. Using following code you can fake the agent.
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'}

# Target url
url="https://www.swiggy.com"

# Content from swiggy homepage and saving all the city name listed there
response_city = requests.get(url, headers=headers)
content_city = response_city.content
soup_city = BeautifulSoup(content_city, "html.parser")
name_city = soup_city.find_all("div", attrs={"class": "_2Im4A"})
print(name_city)
st.write(name_city)

# url_city=[]
# for i in range(3,7):
#     for a in name_city[i].find_all('a', href=True):
#             url_city.append(a['href'])
# print("Total City: ",len(url_city))
#
# st.write("Total City: ",len(url_city))
