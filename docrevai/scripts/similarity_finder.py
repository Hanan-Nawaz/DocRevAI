from sklearn.metrics.pairwise import cosine_similarity
import logging
from docrevai.logging.logger import create_logger
from docrevai.scripts.tf_idf import TFIDF

class SimilarityFinder:
    """
        Create Tf-Idf Vectorizer
    """
    def __init__(self):
        log_format = "%(asctime)s - %(created)f - %(filename)s - %(funcName)s - %(message)s"
        self.logger = create_logger(__name__, logging.ERROR, "read_docs.log", log_format)

    def similarity_finder(self, question: str, chunks: list, top_k : int = 4) -> str:
        """Give us the context

        Parameters
        ----------
        question : str
            The question user asked
        chunks : list
            The chunks we created
        top_k : int, optional
            How many similar chunks we want, by default 4

        Returns
        -------
        str
            The context for AI
        """
        
        try:
            tfidf = TFIDF()
            vectorizer = tfidf.create_tfidf()
            chunks_vec = vectorizer.fit_transform(chunks)
            query_vec = vectorizer.transform([question])        

            scores = cosine_similarity(query_vec, chunks_vec).flatten()

            top_indices = scores.argsort()[-top_k:][::-1]
            context = "\n\n".join(chunks[i] for i in top_indices)

            return context
        
        except Exception:
            self.logger.exception("Error in similarity_finder")
            return ""