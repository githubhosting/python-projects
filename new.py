# Used to import the webdriver from selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


# Get the path of chromedriver which you have install

def startBot(username, password, url):
    path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(path)

    # opening the website in chrome.
    driver.get(url)

    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element_by_name(
        "username").send_keys(username)

    # find the password by inspecting on password input
    driver.find_element_by_name(
        "password").send_keys(password)

    # click on submit
    driver.find_element_by_css_selector(
        "MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-fullWidth RaLoginForm-button css-1qelgoy").click()


# Driver Code
# Enter below your login credentials
username = "admin@foodey.com"
password = "adminfoodey"

# URL of the login page of site
# which you want to automate login.
url = "https://adminpannel.vercel.app/#/login"

# Call the function
startBot(username, password, url)
