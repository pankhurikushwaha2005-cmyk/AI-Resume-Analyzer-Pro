import PyPDF2

def extract_pdf_text(file):
    """
    Extract text from PDF resume.
    """

    reader = PyPDF2.PdfReader(file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text