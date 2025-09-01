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
query = "Materiais elétricos"
results = search_in_collection(collection, query, 3)

pprint(results)
