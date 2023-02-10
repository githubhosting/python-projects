from selenium import webdriver
import pandas as pd

uploaded_file = '#alldob.xlsx'
uploaded_file2 = 'allname.xlsx'
df = pd.read_excel(uploaded_file)
df2 = pd.read_excel(uploaded_file2)
usn_list = []
usn_newlist = []

for i in range(0, 57):
    usn = df['USN'][i]
    usn_list.append(usn)
print(usn_list)

for i in range(1, 71):
    usn = f"1MS21CI{i:03}"
    if usn not in usn_list:
        usn_newlist.append(usn)
print(usn_newlist)

