from  pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Santiago Carreño"
PAGE_ICON = "❣️"
NAME = "Santiago Carreño | Software Developer"
DESCRIPTION = """
I am a qualified and professional web developer with four
years of experience in database administration and
website design. Strong creative and analytical skills.
My main objective is to provide my best knowledge and to
be able to learn, know and understand everything that is
available to me to do
My main objective is to contribute my best knowledge and be 
able to learn, know ad understand everything is at my 
disposal to do
"""
EMAIL = "santiagoestebancmc@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://co.linkedin.com/in/santiago-esteban-carre%C3%B1o-mancera-05441027a",
    "GitHub": "https://github.com/santicarreno13",
    "twitter": "https://twitter.com/forwardpaladih8"
}

PROJECTS = {
    "🏆 API of the Rick and Morty in vue": "https://github.com/santicarreno13/Vue_Proyect_Practice",
    "🏆 Projetc in Java Spring Boot": "https://github.com/santicarreno13/Donneta",
    "🏆 Boot of whatsApp in JavaScript": "https://github.com/santicarreno13/BotWhatsApp",
    "🏆 Back Door in Python with sockets": "https://github.com/santicarreno13/BackDoors",
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label= "📃 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📩", EMAIL)

# --- SOCIAL SECTION ---

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERINCE & QULIFICATIONS ---

st.write("#")
st.subheader("Experience & Qulifications")
st.write(
    """
    - ✔  1 year in Spring Boot in Java
    - ✔  6 months in Laravel with vue and NodeJs
    - ✔  4 years studying the basics of programming
    - ✔  2 years studying MySQL adn GIT
"""    
)

# --- SKILLS ---

st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - 👨‍💻  Programming: Java(Spring Boot), PHP(Laravel), SQL, Python, Perl.
    - 👨‍💻  Programming: Vue, JavaScript, NodeJs, CSS, SASS, GIT.
    - 📊  DataBases: MySQL.
    - 📊  Social Comunication: Technical Support.
"""
)

# --- WORK HISTORY ---

st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1 ---

st.write("💻" , "** Developer web | Accedo S.A.S")
st.write("12/2022 - 06/2023")
st.write(
    """
    - ⇒   The development of logic models to facilitate optimal management of the application
    - ⇒   Development of components for correct operation
"""
)
st.write("#")
st.write("🗣️" , "** Technical Support | Serdempo")
st.write("08/2023 - 11/2023")
st.write(
    """
    - ⇒   Technical support
    - ⇒   Creatin and solving technical problems
"""
)


# --- STUDY HISTORY ---

st.write("#")
st.subheader("Study History")
st.write("---")

# --- 1 ---

st.write("📖" , "** Academic Bachelor | Alberto Lleras Camargo **")
st.write("02/2016 - 12/2021")

# --- 2 ---

st.write("💻" , "** Technician in analysis and desing of information system | SENA **")
st.write("03/2020 - 12/2021")

# --- 3 ---

st.write("💻" , "** Technologist in analysis and desing of information system | SENA **")
st.write("02/2022 - 06/2023")

# --- 4 ---

st.write("💻" , "** Systems Enginner | Politecnico Gran Colombiano **")
st.write("06/2023 - Present")
st.write(" 6 semester ")

# --- PROYECTS & ACCOMPLISHMENTS ---

st.write("#")
st.subheader("Projets & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


