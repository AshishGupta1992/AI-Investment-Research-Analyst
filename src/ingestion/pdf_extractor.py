"""
File: pdf_extractor.py

Purpose:
--------
Extract text from annual report PDFs and return
page-level documents with metadata.

Author: Ashish Gupta
Project: AI Investment Research Analyst
"""

from pathlib import Path
import fitz  # PyMuPDF
import uuid
from typing import List, Dict


class PDFExtractor:
    """
    Extract text and metadata from PDF files.
    """

    def __init__(self):
        pass

    def extract_pdf(
        self,
        pdf_path: str,
        company_name: str,
        year: int
    ) -> List[Dict]:
        """
        Extract text from a PDF page-by-page.

        Parameters
        ----------
        pdf_path : str
            Path to PDF file

        company_name : str
            Company name

        year : int
            Report year

        Returns
        -------
        List[Dict]
        """

        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(
                f"PDF not found: {pdf_path}"
            )

        documents = []

        pdf_document = fitz.open(pdf_path)

        print(
            f"Processing {company_name} | "
            f"{year} | Pages: {len(pdf_document)}"
        )

        for page_number in range(len(pdf_document)):

            page = pdf_document[page_number]

            text = page.get_text("text")

            documents.append(
                {
                    "document_id": str(uuid.uuid4()),
                    "company": company_name,
                    "year": year,
                    "source_file": pdf_path.name,
                    "page_number": page_number + 1,
                    "text": text
                }
            )

        pdf_document.close()

        print(
            f"Completed extraction "
            f"({len(documents)} pages)"
        )

        return documents


if __name__ == "__main__":

    extractor = PDFExtractor()

    pages = extractor.extract_pdf(
        pdf_path="data/raw/Infosys_25.pdf",
        company_name="Infosys",
        year=2025
    )

    print("\nFirst Page Sample:\n")
    print(pages[0]["text"][:1000])

    print("\nMetadata:\n")
    print(pages[0])