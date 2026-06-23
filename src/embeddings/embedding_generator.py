"""
File: embedding_generator.py

Purpose:
---------
Generate embeddings for chunks using BGE-M3.

Project:
AI Investment Research Analyst
"""

import time
from sentence_transformers import SentenceTransformer
from tqdm import tqdm


class EmbeddingGenerator:

    def __init__(
        self,
        model_name: str = "BAAI/bge-m3"
    ):
        """
        Initialize embedding model.
        """

        print("\nLoading embedding model...")
        start_time = time.time()

        self.model = SentenceTransformer(
            model_name
        )
        
        end_time = time.time()

        print(
            f"Model Loaded: {model_name}"
        )

        print(
            f"Loading Time: {end_time - start_time:.2f} seconds"
        )

    def generate_embeddings(
       self,
        chunks: list,
        batch_size: int = 64
    ) -> list:
        """
        Generate embeddings for chunks.

        Parameters
        ----------
        chunks : list
        
        batch_size : int


        Returns
        -------
        embedded_chunks : list
        """
        
        print("\nPreparing text for embedding generation...")

        texts = [
            chunk["chunk_text"]
            for chunk in chunks
        ]


        print(
            f"\nGenerating embeddings "
            f"for {len(texts)} chunks..."
        )
        
        start_time = time.time()

        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=True,
            normalize_embeddings=True,
            convert_to_numpy=True
        )
        
        end_time = time.time()

        print(
            f"\nEmbedding Generation Completed"
        )

        print(
            f"Time Taken: "
            f"{end_time - start_time:.2f} seconds"
        )
        
        embedded_chunks = []

        print(
            "\nAttaching embeddings to chunks..."
        )
        
        for chunk, embedding in zip(
            chunks,
            embeddings
        ):

            embedded_chunk = {
                **chunk,
                "embedding": embedding.tolist()
            }

            embedded_chunks.append(
                embedded_chunk
            )

        print(
            f"Embedded Chunks Created: "
            f"{len(embedded_chunks)}"
        )

        return embedded_chunks