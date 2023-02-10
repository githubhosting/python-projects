import streamlit as st

st.title("CGPA Calculator")
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


