"""
File: semantic_search.py

Purpose:
---------
Generate query embeddings and
retrieve relevant chunks from Qdrant.

Project:
AI Investment Research Analyst
"""

from sentence_transformers import SentenceTransformer

from src.vectordb.qdrant_manager import (
    QdrantManager
)


class SemanticSearch:

    def __init__(self):

        print(
            "\nLoading Embedding Model..."
        )

        self.model = SentenceTransformer(
            "BAAI/bge-m3"
        )

        self.qdrant = QdrantManager()

    def search(
        self,
        query,
        top_k=5
    ):

        print(
            f"\nSearching for: {query}"
        )

        query_embedding = self.model.encode(
            query,
            normalize_embeddings=True
        )

        results = self.qdrant.search(
            query_embedding=query_embedding.tolist(),
            limit=top_k
        )

        return results