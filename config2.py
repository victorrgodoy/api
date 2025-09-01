import db.chromadb as chromadb
import pandas as pd
import uuid
import requests

def populate(csv_path: str):
    df = pd.read_csv(csv_path)
    collection = get_collection()

    for _, row in df.iterrows():
        description = row["Descricao"]
        code = row["Codigo"]
        embedding = fetch_embedding(description)

        collection.add(
            ids=[str(uuid.uuid4())],
            documents=[description],
            embeddings=[embedding],
            metadatas=[{
                "codigo_ncm": code,
                "data_inicio": row["Data_Inicio"],
                "data_fim": row["Data_Fim"],
                "tipo_ato_ini": row["Tipo_Ato_Ini"],
                "numero_ato_ini": row["Numero_Ato_Ini"],
                "ano_ato_ini": row["Ano_Ato_Ini"],
            }]
        )