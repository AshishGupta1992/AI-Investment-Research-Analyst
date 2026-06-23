"""
File: test_search.py

Purpose:
---------
Test semantic search.

Project:
AI Investment Research Analyst
"""

from src.retrieval.semantic_search import (
    SemanticSearch
)


def main():

    search_engine = SemanticSearch()

    query = (
        "FY2025 revenue"
    )

    results = search_engine.search(
        query=query,
        top_k=5
    )

    print("\n")
    print("=" * 60)
    print("SEARCH RESULTS")
    print("=" * 60)

    for idx, result in enumerate(
        results,
        start=1
    ):

        payload = result.payload

        print("\n")
        print(
            f"Result {idx}"
        )

        print(
            f"Score: "
            f"{result.score:.4f}"
        )

        print(
            f"Company: "
            f"{payload['company']}"
        )

        print(
            f"Page: "
            f"{payload['page_number']}"
        )

        print(
            f"\nText:\n"
        )

        print(
            payload["chunk_text"][:500]
        )

        print(
            "\n" + "-" * 60
        )


if __name__ == "__main__":
    main()