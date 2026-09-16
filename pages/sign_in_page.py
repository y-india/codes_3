import streamlit as st
from config import LOGIN_BACKGROUND


st.set_page_config(
    page_title="JobSim",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed",
)


def apply_background(background):

    st.markdown(
        f"""
        <style>

        .stDeployButton {{
            display: none !important;
        }}

        #MainMenu {{
            visibility: hidden !important;
        }}

        header {{
            visibility: hidden !important;
            height: 0 !important;
        }}

        footer {{
            visibility: hidden !important;
        }}

        .stApp {{
            background:
                linear-gradient(
                    rgba(0, 0, 0, 0.52),
                    rgba(0, 0, 0, 0.52)
                ),
                url("{background}");

            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        .main .block-container {{
            max-width: 850px;
            padding-top: 20px !important;
            padding-bottom: 50px;
        }}

        label {{
            font-weight: 600 !important;
        }}

        .stButton > button {{
            width: 100%;
            min-height: 48px;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
        }}

        .section-heading {{
            color: white;
            font-size: 22px;
            font-weight: 700;
            margin-top: 22px;
            margin-bottom: 14px;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )


apply_background(LOGIN_BACKGROUND)


# ============================================================
# BASIC INFORMATION
# ============================================================

st.markdown(
    '<div class="section-heading">Basic Information</div>',
    unsafe_allow_html=True,
)

full_name = st.text_input(
    "Full name",
    placeholder="Enter your full name",
)

email = st.text_input(
    "Email",
    placeholder="Enter your email address",
)

phone = st.text_input(
    "Phone number (optional)",
    placeholder="Enter your phone number",
)

password = st.text_input(
    "Password",
    placeholder="Create a password",
    type="password",
)


# ============================================================
# CAREER INFORMATION
# ============================================================

st.markdown(
    '<div class="section-heading">Career Information</div>',
    unsafe_allow_html=True,
)

target_role = st.selectbox(
    "Target role",
    ["Data Analyst"],
)

current_status = st.selectbox(
    "Current status",
    [
        "Student",
        "Fresher",
        "Working Professional",
        "Job Seeker",
    ],
)

experience = st.selectbox(
    "Experience",
    [
        "0 years",
        "1+ years",
    ],
)


# ============================================================
# SKILLS
# ============================================================

st.markdown(
    '<div class="section-heading">Skills</div>',
    unsafe_allow_html=True,
)

skills = st.multiselect(
    "Skills",
    [
        "Excel",
        "SQL",
        "Python",
        "Power BI",
        "Tableau",
        "Statistics",
    ],
)

other_skills = st.text_input(
    "Other skills",
    placeholder="Enter other skills",
)


# ============================================================
# RESUME
# ============================================================

st.markdown(
    '<div class="section-heading">Resume</div>',
    unsafe_allow_html=True,
)

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "doc", "docx"],
)


# ============================================================
# SUBMIT
# ============================================================

st.write("")

if st.button("Sign In", use_container_width=True):

    if not full_name.strip():
        st.error("Full name is required.")

    elif not email.strip():
        st.error("Email is required.")

    elif not password.strip():
        st.error("Password is required.")

    elif not skills and not other_skills.strip():
        st.error("Please select at least one skill.")

    elif resume is None:
        st.error("Please upload your resume.")

    else:

        progress = st.progress(0)
        status = st.empty()

        import time

        for i in range(100):
            time.sleep(0.1)
            progress.progress(i + 1)

            status.markdown(
                f"""
                <div style="
                    text-align:center;
                    color:white;
                    font-size:18px;
                    font-weight:600;
                    margin-top:15px;
                ">
                    Creating your profile... {i + 1}%
                </div>
                """,
                unsafe_allow_html=True,
            )

        progress.empty()
        status.empty()