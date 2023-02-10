from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('C:\Program Files\Google\Chrome\Application\chrome.exe')
browser = webdriver.Chrome(service=s)
url = 'https://adminpannel.vercel.app/#/login'
browser.get(url)
