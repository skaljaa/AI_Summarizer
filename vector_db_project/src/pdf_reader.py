import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extracts and returns text from a given PDF file.
    """
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
