import streamlit as st


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="JobSim",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ============================================================
# BACKGROUND VARIABLES
# ============================================================

LOGIN_BACKGROUND = (
    "https://images.unsplash.com/photo-1497366754035-f200968a6e72"
    "?auto=format&fit=crop&w=2000&q=80"
)

# You can replace this with a local image:
# LOGIN_BACKGROUND = "assets/login.jpg"


# ============================================================
# JOBSIM TITLE SETTINGS
# Change these values easily
# ============================================================

TITLE_TEXT = "JobSim"

TITLE_COLOR = "#07121F"          # Text color
TITLE_BORDER = 2                 # Border thickness
TITLE_BORDER_COLOR = "#FFFFFF"   # Border color
TITLE_SIZE = 80                  # Text size


# ============================================================
# BACKGROUND + GLOBAL STYLE
# ============================================================

def apply_background(background):

    st.markdown(
        f"""
        <style>

        /* Hide Streamlit controls */
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

        /* Background */
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

        /* Main width */
        .main .block-container {{
            max-width: 850px;
            padding-top: 45px;
            padding-bottom: 50px;
        }}

        /* Inputs */
        label {{
            font-weight: 600 !important;
        }}

        /* Buttons */
        .stButton > button {{
            width: 100%;
            min-height: 48px;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
        }}

        /* White text */
        .white-text {{
            color: white !important;
            text-align: center;
        }}

        /* JobSim title */
        .jobsim-title {{
            text-align: center;
            margin: 10px 0 35px 0;
        }}

        .jobsim-title-text {{
            font-family:
                Impact,
                Haettenschweiler,
                "Arial Narrow Bold",
                sans-serif;

            font-size: {TITLE_SIZE}px;
            font-weight: 900;
            line-height: 0.95;
            letter-spacing: -4px;

            color: {TITLE_COLOR};
            -webkit-text-fill-color: {TITLE_COLOR};

            -webkit-text-stroke:
                {TITLE_BORDER}px
                {TITLE_BORDER_COLOR};

            margin: 0;
            padding: 0;
        }}

        /* Mobile */
        @media (max-width: 768px) {{
            .jobsim-title-text {{
                font-size: 55px;
                letter-spacing: -3px;
                -webkit-text-stroke:
                    1px
                    {TITLE_BORDER_COLOR};
            }}
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# JOBSIM TITLE
# ============================================================

def show_title():

    st.markdown(
        f"""
        <div class="jobsim-title">
            <div class="jobsim-title-text">
                {TITLE_TEXT}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# LOGIN PAGE
# ============================================================

def login_page():

    apply_background(LOGIN_BACKGROUND)

    # Center the login content
    left, center, right = st.columns([1, 2, 1])

    with center:

        # JobSim title
        show_title()

        # Subtitle
        st.markdown(
            """
            <div class="white-text" style="
                font-size: 16px;
                margin-bottom: 25px;
            ">
                Sign in to continue to your career profile
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Email
        st.text_input(
            "Email",
            placeholder="Enter your email",
            key="login_email",
        )

        # Password
        st.text_input(
            "Password",
            placeholder="Enter your password",
            type="password",
            key="login_password",
        )

        st.write("")

        # Login intentionally does nothing
        st.button(
            "Login",
            use_container_width=True,
            key="login_button",
        )

        st.write("")

        # Sign in text
        st.markdown(
            """
            <div class="white-text" style="
                font-size: 15px;
                margin-bottom: 10px;
            ">
                Don't have an account?
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Go to separate sign-in page
        if st.button(
            "Sign In",
            use_container_width=True,
            key="signin_button",
        ):
            st.switch_page("pages\\sign_in_page.py")


# ============================================================
# RUN APP
# ============================================================

login_page()