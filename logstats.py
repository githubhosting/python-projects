import streamlit as st
import pandas as pd
from datetime import datetime

time_frame = []
all_usns = []
tokens = []
with open('logs.log', 'r') as f:
	for _ in range(5): st.write("\n")
	line = f.readline()
	for line in f:
		if "|" in line:
			line = line.split("|")
			time_line = line[1]
			usn = line[2]
			token = line[5]
			tokens.append(token)
			all_usns.append(usn)
			time_line = time_line.strip()
			time_ = datetime.strptime(time_line, '%Y-%m-%d %H:%M:%S.%f')
			time_frame.append(time_)
	df = pd.DataFrame({"Time": time_frame}, index=range(1, len(time_frame) + 1))
	dept = []
	for usn in all_usns:
		dept.append(usn[6:8])
	unique_dept = list(set(dept))
	dept_count = []
	for i in unique_dept:
		dept_count.append(dept.count(i))
	dept_counts = pd.DataFrame({"Dept": unique_dept, "Count": dept_count})
	st.subheader("Time wise count")
	st.line_chart(df, use_container_width=True)
	st.subheader("Department wise count")
	st.write(dept_counts)
	st.subheader("Token wise count")
	st.write(pd.DataFrame({"Token": tokens}).value_counts())
