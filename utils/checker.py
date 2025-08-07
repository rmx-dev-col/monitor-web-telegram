# util/checker.py
import requests
from utils.logger import log

def check_website_status(url: str) -> bool:
    try:
        response = requests.get(url, timeout=10)
        log(f"Revisión de {url} - Código: {response.status_code}")
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        log(f"[ERROR] No se pudo acceder a {url} - {e}")
        return False
