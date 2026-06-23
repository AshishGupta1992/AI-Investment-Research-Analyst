"""
File: load_embeddings.py

Purpose:
---------
Load embeddings.json
and upload vectors into Qdrant.

Project:
AI Investment Research Analyst
"""

import json

from src.vectordb.qdrant_manager import (
    QdrantManager
)


def main():

    print(
        "\nLoading embeddings.json..."
    )

    with open(
        "data/processed/embeddings.json",
        "r",
        encoding="utf-8"
    ) as f:

        embedded_chunks = json.load(f)

    print(
        f"Loaded "
        f"{len(embedded_chunks)} embeddings"
    )

    # --------------------------------
    # Connect Qdrant
    # --------------------------------

    qdrant = QdrantManager()

    # --------------------------------
    # Upload
    # --------------------------------

    qdrant.upload_embeddings(
        embedded_chunks
    )

    qdrant.close()


if __name__ == "__main__":
    main()