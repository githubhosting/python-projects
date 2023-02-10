from selenium import webdriver

B_URL = "./chromedriver.exe"
T_URL = "https://www.selenium.dev/selenium/web/web-form.html"

driver = webdriver.Chrome(executable_path=B_URL)
driver.get(T_URL)
