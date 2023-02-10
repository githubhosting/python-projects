import mechanize
response = mechanize.urlopen("http://parents.msrit.edu/parents_even2022/")
print(response.read())