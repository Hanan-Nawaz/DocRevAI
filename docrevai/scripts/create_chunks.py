import logging
from docrevai.logging.logger import create_logger

class CreateChunks:
    """
        Divide text in small chunks
    """
    def __init__(self):
        log_format = "%(asctime)s - %(created)f - %(filename)s - %(funcName)s - %(message)s"
        self.logger = create_logger(__name__, logging.ERROR, "read_docs.log", log_format)

    def create_chunks(self, clean_text: str, chunk_size: int = 250, overlap_size: int = 50) -> list:
        """Divide the cleaned text into small chunks

        Parameters
        ----------
        clean_text : str
            The clean and normalized text
        chunk_size : int, optional
            The size of chunk, by default 250
        overlap_size : int, optional
            The size of overlap, by default 50

        Returns
        -------
        list
            The list of small chunks
        """
        try:
            words = clean_text.split()
            chunks = []

            step = chunk_size - overlap_size

            for i in range (0, len(words), step):
                chunk = " ".join(words[i:i + chunk_size])
                chunks.append(chunk)

            return chunks
        except Exception:
            self.logger.exception("Error while creating chunks")
            return ""