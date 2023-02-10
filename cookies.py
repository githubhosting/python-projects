import os.path
import pickle
from urllib.parse import urlparse
import time

__author__ = "amitharun3@gmail.com"

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def waitFor(foo, waiter=.5):
    while True:
        try:
            time.sleep(waiter)
            if r := foo(): return r
        except NoSuchElementException:
            pass


def waitTill(foo, waiter=1):
    while True:
        try:
            time.sleep(waiter)
            if not foo(): break
        except NoSuchElementException:
            break


def highlight(element, effect_time, color, border):
    driver = element._parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

    original_style = element.get_attribute('style')
    apply_style(original_style + "border: {0}px solid {1};".format(border, color))
    time.sleep(effect_time)
    apply_style(original_style)


ckk = 'cookies'


def getCkk(url):
    return ckk + '-' + urlparse(url).netloc + '.' + 'pkl'


def login(driver, url):
    driver.get(url)
    waitTill(lambda: driver.find_element(By.XPATH, '//*[@id="mainHeader"]/div[2]/div[2]/div[2]/button'))


def dump(driver, url):
    driver.get(url)
    pickle.dump(driver.get_cookies(), open(getCkk(url), "wb"))


def load(driver, url):
    ckk_ = getCkk(url)
    if not os.path.exists(ckk_):
        login(driver, url)
        dump(driver, url)
        return
    driver.get(url)
    cookies = pickle.load(open(ckk_, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
