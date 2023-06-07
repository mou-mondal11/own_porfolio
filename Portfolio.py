from pathlib import Path
import streamlit as st
from PIL import Image



current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "style"/"main.css"
resume_file = current_dir / "asset"/ "Resume.pdf"
Profile_pic = current_dir / "asset "/"Mou.png"

Page_Title = "Digital CV | Mou Mondal"
Page_Icon = ":wave:"
Name = "Mou Mondal"
Description = """
Passionate and dedicated student pursuing a degree in Business Analytics and Data Science. As a curious and detail-oriented data analyst, I am driven by the thrill of uncovering meaningful insights from complex datasets. I possess a strong foundation in statistical analysis, programming, and data visualization, allowing me to transform raw data into actionable information. With a genuine enthusiasm for leveraging data to drive informed business decisions, I am eager to contribute my skills and knowledge to tackle real-world challenges. Through continuous learning and a commitment to excellence, 
I strive to make a significant impact in the field of data analytics. 
"""
Address = "Kolkata, West Bengal"
Email = "moumondal4368@gmail.com"
Contact = "8777849010"
Social_media = {
    "📎"" LinkedIn" : "https://www.linkedin.com/in/mou-mondal-4368mm/",
    "📎 Credly": "https://www.credly.com/users/mou-mondal.72652d7c/badges",
    "📎 Github": "https://github.com/mou-mondal11"
}
Projects = {
    "🏆"" Country GDP" : "https://mou-mondal11-country-eda-country-ac6o88.streamlit.app/",
    "🏆 Virat Kohli Performance": "https://app.powerbi.com/groups/me/reports/dee825bc-07d4-4520-b6df-c284ad33cac0/ReportSection?experience=power-bi",
    "🏆 Netflix Dashboard" : "https://app.powerbi.com/groups/me/reports/e6d93abc-f5da-47db-99f4-94993e8ad388/ReportSection?experience=power-bi",
    "🏆 Customer Details" : "https://app.powerbi.com/groups/me/reports/9ca39536-8972-4e66-8c29-5a939a0b76cc/ReportSection?experience=power-bi",
    "🏆 Own Portfolio Creation":" "
}

st.set_page_config(page_title = Page_Title, page_icon= Page_Icon)

#st.title("Hello there!")
with open(css_file)as f:
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://64.media.tumblr.com/20651df5ab8d49410d45b6722119edc8/tumblr_ot4npmTtUD1uzwgsuo1_400.gif');
            background-size: cover
           ;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profilepic = Image.open(Profile_pic)


#selected = option_menu(
#    menu_title = None,
#    options = ["Home","Education", "Skills", "Certifications", "Projects"],
#   icons= ["🏠","🎓","📚","⛳","🧮"],
#   menu_icon="cast",
 #   default_index=0,
  #  orientation="horizontal",
   # )



# Display content based on selected page
#if selected == "Home":
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profilepic, width=180)
    st.write("🏠", Address)
    st.write("📞", Contact)
    st.write("💬", Email)
    for Social, link in Social_media.items():
        st.write(f"[{Social}]({link})")
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
with col2:
    st.title(Name)
    st.write(Description)





#elif selected == "Education":
st.write("#")
st.subheader("🎓 Education & Qualification")
st.write("---")
st.write("""
    ✔ MBA in Business Analytics and Data Science
    - [Bengal Institute of Business Studies](https://www.bibs.co.in/), Kolkata, India
    - Expected Graduation: June, 2024

    ✔ BBA (Bachelor of Business Administration)
    - [Techno India University](https://www.technoindiauniversity.ac.in/), Kolkata, India
    - Year of Graduation: 2022

    ✔ High School
    - [Adi MahaKali Pathsala](https://school.banglarshiksha.gov.in/ws/website/head_master_desk/19170103116), Kolkata, West Bengal, India
    - Year of Passing : 2019
    """)

#elif selected == "Skills":
st.write("#")
st.subheader("Skills")
st.write("---")
st.write(
        """
        - Data Visualization: PowerBI, Ms Excel, Tableau, Plotly
        - Programming: Python, SQL, R
        - Modeling: Regression, Classification, Clustering
        - Databases: MySQL, Postgres
        """
    )
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSJwayTRv6RoFaiT-cRcq0RCn1dPbO42G8_g&usqp=CAU", width=200)

with col2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4byOiO5Tjt__ziU_7TcHawh1P3CPNOy0V47xXNVPOUfHQUtiNgF76sr5lXPMgwFgvfF0&usqp=CAU", width=200)

with col3:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzwiiEbbQoLpTXdTJHU_Bi_JVR_bg3D-hy8LgTvR7gJDbgrSS_TNzXtj7KlXSKJrLKkw8&usqp=CAU", width=200)
col4, col5, col6 = st.columns(3)

with col4:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRN1Luq_4m5dYUIdX71-iYSUrULhGEH6xFHjQ&usqp=CAU", width=200)

with col5:
    st.image("data:image/jpeg;base64,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", width=200)

with col6:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfsuYjkedxKniZ7mjNHEEfpTU1YG_iFSuG8g&usqp=CAU", width=200)
col7, col8, col9 = st.columns(3)

with col7:
    st.image("https://www.udacity.com/blog/wp-content/uploads/2020/12/Python-Tutorial_Blog-scaled.jpeg", width=200)

with col8:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIZFh8mOsWtU7feZnyHlajg-jPUJu15ICQ2YNHFbhp4bO5wXW3UzqEDQNQXxueqItDT4A&usqp=CAU", width =200)
with col9:
    st.image("data:image/jpeg;base64,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", width=200)

#elif selected == "Certifications":
st.write("#")
st.subheader("Certifications")
st.write("---")
st.write(
        """
        - Microsoft Office Specialist: Excel
        - Advance Excel with Power BI (IITK)
        - Machine Learning with Python (IITK)
        - R Essentials(IBM)
        - Build Your Own Chatbot - Level 1(IBM)
        - Complete SQL and Databases Bootcamp: Zero to Mastery[2023] (Udemy)
        - Python for Data Science (IBM)
        - Data Visualization with Python (IBM)
        - Power BI Virtual Case Experience (Forage)
        - Data Visualisation: Empowering Business with Effective Insights (Forage)
        """
    )

    # Define the Google Drive link
google_drive_link = "https://drive.google.com/drive/folders/1kV3ZZSNm-q9GNfr_vtGI-aUBYOIy0RNL"

    # Add a "View More" button
if st.button("View More"):
        # Link the button to the Google Drive link
    st.markdown(f"[Click here to view more certifications]({google_drive_link})")


#elif selected == "Projects":
st.write("#")
st.subheader("Projects")
st.write("---")
for project, link in Projects.items():
    st.write(f"[{project}]({link})")
