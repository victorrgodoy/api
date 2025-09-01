import uuid
import pandas as pd
import chromadb
import requests

# API Ollama
ollama_url = "http://localhost:11434/api/embeddings" 

# Inicialização com persistência
chroma_client = chromadb.Client(settings=chromadb.Settings(persist_directory="./chroma_db"))

# Deletar coleção antiga se existir
if "ncm_test" in [c.name for c in chroma_client.list_collections()]:
    chroma_client.delete_collection("ncm_test")

# Criar nova coleção com dimensão explícita
collection = chroma_client.create_collection(
    name="ncm_test",
    metadata={"hnsw:space": "cosine"},  # espaço métrico opcional
    embedding_function=None  # Desabilitar função de embedding padrão
)

# Ler CSV
df = pd.read_csv("ncm_85.csv")

# Primeiro, verificar a dimensão do embedding
test_description = df.iloc[0]["Descricao"]
data = {"model": "nomic-embed-text", "prompt": test_description}
embedding = requests.post(ollama_url, json=data).json()["embedding"]
embedding_dimension = len(embedding)
print(f"Dimensão do embedding: {embedding_dimension}")

# Recriar coleção com a dimensão correta
chroma_client.delete_collection("ncm_test")
collection = chroma_client.create_collection(
    name="ncm_test",
    metadata={"hnsw:space": "cosine"},
    embedding_function=None
)

# Iterar sobre linhas
for index, row in df.head(5).iterrows():
    description = row["Descricao"]
    code = row["Codigo"]

    data = {"model": "nomic-embed-text", "prompt": description}
    embedding = requests.post(ollama_url, json=data).json()["embedding"]

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

# Testar query - agora você precisa fornecer o embedding da query também
query_text = "Equipamentos elétricos e partes de motores"
query_data = {"model": "nomic-embed-text", "prompt": query_text}
query_embedding = requests.post(ollama_url, json=query_data).json()["embedding"]

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)
print("\nResultado da query:")
print(results)