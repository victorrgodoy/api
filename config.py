import os
from dotenv import load_dotenv

load_dotenv()

#provider ollama
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/embeddings")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")

CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "ncm_85")
CHROMA_HOST = os.getenv("CHROMA_HOST", "localhost")
CHROMA_PORT = int(os.getenv("CHROMA_PORT", 8000))

NCM_API_URL = os.getenv("NCM_API_URL", "https://portalunico.siscomex.gov.br/classif/api/publico/nomenclatura/download/json")

OUTPUT_CSV = os.getenv("OUTPUT_CSV", "ncm_85.csv")