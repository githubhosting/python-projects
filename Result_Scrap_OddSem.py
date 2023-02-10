from selenium import webdriver
import time

DEPT = "IS"
B_URL = "./chromedriver.exe"
driver = webdriver.Chrome(executable_path=B_URL)
driver.get("http://exam.msrit.edu/index.php")

cap = input("Enter the captcha \n")

with open(f'#{DEPT}odd.csv', 'w+') as f:
    for i in range(1, 170):
        element = driver.find_element_by_id("usn")
        element.send_keys(f"1MS20{DEPT}{i:03}")
        element2 = driver.find_element_by_id("osolCatchaTxt0")
        element2.send_keys(cap)

        driver.find_element_by_class_name("buttongo").click()

        try:
            name = driver.find_element_by_tag_name("h3")
            cgpa = driver.find_elements_by_tag_name("p")

            data = f'1MS20{DEPT}{i:03}, {name.text}, {cgpa[4].text}\n'
            print_data = f'{i} 1MS20{DEPT}{i:03} {name.text} {cgpa[4].text}'
            f.write(data)
            print(print_data)
        except Exception as e:
            print(e)
        driver.back()
# capt = driver.find_element_by_id("osolCatchaTxt0")
#
# capt_click = driver.find_element_by_class_name("buttongo")
# element = driver.find_element_by_id("usn")
# for i in range(1, 170):
#     element.clear()
#     element.send_keys(f"1MS21{DEPT}{i:03}")
#     capt.send_keys(cap)
#     # element2 = driver.find_element_by_id("osolCatchaTxt0")
#     # element2.send_keys(cap)
#     capt_click.click()
#
#     try:
#         name = driver.find_element_by_tag_name("h3")
#         cgpa = driver.find_elements_by_tag_name("p")
#
#         data = f'1MS21{DEPT}{i:03}, {name.text}, {cgpa[4].text}\n'
#         f.write(data)
#         print(data)
#         # print(f'{name.text} - {cgpa[4].text}')
#     except Exception as e:
#         print(e)
#     driver.back()
