import streamlit as st
import pandas as pd

tr_props = [
	("display", "none"),
]
td_props = [
	('text-align', 'center'),
]
styles_table = [
	dict(selector="td:nth-child(3)", props=td_props),
	dict(selector="td:nth-child(4)", props=td_props),
	dict(selector="td:nth-child(5)", props=td_props),
	dict(selector="thead tr th:first-child", props=tr_props),
	dict(selector="tbody tr th:first-child", props=tr_props),
]

st.set_page_config(page_title="Grade Calculator Sanju", page_icon="📊", layout="centered")


def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("styles.css")

grade_ranges = {'Business Management HL': [12, 13, 27, 37, 49, 57, 70], 'Economics HL': [14, 15, 29, 39, 51, 64, 74],
                'Mathematics AA HL': [14, 15, 38, 52, 62, 71, 82], 'Spanish ad initio SL': [13, 14, 29, 43, 58, 71, 84],
                'Computer Science SL': [14, 15, 30, 41, 51, 60, 71], 'English L & L SL': [11, 12, 25, 39, 53, 65, 80]}

st.title("Grade Calculator")
st.subheader("Select your Subjects")
sub = st.multiselect("Multi Select subjects", grade_ranges.keys())
each_sub_max_score = []
each_sub_your_score = []

st.subheader("Enter your score for each subjects")
for i in range(len(sub)):
	each_sub_max_score.append(st.slider(f"{sub[i]} Max Score", 0, 100, step=1))
	if each_sub_max_score[i]:
		each_sub_your_score.append(st.slider(f"{sub[i]} Your Score", 0, each_sub_max_score[i], step=1))
percentage = []
for i in range(len(each_sub_your_score)):
	percent = each_sub_your_score[i] / each_sub_max_score[i] * 100
	percent = round(percent, 2)
	percentage.append(percent)

grades_scored = []
for i in range(len(percentage)):
	st.write(f"{sub[i]}: {percentage[i]}%")
	if percentage[i] <= grade_ranges[sub[i]][0]:
		grades_scored.append(1)
	elif grade_ranges[sub[i]][0] < percentage[i] < grade_ranges[sub[i]][2]:
		grades_scored.append(2)
	elif grade_ranges[sub[i]][2] <= percentage[i] < grade_ranges[sub[i]][3]:
		grades_scored.append(3)
	elif grade_ranges[sub[i]][3] <= percentage[i] < grade_ranges[sub[i]][4]:
		grades_scored.append(4)
	elif grade_ranges[sub[i]][4] <= percentage[i] < grade_ranges[sub[i]][5]:
		grades_scored.append(5)
	elif grade_ranges[sub[i]][5] <= percentage[i] < grade_ranges[sub[i]][6]:
		grades_scored.append(6)
	elif grade_ranges[sub[i]][6] <= percentage[i]:
		grades_scored.append(7)
	else:
		grades_scored.append(0)
st.subheader("Your Grades")
if len(grades_scored) == len(sub):
	table = pd.DataFrame({'SubjectS': sub, 'Percentage': [f"{p:.2f} %" for p in percentage], 'Grade': grades_scored})
	st.markdown(table.style.set_table_styles(styles_table).to_html(), unsafe_allow_html=True)
	st.write("<hr/>", unsafe_allow_html=True)
	st.write(f"Your Total Grade Points: {sum(grades_scored)}")
