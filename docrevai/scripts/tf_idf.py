from sklearn.feature_extraction.text import TfidfVectorizer
import logging
from docrevai.logging.logger import create_logger

class TFIDF:
    """
        Create Tf-Idf Vectorizer
    """
    def __init__(self):
        log_format = "%(asctime)s - %(created)f - %(filename)s - %(funcName)s - %(message)s"
        self.logger = create_logger(__name__, logging.ERROR, "read_docs.log", log_format)

    def create_tfidf(self) -> TfidfVectorizer:
        """Create Tf-Idf Vectorizer

        Returns
        -------
        TfidfVectorizer
            Returns the vectorizer
        """
        try: 
            vectorizer = TfidfVectorizer(
                stop_words="english",
                lowercase=True,
                max_features=2000,
                ngram_range=(1, 2)
            )

            return vectorizer
        
        except Exception:
            self.logger.exception("Error in Tf-Idf vectorizer")