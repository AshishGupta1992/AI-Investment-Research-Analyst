# AI-Investment-Research-Analyst
AI-powered financial research system that transforms annual reports into a searchable knowledge base using Semantic Search, BGE-M3 embeddings, and Qdrant.

# AI Investment Research Analyst

An AI-powered financial research system that transforms annual reports into a searchable knowledge base using Semantic Search, BM25, Hybrid Retrieval, BGE-M3 embeddings, and Qdrant.

## Project Overview

Financial annual reports often contain hundreds of pages of information. Finding specific insights manually can be time-consuming.

This project builds a Retrieval-Augmented Generation (RAG) foundation that enables users to retrieve relevant information from annual reports using advanced search techniques.

Current implementation includes:

- PDF Extraction
- Text Cleaning
- Chunking
- Embedding Generation (BGE-M3)
- Qdrant Vector Database
- Semantic Search

## Data Sources

The project currently uses FY2024-25 annual reports from:

- Infosys
- TCS
- HDFC Bank
- ICICI Bank
- Reliance Industries

## Architecture

Annual Reports

➡️ PDF Extraction

➡️ Text Cleaning

➡️ Chunking

➡️ Embedding Generation (BGE-M3)

➡️ Qdrant Vector Database

➡️ Semantic Search


## Project Structure

```text
AI_Investment_Research_Analyst/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── ingestion/
│   ├── embeddings/
│   ├── vectordb/
│   └── retrieval/
│
├── main.py
├── README.md
├── INSTRUCTIONS.md
└── requirements.txt
```

## Technologies Used

- Python
- Sentence Transformers
- BAAI/bge-m3
- Qdrant
- NumPy
- Pandas

## Retrieval Methods Implemented

### Semantic Search

Uses vector embeddings to retrieve chunks based on semantic meaning.


## Sample Query

```text
FY2025 revenue
```

Retrieved results include:

- Revenue from Operations
- Financial Results
- Revenue Growth Analysis
- CEO Commentary

## Current Progress

### Completed

- [x] PDF Extraction
- [x] Chunking
- [x] Embedding Generation
- [x] Qdrant Integration
- [x] Semantic Search

### Planned

- [ ] Reranking
- [ ] LLM Answer Generation
- [ ] Source Citations
- [ ] Multi-Document Comparison
- [ ] Financial Research Agent

## Repository Notes

The following files are intentionally excluded from GitHub:

- Annual Reports (PDFs)
- chunks.json
- embeddings.json
- Qdrant local database files

These files are generated during execution.

## Author

Ashish Gupta

Senior Data Analyst | AI & Analytics Enthusiast

