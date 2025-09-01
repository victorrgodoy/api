import chromadb
import uuid
import pandas as pd
import logging
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction
from config import CHROMA_COLLECTION, OLLAMA_URL, EMBEDDING_MODEL

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def create_collection(name_collection: str = CHROMA_COLLECTION, path: str = "./chroma.db"):
    client = chromadb.PersistentClient(path)

    ollama_ef = OllamaEmbeddingFunction(
        url=OLLAMA_URL,
        model_name=EMBEDDING_MODEL,
    )
    
    try:
        collection = client.get_collection(
            name=name_collection,
            embedding_function=ollama_ef
        )
        logger.info(f"Collection '{name_collection}' already exists.")
        return collection
    except:
        collection = client.create_collection(
            name=name_collection,
            embedding_function=ollama_ef
        )
        logger.info(f"Collection '{name_collection}' created with Ollama embedding function.")
        return collection
    
def populate_collection(csv_path: str, collection):

    if collection.count() > 0:
        logger.info(f"Collection already has {collection.count()} items. Skipping population.")
        return

    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        code_ncm = row["Codigo"]
        description_ncm = row["Descricao"]

        collection.add(
            ids=[str(uuid.uuid4())],
            documents=[description_ncm],  
            metadatas=[{"codigo_ncm": code_ncm}]
        )
    
    logger.info(f"Collection populated with {len(df)} items!")

def search_in_collection(collection, query: str, n_results: int = 5):
    results = collection.query(
        query_texts=[query], 
        n_results=n_results,
    )
    logger.info(f"Search completed for: '{query}'")
    return results