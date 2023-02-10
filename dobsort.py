import pandas as pd
import numpy as np
import streamlit as st
from selenium import webdriver

B_URL = "./chromedriver.exe"
T_URL = "https://parents.msrit.edu"
browser = webdriver.Chrome(executable_path=B_URL)
browser.get(T_URL)

df = pd.read_excel("checkdob.xlsx")

df['Date'] = pd.to_datetime(df['DOB']).dt.date
print(df)

with open(f'#ppldata.csv', 'w+') as f:
    f.write(f'USN, Name, Quota\n')
    for i in range(len(df)):
        usn = df['USN'][i]
        d = df['Date'][i].strftime("%d")
        m = df['Date'][i].strftime("%B")[:3]
        y = df['Date'][i].strftime("%Y")
        username = browser.find_element_by_id("username")
        dd = browser.find_element_by_id("dd")
        mm = browser.find_element_by_id("mm")
        yyyy = browser.find_element_by_id("yyyy")
        login = browser.find_elements_by_tag_name("input")[6]
        username.send_keys(f"{usn}")
        dd.send_keys(f"{d}")
        mm.send_keys(f"{m}")
        yyyy.send_keys(f"{y}")
        login.click()
        try:
            name = browser.find_element_by_tag_name("h3")
            td = browser.find_elements_by_tag_name("td")
            if name.text == "Notice Board":
                print(f"{name.text} {usn} is not success")
            else:
                write = f'{usn}, {name.text}, {d}/{m}/{y}, {td[4].text[7:]}\n'
                f.write(write)
                print(f"{name.text} - {td[4].text[7:]}")
            browser.back()
            browser.refresh()
        except Exception as e:
            print(e)
            browser.back()
