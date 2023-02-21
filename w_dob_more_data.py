import pandas as pd
import numpy as np
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By

B_URL = "./chromedriver.exe"
T_URL = "https://parents.msrit.edu"
# browser = webdriver.Chrome(executable_path=B_URL)
# browser.get(T_URL)

df = pd.read_excel("verifydob.xlsx")
df['Date'] = pd.to_datetime(df['DOB']).dt.date

with open(f'#ppldata.csv', 'w+') as f:
	row1 = f"USN, NAME, UHV, Kannada, DBMS, Math, DMS, DS, COA, DS Lab, OOPS, AEC, Total, \n"
	f.write(row1)
	for i in range(len(df)):
		browser = webdriver.Chrome(executable_path=B_URL)
		browser.get(T_URL)
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
		name = browser.find_element_by_tag_name("h3")
		td = browser.find_elements_by_tag_name("td")
		if name.text == "Notice Board":
			print(f"{name.text} {usn} is not success")
		else:
			write = f'{usn}, {name.text}, {d}/{m}/{y}, {td[4].text[7:]}\n'
			name_usn = f'{usn}, {name.text}, '
			f.write(name_usn)
			print(name_usn, end=" ")
			browser.get(
				"https://parents.msrit.edu/index.php?option=com_studentdashboard&controller=studentdashboard&task=dashboard")
			browser.implicitly_wait(1)
			chart = browser.find_element_by_xpath(
				'//*[@id="page_bg"]/div[1]/div/div/div[4]/div[1]/div/script').get_attribute('innerHTML')
			marks = dict(eval(chart[chart.find("["):chart.rfind("]") + 1]))
			total = 0
			for key, val in marks.items():
				total += val
				write = f'{val},'
				print(f"{write}", end=" ")
				f.write(write)
			write = f'{total}\n'
			print(f"{write}")
			f.write(write)
			browser.close()
