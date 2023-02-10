from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.tomshardware.com/reviews/gpu-hierarchy,4388.html'

browser = webdriver.Chrome()
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')
# print(soup.prettify())
find = soup.find_all('tr', class_='table__body__row')
for i in find:
    print(i.text)
