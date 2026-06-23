"""
File: main.py

Purpose:
---------
Run PDF extraction pipeline

Author: Ashish Gupta
Project: AI Investment Research Analyst
"""

import json
from pathlib import Path
from pathlib import Path
from src.ingestion.pdf_extractor import PDFExtractor
from src.ingestion.text_cleaner import TextCleaner
from src.ingestion.chunker import Chunker
from src.embeddings.embedding_generator import (
    EmbeddingGenerator
)


def save_embeddings(
    embedded_chunks
):

    output_file = (
        Path("data/processed")
        / "embeddings.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            embedded_chunks,
            f,
            ensure_ascii=False
        )

    print(
        f"\nEmbeddings saved: "
        f"{output_file}"
    )

def save_chunks(chunks):

    processed_folder = Path("data/processed")

    processed_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = processed_folder / "chunks.json"

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            chunks,
            f,
            ensure_ascii=False,
            indent=4
        )

    print("\nChunks saved successfully.")
    print(f"Location: {output_file}")

def main():

    print("=" * 50)
    print("AI Investment Research Analyst")
    print("PDF Extraction Pipeline")
    print("=" * 50)


     # -----------------------------------
    # Initialize Components
    # -----------------------------------
    
    extractor = PDFExtractor()
    text_cleaner = TextCleaner()
    chunker = Chunker()
    embedding_generator = EmbeddingGenerator()
    
    # -----------------------------------
    # PDF Configuration
    # -----------------------------------
    
    pdf_files = [
        {
            "path": "data/raw/Infosys_25.pdf",
            "company": "Infosys",
            "year": 2025
        },
        {
            "path": "data/raw/TCS_25.pdf",
            "company": "TCS",
            "year": 2025
        },
        {
            "path": "data/raw/HDFC_25.pdf",
            "company": "HDFC Bank",
            "year": 2025
        },
        {
            "path": "data/raw/Reliance_25.pdf",
            "company": "Reliance",
            "year": 2025
        }
    ]

    # -----------------------------------
    # Extract PDFs
    # -----------------------------------
    
    all_pages = []

    for pdf in pdf_files:

        print("\n")
        print(f"Processing: {pdf['company']}")

        try:

            pages = extractor.extract_pdf(
                pdf_path=pdf["path"],
                company_name=pdf["company"],
                year=pdf["year"]
            )

            all_pages.extend(pages)

            print(
                f"Successfully extracted "
                f"{len(pages)} pages"
            )

        except Exception as e:

            print(
                f"Failed to process "
                f"{pdf['company']}"
            )

            print(f"Error: {e}")
            
    # -----------------------------------
    # Clean Extracted Text
    # -----------------------------------

    print("\nCleaning extracted text...")

    all_pages = text_cleaner.clean_documents(
        all_pages
    )

    print(
        f"Successfully cleaned "
        f"{len(all_pages)} pages"
    )
    
     # -----------------------------------
    # Create Chunks
    # -----------------------------------
    
    print("\nCreating chunks...")

    chunks = chunker.create_chunks(
        all_pages
    )

    print(
        f"Successfully created "
        f"{len(chunks)} chunks"
    )

    # -----------------------------------
    # Save Chunks
    # -----------------------------------
    
    save_chunks(chunks)
    
    
    # -----------------------------------
    # Creating Embeddings
    # -----------------------------------
    
    print("\nGenerating Embeddings...")

    embedded_chunks = (
        embedding_generator.generate_embeddings(
            chunks
        )
    )

    print(
        f"Generated embeddings for "
        f"{len(embedded_chunks)} chunks"
    )
    
     # -----------------------------------
    # Save Embeddings
    # -----------------------------------
    
    save_embeddings(
    embedded_chunks
    )
    
    
    # -----------------------------------
    # Statistics
    # -----------------------------------

    print("\n")
    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)

    print(f"Total Pages Extracted: {len(all_pages)}")

    if all_pages:

        print("\nSample Record:\n")

        print(
            {
                "company": all_pages[0]["company"],
                "year": all_pages[0]["year"],
                "page_number": all_pages[0]["page_number"]
            }
        )

        print("\nFirst 500 Characters:\n")

        print(
            all_pages[0]["text"][:500]
        )
        print("\nSample Metadata:")
        print(all_pages[0].keys())

        print("\nSample Text:")
        print(all_pages[0]["text"][:1000])
        
        print("\nSample Chunk:\n")

        print(chunks[1])
        
        print("\nChunk Statistics")
        print("-" * 40)

        print(f"Pages      : {len(all_pages)}")
        print(f"Chunks     : {len(chunks)}")

        avg_size = sum(
            len(chunk["chunk_text"])
            for chunk in chunks
        ) / len(chunks)

        print(
            f"Avg Chunk Size : "
            f"{avg_size:.0f} characters"
        )

if __name__ == "__main__":
    main()