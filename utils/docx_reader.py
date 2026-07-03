from docx import Document

def extract_docx_text(file):
    """
    Extract text from DOCX resume.
    """

    document = Document(file)

    text = ""

    for para in document.paragraphs:
        text += para.text + "\n"

    return text