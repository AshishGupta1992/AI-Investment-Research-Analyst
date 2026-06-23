"""
File: qdrant_manager.py

Purpose:
---------
Manage Qdrant collection creation and connection.

Project:
AI Investment Research Analyst
"""

from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance
)
from qdrant_client.models import PointStruct


class QdrantManager:

    def __init__(
        self,
        collection_name="financial_reports"
    ):

        self.collection_name = collection_name

        print(
        "\nInitializing Local Qdrant..."
        )

        self.client = QdrantClient(
            path="./qdrant_data"
        )

        print(
        "Qdrant Initialized Successfully."
         )

    def close(self):
        """
        Close Qdrant connection.
        """

        self.client.close()

        print(
            "\nQdrant connection closed."
    )
    
    def create_collection(
        self,
        vector_size
    ):
        """
        Create collection if not exists.
        """

        collections = (
            self.client.get_collections()
        )

        existing_collections = [
            collection.name
            for collection
            in collections.collections
        ]

        if self.collection_name in existing_collections:

            print(
                f"\nCollection already exists:"
            )

            print(self.collection_name)

            return

        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )

        print(
            f"\nCollection Created:"
        )

        print(self.collection_name)

    def search(
        self,
        query_embedding,
        limit=5
    ):
        """
        Search vectors in Qdrant.
        """

        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_embedding,
            limit=limit
        )

        return results.points
    
    def upload_embeddings(
        self,
        embedded_chunks,
        batch_size=100
    ):
        """
        Upload embeddings to Qdrant.
        """

        print(
            f"\nUploading "
            f"{len(embedded_chunks)} vectors..."
        )

        for i in range(
            0,
            len(embedded_chunks),
            batch_size
        ):

            batch = embedded_chunks[
                i:i + batch_size
            ]

            points = []

            for idx, item in enumerate(batch):

                points.append(
                    PointStruct(
                        id=i + idx,
                        vector=item["embedding"],
                        payload={
                            "chunk_id":
                                item["chunk_id"],

                            "company":
                                item["company"],

                            "year":
                                item["year"],

                            "page_number":
                                item["page_number"],

                            "source_file":
                                item["source_file"],

                            "chunk_text":
                                item["chunk_text"]
                        }
                    )
                )

            self.client.upsert(
                collection_name=
                self.collection_name,

                points=points
            )

            print(
                f"Uploaded "
                f"{min(i + batch_size, len(embedded_chunks))}"
                f"/{len(embedded_chunks)}"
            )

        print(
            "\nUpload Completed."
        )