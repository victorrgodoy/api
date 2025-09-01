import requests
import config.settings as settings

def fetch_embedding(text: str):
    data = {"model": "nomic-embed-text", "prompt": text}
    response = requests.post(settings.OLLAMA_URL, json=data)
    response.raise_for_status()
    return response.json()["embedding"]