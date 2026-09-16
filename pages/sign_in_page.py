import streamlit as st

st.set_page_config(
    page_title="JobSim",
    layout="centered",
)

st.title("JobSim")

st.subheader("Basic Information")

full_name = st.text_input("Full name")
email = st.text_input("Email")
phone = st.text_input("Phone number (optional)")
password = st.text_input("Password", type="password")

st.subheader("Career Information")

target_role = st.selectbox(
    "Target role",
    ["Data Analyst"]
)

current_status = st.selectbox(
    "Current status",
    [
        "Student",
        "Fresher",
        "Working Professional",
        "Job Seeker"
    ]
)

experience = st.selectbox(
    "Experience",
    [
        "0 years",
        "1+ years"
    ]
)

st.subheader("Skills")

skills = st.multiselect(
    "Skills",
    [
        "Excel",
        "SQL",
        "Python",
        "Power BI",
        "Tableau",
        "Statistics"
    ]
)

other_skills = st.text_input("Other skills")

st.subheader("Resume")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "doc", "docx"]
)

st.write("")

if st.button("Sign In", use_container_width=True):

    progress = st.progress(0)

    import time

    for i in range(100):
        time.sleep(0.1)
        progress.progress(i + 1)

    st.success("Profile submitted.")