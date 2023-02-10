# automate login to a website
username = "admin@foodey.com"
password = "adminfoodey"

import requests
import re
from bs4 import BeautifulSoup
from robobrowser import RoboBrowser

br = RoboBrowser()
br.open("https://adminpannel.vercel.app/#/login")
form = br.get_form()
form['username'] = username
form['password'] = password
br.submit_form(form)

src = str(br.parsed())
start = '<div class="MuiTypography-root MuiTypography-h5 css-zq6grw">'
end = '</div>'
result = re.search('%s(.*)%s' % (start, end), src).group(1)
print(result)
