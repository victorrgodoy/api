import data
import config2
import search
import pprint

if __name__ == "__main__":
    csv_path = data.getData()
    print("Data fetched successfully.")

    config2.populate(csv_path)
    print("Data populated into ChromaDB successfully.")

    results = search.search("transformadores elétricos", n_results=2)
    pprint("Search results:", results)





