import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model once
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# In-memory FAISS index (L2 distance)
dimension = 384  # Matches embedding size of the model
index = faiss.IndexFlatL2(dimension)

# Metadata store
metadata = []

def embed_text(text):
    return embedding_model.encode([text])[0]

def add_to_index(text, meta):
    vector = embed_text(text)
    index.add(np.array([vector]))
    metadata.append(meta)

def search(query, k=3):
    vector = embed_text(query)
    D, I = index.search(np.array([vector]), k)
    return [(metadata[i], D[0][j]) for j, i in enumerate(I[0]) if i < len(metadata)]
