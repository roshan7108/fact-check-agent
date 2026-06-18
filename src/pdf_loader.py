from pypdf import PdfReader


def load_pdf(pdf_path, max_chars=12000):

    reader = PdfReader(pdf_path)

    full_text = ""

    for page in reader.pages:

        text = page.extract_text()

        if text:

            full_text += text + "\n"

    return full_text[:max_chars]