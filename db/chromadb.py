import chromadb
import uuid
import pandas as pd
from embedding import fetch_embedding

def create_collection(name_collection: str):
    client = chromadb.Client()
    try:
        print("Collection already exists.")
        return client.get_collection(name=name_collection)
    except:
        print("Collection created.")
        return client.create_collection(name=name_collection)
    
def populate_collection(csv_path: str, collection: str):
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        code_ncm = row["Codigo"]
        description_ncm = row["Descricao"]
        embedding = fetch_embedding(description_ncm)

        collection.add(
            ids=[str(uuid.uuid4())],
            documents=[description_ncm],
            embeddings=[embedding],  
            metadatas=[{"codigo_ncm": code_ncm}]
        )
    print("Collection populated.")