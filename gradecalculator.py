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

# grade_ranges = {'Business Management HL': [12, 13, 27, 37, 49, 57, 70],
#                 'Economics HL': [14, 15, 29, 39, 51, 64, 74],
#                 'Mathematics AA HL': [14, 15, 38, 52, 62, 71, 82],
#                 'Spanish ad initio SL': [13, 14, 29, 43, 58, 71, 84],
#                 'Computer Science SL': [14, 15, 30, 41, 51, 60, 71],
#                 'English L & L SL': [11, 12, 25, 39, 53, 65, 80]}

grade_ranges_1 = {'English L & L HL': [13, 14, 28, 41, 54, 66, 80],
                  'English L & L SL': [11, 12, 25, 39, 53, 65, 80],
                  'Korean A Lit. HL': [13, 14, 28, 44, 58, 70, 85],
                  'Korean A Lit. SL': [13, 14, 28, 44, 58, 70, 85], }

grade_ranges_2 = {'English B HL': [15, 16, 30, 45, 59, 73, 87],
                  'English B SL': [15, 16, 30, 45, 59, 73, 87],
                  'French B SL': [14, 15, 28, 43, 58, 72, 85],
                  'French ab initio': [14, 15, 30, 43, 58, 69, 83],
                  'Hindi B HL': [17, 18, 36, 51, 62, 73, 85],
                  'Hindi B SL': [13, 14, 27, 43, 57, 71, 85],
                  'Mandarin ab initio': [13, 14, 24, 39, 56, 71, 83],
                  'Mandarin B SL': [13, 14, 24, 39, 56, 71, 83],
                  'Spanish B HL': [12, 13, 25, 40, 55, 70, 83],
                  'Spanish B SL': [12, 13, 25, 40, 55, 70, 83],
                  'Spanish ab initio': [13, 14, 29, 43, 58, 71, 84], }

grade_ranges_3 = {'Business Management HL': [12, 13, 27, 37, 49, 57, 70],
                  'Business Management SL': [11, 12, 23, 38, 49, 60, 70],
                  'Economics HL': [14, 15, 29, 39, 51, 64, 74],
                  'Economics SL': [13, 14, 28, 42, 53, 65, 75],
                  'Global Politics HL': [10, 11, 23, 34, 45, 59, 71],
                  'Global Politics SL': [10, 11, 24, 34, 46, 60, 72],
                  'Psychology HL': [9, 10, 22, 34, 46, 58, 71],
                  'Psychology SL': [9, 10, 23, 33, 46, 59, 71], }

grade_ranges_4 = {'Biology HL': [15, 16, 26, 37, 51, 64, 77],
                  'Biology SL': [13, 14, 25, 35, 48, 61, 74],
                  'Chemistry HL': [16, 17, 30, 43, 55, 66, 78],
                  'Chemistry SL': [15, 16, 29, 41, 53, 63, 75],
                  'Computer Science HL': [14, 15, 29, 40, 49, 60, 70],
                  'Computer Science SL': [14, 15, 30, 41, 51, 60, 71],
                  'Design Technology HL': [16, 17, 26, 36, 49, 60, 71],
                  'Design Technology SL': [16, 17, 29, 40, 50, 60, 70],
                  'Physics HL': [14, 15, 26, 38, 48, 59, 69],
                  'Physics SL': [12, 13, 22, 34, 44, 54, 64],
                  'ESS SL': [11, 12, 23, 35, 45, 56, 66], }

grade_ranges_5 = {'Mathematics (A&A) HL': [14, 15, 38, 52, 62, 71, 82],
                  'Mathematics (A&A) SL': [14, 15, 39, 53, 63, 72, 81],
                  'Mathematics (A&I) SL': [14, 15, 39, 53, 63, 72, 81], }

grade_ranges_6 = {'Music HL': [14, 15, 31, 47, 56, 68, 77],
                  'Music SL': [14, 15, 31, 48, 58, 70, 80],
                  'Theatre HL': [8, 9, 20, 31, 48, 65, 81],
                  'Theatre SL': [8, 9, 20, 31, 48, 65, 81],
                  'Visual Arts HL': [12, 13, 26, 41, 55, 70, 84],
                  'Visual Arts SL': [12, 13, 26, 41, 54, 71, 85], }
grade_ranges = {**grade_ranges_1, **grade_ranges_2, **grade_ranges_3, **grade_ranges_4, **grade_ranges_5,
                **grade_ranges_6}

st.title("Grade Calculator")
st.subheader("Select your Subjects according to groups")
subject = []
# subject = st.multiselect("Multi Select subjects", grade_ranges.keys())
subject.append(st.selectbox(f"Select Group 1 Subject", options=grade_ranges_1.keys()))
subject.append(st.selectbox(f"Select Group 2 Subject", options=grade_ranges_2.keys()))
subject.extend(st.multiselect("Select Group 3 Subjects", grade_ranges_3.keys()))
subject.extend(st.multiselect("Select Group 4 Subjects", grade_ranges_4.keys()))
subject.append(st.selectbox(f"Select Group 5 Subject", options=grade_ranges_5.keys()))
checkbox = st.checkbox("Select Group 6 Subject", value=False)
if checkbox:
	subject.append(st.selectbox(f"Select Group 6 Subject", options=grade_ranges_6.keys()))

st.write("You selected:", subject)
if len(subject) == 0:
	st.warning("Please select at least one subject")

each_sub_max_score = []
each_sub_your_score = []

st.subheader("Enter your score for each subjects")
choice = st.radio("Select the type of Entry", ["Text", "Slider"])


def foo(i):
	if len(st.session_state[f"marks{i}"]) == 2:
		st.session_state[f"marks{i}"] = f'{st.session_state[f"marks{i}"]}/'


if choice == "Text":
	for i in range(len(subject)):
		marks_scored = st.text_input(f"{subject[i]} Score", key=f"marks{i}", on_change=lambda _i=i: foo(_i))

		if marks_scored:
			marks_scored = marks_scored.split("/")
			each_sub_your_score.append(marks_scored[0])
			if marks_scored[1]:
				each_sub_max_score.append(marks_scored[1])

elif choice == "Slider":
	for i in range(len(subject)):
		each_sub_max_score.append(st.slider(f"{subject[i]} Max Score", 0, 100, step=1))
		if each_sub_max_score[i]:
			each_sub_your_score.append(st.slider(f"{subject[i]} Your Score", 0, each_sub_max_score[i], step=1))

percentage = []
for i in range(len(each_sub_your_score)):
	if len(each_sub_your_score) == len(each_sub_max_score):
		your_score = int(each_sub_your_score[i])
		max_score = int(each_sub_max_score[i])
		if your_score >= max_score:
			st.warning(f"Your score is greater than max score")
		elif your_score <= max_score:
			percent = your_score / max_score * 100
			percent = round(percent, 2)
			percentage.append(percent)

grades_scored = []
for i in range(len(percentage)):
	st.write(f"{subject[i]}: {percentage[i]}%")
	if percentage[i] <= grade_ranges[subject[i]][0]:
		grades_scored.append(1)
	elif grade_ranges[subject[i]][0] < percentage[i] < grade_ranges[subject[i]][2]:
		grades_scored.append(2)
	elif grade_ranges[subject[i]][2] <= percentage[i] < grade_ranges[subject[i]][3]:
		grades_scored.append(3)
	elif grade_ranges[subject[i]][3] <= percentage[i] < grade_ranges[subject[i]][4]:
		grades_scored.append(4)
	elif grade_ranges[subject[i]][4] <= percentage[i] < grade_ranges[subject[i]][5]:
		grades_scored.append(5)
	elif grade_ranges[subject[i]][5] <= percentage[i] < grade_ranges[subject[i]][6]:
		grades_scored.append(6)
	elif grade_ranges[subject[i]][6] <= percentage[i]:
		grades_scored.append(7)
	else:
		grades_scored.append(0)
st.subheader("Your Grades")
if len(grades_scored) == len(subject):
	table = pd.DataFrame(
		{'SubjectS': subject, 'Percentage': [f"{p:.2f} %" for p in percentage], 'Grade': grades_scored})
	st.markdown(table.style.set_table_styles(styles_table).to_html(), unsafe_allow_html=True)
	st.write("<hr/>", unsafe_allow_html=True)
	st.write(f"Your Total Grade Points: {sum(grades_scored)}")
