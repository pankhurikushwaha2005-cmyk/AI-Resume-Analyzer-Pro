import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer Pro",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer Pro")
st.subheader("Developed by Pankhuri Kushwaha")

st.write("""
Welcome to AI Resume Analyzer Pro!

This application will:
- Analyze PDF and DOCX resumes
- Calculate ATS compatibility score
- Compare resumes with job descriptions
- Detect missing skills
- Suggest improvements using AI
""")

st.success("Project setup completed successfully! 🎉")