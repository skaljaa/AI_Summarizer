import os
from src.pdf_reader import extract_text_from_pdf
from src.summarizer import summarize_text
from src.vector_db import add_to_index, search

DATA_DIR = "data"
SUMMARY_DIR = "summaries"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(SUMMARY_DIR, exist_ok=True)

def process_pdf(pdf_filename):
    print(f"\nProcessing: {pdf_filename}")
    path = os.path.join(DATA_DIR, pdf_filename)
    text = extract_text_from_pdf(path)
    summary = summarize_text(text)

    # Save summary to file
    summary_path = os.path.join(SUMMARY_DIR, f"{pdf_filename}.txt")
    with open(summary_path, "w") as f:
        f.write(summary)

    # Add summary to vector DB with metadata
    add_to_index(summary, {"filename": pdf_filename, "summary_path": summary_path})
    print(f"Summary saved and indexed for: {pdf_filename}")

def run():
    print("\n== PDF Summarizer + Vector DB ==")
    pdfs = [f for f in os.listdir(DATA_DIR) if f.endswith(".pdf")]

    for pdf in pdfs:
        process_pdf(pdf)

    print("\n== Search Interface ==")
    while True:
        query = input("\nEnter a search query (or 'exit'): ")
        if query.lower() == 'exit':
            break
        results = search(query)
        print("\nTop Results:")
        for meta, score in results:
            print(f"File: {meta['filename']} (Score: {score:.2f})")

if __name__ == "__main__":
    run()
