import requests

def fetch_data(url: str):
    response = requests.get(url)
    return response.json()

def crear_ingestion(url: str, payload: dict):
    response = requests.post(url, json=payload)
    return response.json()