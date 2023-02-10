import mechanize
from bs4 import BeautifulSoup
from urllib.request import urlopen

import http.cookiejar as cookielib

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://adminpannel.vercel.app")

br.select_form(nr=0)
br.form['username'] = 'admin@foodey.com'
br.form['password'] = 'adminfoodey'
br.submit()

print(br.response().read())
