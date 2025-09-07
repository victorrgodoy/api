from pprint import pprint
from util.data import fetch_ncm_data
from db.chromadb import create_collection, populate_collection, search_in_collection

# 1 - Fetch data from gov (ncm 85)
fetch_ncm_data()

# 2 - Create database
collection = create_collection("ncm_85")

# 3 - Populate database with LLM Embedding
populate_collection("data/ncm_85.csv", collection)

#4 - Search in collection
query = "Trifásicos"
results = search_in_collection(collection, query, 1)

document = results['documents'][0][0] 

codigo_ncm = results['metadatas'][0][0]['codigo_ncm']  

distancia = results['distances'][0][0]

print("Search results:")
print(
    f"document: {document}\n"
    f"codigo_ncm: {codigo_ncm}\n"
    f"distancia: {distancia}\n"
)
