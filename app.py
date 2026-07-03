import streamlit as st

from utils.pdf_reader import extract_pdf_text
from utils.docx_reader import extract_docx_text
from utils.ats_score import calculate_ats_score
from utils.skill_extractor import extract_skills
from utils.jd_matcher import match_resume_with_jd
from utils.ai_helper import generate_suggestions

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Resume Analyzer Pro",
    page_icon="📄",
    layout="wide"
)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("AI Resume Analyzer")
st.sidebar.write("Navigate through the application.")

st.sidebar.info(
    """
    Version: 1.0

    Developed by:
    Pankhuri Kushwaha
    """
)

# -------------------------------
# Main Heading
# -------------------------------
st.title("📄 AI Resume Analyzer Pro")

st.write("""
Welcome!

This application helps job seekers analyze their resume,
compare it with a Job Description,
calculate ATS score,
and get AI-based suggestions.
""")

st.divider()

# -------------------------------
# Resume Upload
# -------------------------------
st.header("📤 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose your Resume",
    type=["pdf", "docx"]
)

# -------------------------------
# Main Resume Processing
# -------------------------------
if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    st.subheader("Uploaded File Details")

    st.write("**File Name:**", uploaded_file.name)
    st.write("**File Type:**", uploaded_file.type)
    st.write("**File Size:**", round(uploaded_file.size / 1024, 2), "KB")

    # -------------------------------
    # Extract Resume Text
    # -------------------------------
    if uploaded_file.name.endswith(".pdf"):
        resume_text = extract_pdf_text(uploaded_file)

    elif uploaded_file.name.endswith(".docx"):
        resume_text = extract_docx_text(uploaded_file)

    else:
        resume_text = ""

    # -------------------------------
    # Resume Preview
    # -------------------------------
    st.subheader("📄 Resume Preview")

    st.text_area(
        "Extracted Resume Text",
        resume_text,
        height=350
    )

    # -------------------------------
    # ATS Score
    # -------------------------------
    ats_score = calculate_ats_score(resume_text)

    st.subheader("📊 ATS Compatibility Score")

    st.progress(ats_score / 100)

    st.success(f"ATS Score: {ats_score}/100")

    # -------------------------------
    # Skill Extraction
    # -------------------------------
    skills = extract_skills(resume_text)

    st.subheader("🛠 Extracted Skills")

    if skills:
        for skill in skills:
            st.markdown(f"✅ {skill}")
    else:
        st.warning("No skills detected.")

    # -------------------------------
    # Job Description
    # -------------------------------
    st.divider()

    st.subheader("📋 Job Description")

    job_description = st.text_area(
        "Paste the Job Description here",
        height=200
    )

    # -------------------------------
    # Resume Matching
    # -------------------------------
    if job_description:

        match_percentage, matching_skills, missing_skills = match_resume_with_jd(
            resume_text,
            job_description
        )

        st.subheader("🎯 Resume Match")

        st.progress(match_percentage / 100)

        st.success(f"Match Score: {match_percentage}%")

        st.subheader("✅ Matching Skills")

        if matching_skills:
            for skill in matching_skills:
                st.markdown(f"✅ {skill}")
        else:
            st.info("No matching skills found.")

        st.subheader("❌ Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.markdown(f"❌ {skill}")
        else:
            st.success("No missing skills. Great match!")

    # -------------------------------
    # AI Suggestions
    # -------------------------------
    st.divider()

    st.subheader("🤖 AI Resume Suggestions")

    suggestions = generate_suggestions(
        resume_text,
        skills,
        ats_score
    )

    for suggestion in suggestions:
        st.info("💡 " + suggestion)