import pandas as pd
import requests

url = "https://portalunico.siscomex.gov.br/classif/api/publico/nomenclatura/download/json"
print("Downloading data from:", url)
resp = requests.get(url)
resp.raise_for_status()  
data = resp.json()
print("Data downloaded successfully. Number of records:", len(data))

df = pd.DataFrame(data["Nomenclaturas"])
print("DataFrame created. Number of rows:", len(df), "Number of columns:", len(df.columns))
print("Columns:", df.columns.tolist())

df_85 = df[df["Codigo"].astype(str).str.startswith("85")]
print("Filtered DataFrame for codes starting with '85'. Number of rows:", len(df_85))

df_85.to_csv("ncm_85.csv", index=False)
print("Filtered data saved to ncm_85.csv")




