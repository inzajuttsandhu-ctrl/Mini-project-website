import streamlit as st
import datetime

st.set_page_config(
    page_title="Student Mini App",
    page_icon="🎓"
)

st.title("🎓 Student Management Mini App")

st.subheader("Student Information")

name = st.text_input("Enter student name")
age = st.number_input("Enter age", 1, 100)
course = st.selectbox(
    "Select course",
    ["Python", "Web Development", "Data Science", "AI"]
)

join_date = st.date_input(
    "Joining Date",
    datetime.date.today()
)

if st.button("Save Student"):
    st.success("Student Saved ✅")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Course:", course)
    st.write("Joining Date:", join_date)
