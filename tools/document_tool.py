from io import BytesIO

from pypdf import PdfReader
from docx import Document


def extract_document(uploaded_file):

    file_name = uploaded_file.name.lower()

    file_bytes = uploaded_file.getvalue()

    if file_name.endswith(".pdf"):

        reader = PdfReader(
            BytesIO(file_bytes)
        )

        pages = []

        for page in reader.pages:

            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n\n".join(pages).strip()

    if file_name.endswith(".docx"):

        document = Document(
            BytesIO(file_bytes)
        )

        paragraphs = []

        for paragraph in document.paragraphs:

            text = paragraph.text.strip()

            if text:
                paragraphs.append(text)

        return "\n\n".join(paragraphs).strip()

    if file_name.endswith(".txt"):

        return file_bytes.decode(
            "utf-8",
            errors="ignore"
        ).strip()

    raise ValueError(
        "Unsupported file type. Please upload PDF, DOCX or TXT."
    )
