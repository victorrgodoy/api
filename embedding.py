import config
import requests

def get_embedding(prompt: str):
    model = config.EMBEDDING_MODEL
    url = config.EMBEDDING_API_URL
    prompt = prompt
    generate = {'model': model, 'prompt': prompt}

    try:
        response = requests.post(url, json=generate, timeout=30)
        response.raise_for_status()
        return response.json()["embedding"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching embedding: {e}")
        raise

    