from config2 import get_collection  # se config.py está na mesma pasta
from ollama import fetch_embedding  # ajustado para mesma pasta

def search(query: str, n_results: int = 2):
    collection = get_collection()
    
    # Gera o embedding com Ollama
    query_embedding = fetch_embedding(query)
    
    # Passa o embedding na query
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )



