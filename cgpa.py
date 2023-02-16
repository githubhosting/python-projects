import streamlit as st
import pandas as pd

subjects = ["Maths", "DBMS", "DS", "COA", "DMS", "UHV", "Kannada", "AEC", "OOPS Lab", "DS Lab"]
credits_each = [3, 3, 3, 3, 3, 2, 1, 1, 1, 1]

st.title("CGPA Calculator")
tab1, tab2, tab3, tab4 = st.tabs(["To Score", "Each Subject", "Credit-CGPA", "Estimator"])

with tab2:
    st.subheader("Enter your Average CIE Marks for each subjects")
    choice = st.radio("Select your input method", ("Slider", "Value input"))
    marks = []

    for i in range(len(subjects)):
        if choice == "Value input":
            marks.append(st.number_input(subjects[i], 0, 50, step=1))
        else:
            marks.append(st.slider(subjects[i], 0, 50, step=1))
    to_scoreO = []
    to_score_Aplus = []
    to_score_A = []
    to_score_Bplus = []
    to_score_B = []

    for i in range(len(marks)):
        to_scoreO.append((90 - marks[i]) * 2)
        to_score_Aplus.append((90 - marks[i]) * 2 - 20)
        to_score_A.append((90 - marks[i]) * 2 - 40)
        to_score_Bplus.append((90 - marks[i]) * 2 - 60)
        to_score_B.append((90 - marks[i]) * 2 - 80)
    table = pd.DataFrame(
        {"Subject": subjects, "Avg Marks CIE": marks, "O": to_scoreO, "A+": to_score_Aplus, "A": to_score_A,
         "B+": to_score_Bplus, "B": to_score_B})
    table_side = pd.DataFrame(
        {"Subject": subjects, "O": to_scoreO, "A+": to_score_Aplus, "A": to_score_A,
         "B+": to_score_Bplus, "B": to_score_B})
    st.write("You have to score the following marks in SEE to get the respective grade")
    st.table(table)
with tab4:
    st.subheader("Enter your Predicted Grade for each subjects")
    show = st.checkbox("Show Table")
    if show:
        with st.sidebar:
            st.write("You have to score the following marks in SEE to get the respective grade")
            st.table(table_side)

    grade_in_each = []
    for i in range(len(subjects)):
        grade_in_each.append(st.selectbox(subjects[i], ["O", "A+", "A", "B+", "B", "C"]))
    credits_in_each = [
        10 if i == "O" else 9 if i == "A+" else 8 if i == "A" else 7 if i == "B+" else 6 if i == "B" else 5
        for i in
        grade_in_each]
    total_credits = sum(credits_in_each)
    total_credits_each = [i * j for i, j in zip(credits_in_each, credits_each)]
    total_credits_final = sum(total_credits_each)
    cgpa = total_credits_final / 21
    table = pd.DataFrame(
        {"Subject": subjects, "Grade": grade_in_each, "Credits": credits_in_each, "Total Credits": total_credits_each})
    st.table(table)
    cgpa = round(cgpa, 3)
    st.subheader(f"Your CGPA is:\t " f"{cgpa}")
with tab1:
    st.subheader("How much is average CIE marks?")
    avg = st.slider("Average CIE marks", 0, 50, step=1)
    to_score = (90 - avg) * 2
    st.subheader("You should score")
    grades = [to_score, to_score - 20, to_score - 40, to_score - 60, to_score - 80, to_score - 100]
    grade_letter = ["O", "A+", "A", "B+", "B", "C"]
    table_1 = pd.DataFrame({"Grade": grade_letter, "Marks": grades})
    st.table(table_1)

with tab3:
    choice = st.radio("Select your course", ("Slider", "Value input"))
    if choice == "Value input":
        cgpa = st.number_input("Select your CGPA", 0.0, 10.0, step=0.1)
    else:
        cgpa = st.slider("Select your CGPA", 0.0, 10.0, step=0.1)

    credits = 21 * cgpa
    st.subheader(f"Your Should get {credits} credits")

    if choice == "Value input":
        credits = st.number_input("Enter your credits", 0, 210, step=1)
    else:
        credits = st.slider("Enter your credits", 0, 210, step=1)
    cgpa = credits / 21
    st.subheader(f"Your CGPA will be {cgpa}")
