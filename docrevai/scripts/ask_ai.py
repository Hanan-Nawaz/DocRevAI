from docrevai.logging.logger import create_logger
from ollama import chat
import logging 

class AskAI:
    """
        AI answers the users question 
    """
    def __init__(self):
        log_format = "%(asctime)s - %(created)f - %(filename)s - %(funcName)s - %(message)s"
        self.logger = create_logger(__name__, logging.ERROR, "read_docs.log", log_format)

    def ask_ai(self, question: str, context: str) -> str:
        """AI answers the users question 

            Parameters
            ----------
            question : str
                The question user aksed to AI
            context : str
                The Context AI have

            Returns
            -------
            str
                The answer of the question
        """
        try:
            prompt = f"""
                You are a PDF question-answering assistant.

                Answer the question using ONLY the context below.

                Rules:
                - Do not use outside knowledge.
                - If the answer is not clearly present in the context, say:
                "I could not find this in the PDF."
                - Do not guess.
                - Keep the answer short.

                Context:
                {context}

                Question:
                {question}

                Answer:
            """

            response = chat(
                model = "phi3:mini",
                messages=[
                    {
                        "role": "user", "content": prompt
                    }
                ]
            )

            return response.message.content
        
        except Exception:
            self.logger.exception("Error in Ask Ai")