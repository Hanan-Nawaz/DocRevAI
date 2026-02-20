from pypdf import PdfReader

def read_pdf(path: str) -> str:
    """
    Read a PDF file and return all extracted text.

    Parameters
    ----------
    path : str
        Path to the PDF file.

    Returns
    -------
    str
        Raw extracted text from the PDF.
        Returns an empty string if reading fails.
    """

    try:
        pdf_reader = PdfReader(path)
        return "".join(page.extract_text() or "" for page in pdf_reader.pages)

    except Exception as error:
        print(f"Error while reading file {path}. Error: {error}")
        return ""