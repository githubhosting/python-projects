import streamlit as st
from selenium import webdriver
import pandas as pd

DRIVER_URL = "./chromedriver.exe"
TARGET_URL = "https://www.tomshardware.com/reviews/gpu-hierarchy,4388.html"


driver = webdriver.Chrome(executable_path=DRIVER_URL)
driver.get(TARGET_URL)
driver.implicitly_wait(0.5)

gpus = driver.find_elements_by_xpath('//td[@class="table_body__data" colspan="1" style="text-align:left"]')

gpu_list = []
for gpu in range(len(gpus)):
    gpu_list.append(gpus[gpu].text)
print(gpu_list)
