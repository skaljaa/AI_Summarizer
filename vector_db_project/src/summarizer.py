from transformers import pipeline

# Load model once globally
summarizer_pipeline = pipeline("summarization")

def summarize_text(text):
    """
    Summarizes the input text and returns the summary.
    """
    if not text:
        return "No content to summarize."

    # Split long text into chunks
    max_chunk_size = 1000
    text_chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]

    summary = ""
    for chunk in text_chunks:
        summarized = summarizer_pipeline(chunk, max_length=130, min_length=30, do_sample=False)
        summary += summarized[0]['summary_text'] + "\n"

    return summary.strip()
