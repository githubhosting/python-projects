import requests

url_to_parse = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url_to_parse)
print(response)
from bs4 import BeautifulSoup

# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
response = requests.get(url_to_parse)
