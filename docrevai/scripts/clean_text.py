import logging
from docrevai.logging.logger import create_logger
import re

class CleanText:
    """
        Read the raw text and return cleaned and normalized text.
    """
    def __init__(self):
        log_format = "%(asctime)s - %(created)f - %(filename)s - %(funcName)s - %(message)s"
        self.logger = create_logger(__name__, logging.ERROR, "read_docs.log", log_format)

    def clean_text(self, text: str) -> str:
        """Clean and normalize text

        Parameters
        ----------
        raw_text : str
            Text that is not clean

        Returns
        -------
        str
            Text that is clean
        """
        try:
            # Normalize unicode quotes/dashes
            replacements = {
                "\u2018": "'",
                "\u2019": "'",
                "\u201c": '"',
                "\u201d": '"',
                "\u2013": "-",
                "\u2014": "-",
                "\xa0": " ",   # non-breaking space
            }

            for old, new in replacements.items():
                text = text.replace(old, new)

            # Remove page numbers
            # Examples:
            # Page 1
            # 1
            # - 1 -

            text = re.sub(r'\n\s*Page\s+\d+\s*\n', '\n', text, flags=re.IGNORECASE)
            text = re.sub(r'\n\s*-\s*\d+\s*-\s*\n', '\n', text)
            text = re.sub(r'\n\s*\d+\s*\n', '\n', text)

            # Remove URLs
            text = re.sub(r'http\S+|www\S+', '', text)

            # Remove emails
            text = re.sub(r'\S+@\S+', '', text)

            # Fix broken hyphenated words
            # Example:
            # machine-
            # learning
            # -> machinelearning

            text = re.sub(r'-\n', '', text)

            # Replace line breaks inside sentences
            text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)

            # Remove excessive newlines
            text = re.sub(r'\n{2,}', '\n\n', text)

            # Remove weird characters
            # Keep:
            # letters, numbers, punctuation
            text = re.sub(r'[^\w\s.,!?;:%()\-\n]', ' ', text)

            # Remove multiple spaces
            text = re.sub(r'\s{2,}', ' ', text)

            # Remove duplicate lines
            seen = set()
            cleaned_lines = []

            for line in text.splitlines():
                line = line.strip()

                if line and line not in seen:
                    cleaned_lines.append(line)
                    seen.add(line)

            text = "\n".join(cleaned_lines)

            return text.strip()
        
        except Exception:
            self.logger.exception(f"Error while cleaning text.")
            return ""
