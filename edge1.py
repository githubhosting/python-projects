from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    B_URL = "./chromedriver.exe"
    T_URL = "https://www.tutorialspoint.com/about/about_careers.htm"

    browser = webdriver.Chrome(executable_path=B_URL)
    browser.implicitly_wait(20)
    browser.get(T_URL)
