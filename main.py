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
fake_descriptions = [
    "Transformador de energia doméstico 500VA",
    "Gerador portátil de 3kW",
    "Interruptor de parede para iluminação",
    "Painel de distribuição elétrica residencial",
    "Motor elétrico trifásico 2CV",
    "Placa controladora para inversor solar",
    "Disjuntor termomagnético 10A",
    "Bobina de ignição para equipamento elétrico",
    "Cabo de alimentação elétrica de alta tensão",
    "Sensor de corrente para medição industrial"
]

for description in fake_descriptions:
    result = search_in_collection(collection, description, 1)
    
    document = result['documents'][0][0] 
    codigo_ncm = result['metadatas'][0][0]['codigo_ncm']  
    distancia = result['distances'][0][0]

    print("Search results:")
    print(
        f"document: {document}\n"
        f"codigo_ncm: {codigo_ncm}\n"
        f"distancia: {distancia}\n"
    )
