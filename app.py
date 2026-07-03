import streamlit as st
from utils.ats_score import calculate_ats_score
from utils.pdf_reader import extract_pdf_text
from utils.docx_reader import extract_docx_text
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

st.write(
    """
    Welcome!

    This application helps job seekers analyze their resume,
    compare it with a Job Description,
    calculate ATS score,
    and get AI-based suggestions.
    """
)

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
# Display File Details
# -------------------------------
if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    st.subheader("Uploaded File Details")

    st.write("**File Name:**", uploaded_file.name)
    st.write("**File Type:**", uploaded_file.type)
    st.write("**File Size:**", round(uploaded_file.size / 1024, 2), "KB")
 # Extract Resume Text

if uploaded_file is not None:

    if uploaded_file.name.endswith(".pdf"):
        resume_text = extract_pdf_text(uploaded_file)

    elif uploaded_file.name.endswith(".docx"):
        resume_text = extract_docx_text(uploaded_file)

    st.subheader("📄 Resume Preview")

    st.text_area(
        "Extracted Resume Text",
        resume_text,
        height=350
    )

    ats_score = calculate_ats_score(resume_text)

    st.subheader("📊 ATS Compatibility Score")

    st.progress(ats_score / 100)

    st.success(f"ATS Score: {ats_score}/100")