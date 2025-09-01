import requests
import pandas as pd
import dataclasses


@dataclasses
class Data:
    url: str = "https://portalunico.siscomex.gov.br/classif/api/publico/nomenclatura/download/json"
    output_csv: str = "ncm_85.csv"

    def fetch_data(self):
        resp = requests.get(self.url)
        resp.raise_for_status()
        data = resp.json()
        return data
    

    def filter_data(self, data):
        df = pd.DataFrame(data["Nomenclaturas"])
        df_filtered = df[df["Codigo"].astype(str).str.startswith("85")]
        df_filtered.to_csv(self.output_csv, index=False)
        return df_filtered