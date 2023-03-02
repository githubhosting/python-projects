import streamlit as st
import pandas as pd
from datetime import datetime

time_frame = []
with open('logs.txt', 'r') as f:
	for _ in range(5): st.write("\n")
	st.subheader("Logs")
	# st.text(f.read())
	line = f.readline()
	for line in f:
		if "|" in line:
			line = line.split("|")
			time_line = line[1]
			time_line = datetime.strptime(time_line, '%Y-%m-%d %H:%M:%S')
			time_frame.append(time_line)
	df = pd.DataFrame(time_frame)
	st.write(df)
