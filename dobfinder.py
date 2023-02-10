import pandas as pd
import numpy as np

USN = '1MS21CI049'
dob = '2003-05-'
for i in range(20, 32):

    link = ('https://upylba53h2.execute-api.us-east-1.amazonaws.com/sis?usn=' + USN + '&dob=' + dob + str(i))
    # print(link)
    data = pd.read_json(link)
    if data.empty:
        pass
    else:
        print(dob+ str(i))
        break

