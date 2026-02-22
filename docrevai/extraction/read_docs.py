from pypdf import PdfReader
from docrevai.logging.logger import create_logger
import logging

class ReadDocs:
    """
        Read a file and return all extracted text.

        Note
        ----
        Currently, only for PDF's.
    """
    def __init__(self):
        log_format = "%(asctime)s - %(created)f - %(filename)s - %(funcName)s - %(message)s"
        self.logger = create_logger(__name__, logging.ERROR, "read_docs.log", log_format)

    def read_pdf(self, path: str) -> str:
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
            self.logger.exception(f"Error while reading file {path}. Error: {error}")
            return ""