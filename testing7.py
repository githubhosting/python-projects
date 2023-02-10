import re
import config

from robobrowser import RoboBrowser

br = RoboBrowser()
br.open("https://adminpannel.vercel.app/#/login")
form = br.get_form()
form['username'] = "admin@foodey.com"
form['password'] = "adminfoodey"
br.submit_form(form)

src = str(br.parsed())
start = '<div class="MuiTypography-root MuiTypography-h5 css-zq6grw">'
end = '</div>'
result = re.search('%s(.*)%s' % (start, end), src).group(1)

