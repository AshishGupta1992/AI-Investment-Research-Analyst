import json

from src.vectordb.qdrant_manager import (
    QdrantManager
)

# ----------------------------
# Load Embeddings
# ----------------------------

with open(
    "data/processed/embeddings.json",
    "r",
    encoding="utf-8"
) as f:

    embedded_chunks = json.load(f)

# ----------------------------
# Detect Embedding Size
# ----------------------------

vector_size = len(
    embedded_chunks[0]["embedding"]
)

print(
    f"Embedding Size: "
    f"{vector_size}"
)

# ----------------------------
# Create Collection
# ----------------------------

qdrant = QdrantManager()

qdrant.create_collection(
    vector_size=vector_size
)

qdrant.close()