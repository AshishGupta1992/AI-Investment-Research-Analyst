"""
File: text_cleaner.py

Purpose:
---------
Clean extracted PDF text before chunking.

Project:
AI Investment Research Analyst
"""

import re


class TextCleaner:

    def __init__(self):
        pass

    def clean_text(self, text: str) -> str:
        """
        Clean PDF extracted text.

        Parameters
        ----------
        text : str

        Returns
        -------
        str
        """

        if not text:
            return ""

        # -----------------------------
        # Remove non-breaking spaces
        # -----------------------------
        text = text.replace("\xa0", " ")

        # -----------------------------
        # Remove tabs
        # -----------------------------
        text = text.replace("\t", " ")

        # -----------------------------
        # Remove extra newlines
        # -----------------------------
        text = re.sub(r"\n+", "\n", text)

        # -----------------------------
        # Remove multiple spaces
        # -----------------------------
        text = re.sub(r"\s+", " ", text)

        # -----------------------------
        # Remove page references
        # Example:
        # Page 123
        # PAGE 145
        # -----------------------------
        text = re.sub(
            r'\bpage\s+\d+\b',
            '',
            text,
            flags=re.IGNORECASE
        )

        # -----------------------------
        # Remove standalone page numbers
        # -----------------------------
        text = re.sub(
            r'^\d+$',
            '',
            text,
            flags=re.MULTILINE
        )

        # -----------------------------
        # Remove leading/trailing spaces
        # -----------------------------
        text = text.strip()

        return text

    def clean_documents(self, documents):
        """
        Clean all extracted pages.
        """

        cleaned_docs = []

        for doc in documents:

            cleaned_text = self.clean_text(
                doc["text"]
            )

            doc["text"] = cleaned_text

            cleaned_docs.append(doc)

        return cleaned_docs