import requests
from bs4 import BeautifulSoup

# url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
url = 'https://myselfshravan.github.io/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())
# print(soup.find_all('p')[1].get_text())
# print(soup.find_all('i', class_='skills__name1'))
print(soup.find_all('h2', id='skills'))
