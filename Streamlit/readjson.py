import pandas as pd

USN = '1MS21CI049'
dob = '2003-05-21'
i = 21
T_URL = ('https://upylba53h2.execute-api.us-east-1.amazonaws.com/sis?usn=' + USN + '&dob=' + dob)

data = pd.read_json(T_URL)


