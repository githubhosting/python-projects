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
	dept_ = []
	unique_usn = list(set(all_usns))
	for usn in all_usns:
		dept.append(usn[4:8])
	for usn in unique_usn:
		dept_.append(usn[4:8])
	unique_dept = list(set(dept))
	dept_count = []
	dept_count_ = []
	for i in unique_dept:
		dept_count.append(dept.count(i))
	for j in unique_dept:
		dept_count_.append(dept_.count(j))

	dept_count, dept_count_, unique_dept = zip(*sorted(zip(dept_count, dept_count_, unique_dept), reverse=True))

	dept_counts = pd.DataFrame({"Dept": unique_dept, "Count Rep": dept_count, "Count Unique": dept_count_})
	st.subheader("Time wise count")
	st.line_chart(df, use_container_width=True)
	st.subheader("Department wise count")
	st.write(dept_counts)
	st.subheader("Token wise count")
	st.write(pd.DataFrame({"Token": tokens}).value_counts())
