from selenium import webdriver
import time
import cookies
import random

quotes = ["Life is too short to waste time on things that don't matter. Focus on what brings you joy and fulfillment.",
          "The only way to do great work is to love what you do. If you're passionate about something, success will follow.",
          "Success is not about having the best of everything. It's about making the most of what you have.",
          "Happiness is not a destination, it's a journey. Find joy in every step and make the most of every moment.",
          "Believe in yourself and trust the journey. Every experience, good or bad, is preparing you for something better.",
          "Never stop learning, growing, and exploring. The world is full of endless possibilities, embrace them.",
          "Take care of yourself first. When you're at your best, you can give your best to the world.",
          "Be kind, work hard, and stay positive. The rest will fall into place.",
          "Surround yourself with people who lift you up, inspire you, and support you. Life is too short to settle for anything less.",
          "Life is not about waiting for the storm to pass, it's about learning to dance in the rain."]

URL = "https://www.kooapp.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(1)

try:
    cookies.load(driver, URL)
    print("Logged in")
    quote = random.choice(quotes)
    print("Posting: ", end="")
    driver.get(f"{URL}/create")
    text_input = driver.find_element_by_id("koo-create-editable-en")
    for ch in quote:
        text_input.send_keys(ch)
        print(ch, end="")
        time.sleep(.1)
    post_btn = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div/div/div[1]/div[2]/button')
    post_btn.click()
    print("Posted")
finally:
    driver.quit()

# time.sleep(60 * 3)
# print("Waiting for 3min")
