import streamlit as st
import base64

# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Your Name Portfolio",
    page_icon="📊",
)

def home_page():
    # ----- Left menu -----
    with st.sidebar:
        st.image("eae_img.png", width=200)
        st.header("Introduction to Programming Languages for Data")
        st.write("###")
        st.write("***Final Project - Feb 2025***")
        st.write("**Author:** Sandeep Kotyada")  # TODO: Add your name
        st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")

    # ----- Top title -----
    st.markdown(
        """<div style="text-align: center;">
            <h1>👋 Hi! My name is Sandeep Kotyada</h1>
        </div>""",
        unsafe_allow_html=True,
    )  # TODO: Add your name

    # ----- Profile image file -----
    profile_image_file_path = "my_image.jpg"  # TODO: Upload your profile image

    try:
        with open(profile_image_file_path, "rb") as img_file:
            img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

        # ----- Your Profile Image -----
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <img src="{img}" alt="Your Name" width="300" height="300"
                style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
    except FileNotFoundError:
        st.warning("Profile image not found. Please upload 'profile.png'.")

    # ----- Personal title or short description -----
    current_role = "Data Engineer"  # TODO: Update this

    st.markdown(
        f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""",
        unsafe_allow_html=True,
    )

    st.write("##")  # Adding some space

    # ----- About me section -----
    st.subheader("About Me")

    st.write("""
    - 🧑‍💻 I am a Data Engineer with 5 years of experience in Big Data & Data Engineering.
    - 🛩️ prev: Worked at Imaginnovate, focusing on scalable data pipelines.
    - ❤️ Passionate about data-driven solutions.
    - 🤖 Built multiple data solutions, ETL Pipelines & analytics dashboards.
    - 🏂 Enjoy hiking, traveling, and exploring new tech.
    - 📫 How to reach me: kotyadasandeep11@gmail.com
    - 🏠 Based in Barcelona.
    """)

    # Feel free to add your LinkedIn, GitHub, or other social media links.

# Assemble the app with the navigation menu
pg = st.navigation([
    st.Page(home_page, title="Home", icon="👋"),
    st.Page("pages/01_image_cropper.py", title="Image Cropper", icon="🖼️"),
    st.Page("pages/02_netflix_data_analysis.py", title="Netflix Data Analysis", icon="🎬"),
    st.Page("pages/03_temperatures_dashboard.py", title="Temperatures Dashboard", icon="🌦️"),
])
pg.run()
