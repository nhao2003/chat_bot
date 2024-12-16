import os
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
if not os.path.exists("./.cache"):
    raise FileNotFoundError("Cache folder not found. Run 'python -m app.cache' to generate cache.")

# Initialize Sentence Transformer model for text embedding
embedding_model = SentenceTransformer("dangvantuan/vietnamese-embedding", cache_folder="./.cache")


def get_embedding(text: str) -> list[float]:
    """
    Generate embedding for the given text using the Sentence Transformer model.

    Args:
        text (str): Input text to generate embedding for.

    Returns:
        list[float]: Embedding vector for the input text.
    """
    if not text.strip():
        print("Attempted to get embedding for empty text.")
        return []
    
    return embedding_model.encode(text).tolist()

    # genai.configure(api_key="AIzaSyC2QatxVEu6O_J0vynLVgODEhPCGRI1mig")

    # result = genai.embed_content(
    #     model="models/text-embedding-004",
    #     content=text
    # )
    
    # return result['embedding']
