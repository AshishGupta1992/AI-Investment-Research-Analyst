"""
File: chunker.py

Purpose:
---------
Convert cleaned documents into chunks suitable
for embeddings and vector search.

Project:
AI Investment Research Analyst
"""

import uuid
from typing import List, Dict

from langchain_text_splitters import RecursiveCharacterTextSplitter


class Chunker:

    def __init__(
        self,
        chunk_size: int = 800,
        chunk_overlap: int = 150
    ):
        """
        Parameters
        ----------
        chunk_size : int
            Max characters per chunk

        chunk_overlap : int
            Overlap between chunks
        """

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def create_chunks(
        self,
        documents: List[Dict]
    ) -> List[Dict]:
        """
        Convert page-level documents into chunks.

        Parameters
        ----------
        documents : List[Dict]

        Returns
        -------
        List[Dict]
        """

        chunks = []

        for doc in documents:

            text = doc["text"]

            split_chunks = self.text_splitter.split_text(
                text
            )

            for chunk_text in split_chunks:

                chunk = {
                    "chunk_id": str(uuid.uuid4()),
                    "company": doc["company"],
                    "year": doc["year"],
                    "source_file": doc["source_file"],
                    "page_number": doc["page_number"],
                    "chunk_text": chunk_text
                }

                chunks.append(chunk)

        return chunks