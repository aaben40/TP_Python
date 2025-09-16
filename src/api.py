import requests
import logging
import time
try:
    from .exceptions import ThresholdExceededException
except ImportError:
    from exceptions import ThresholdExceededException

def format_url(protocol: str, hostname: str, uri: str) -> str:
    if not protocol or protocol.strip() == "":
        raise ValueError("Le protocole ne peut pas être vide")

    if not hostname or hostname.strip() == "":
        raise ValueError("Le hostname ne peut pas être vide")
    
    if not uri.startswith("/"):
        uri = "/" + uri
    url = f"{protocol}://{hostname}{uri}"
    
    if not url.startswith(("http://", "https://")):
        raise ValueError("URL mal formatée : commencer par http:// ou https://")
    return url


def http_get_etape1() -> dict:
    url = "https://dummyjson.com/products"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"Requête réussie - Code: {response.status_code}")
        else:
            logging.critical(f"Erreur de requête - Code: {response.status_code}")
            response.raise_for_status()
        return response.json()
        
    except requests.exceptions.RequestException as e:
        logging.critical(f"Erreur lors de la requête HTTP: {e}")
        raise


def http_get(url: str, threshold: int = None) -> dict:
    start_time = time.time()
    
    try:  
        timeout = threshold if threshold else 30
        response = requests.get(url, timeout=timeout)
        
        response_time = time.time() - start_time
        
        if threshold and response_time > threshold:
            raise ThresholdExceededException(
                f"Temps de reponse ({response_time:.2f}s) depasse le seuil ({threshold}s)"
            )
        
        if response.status_code == 200:
            logging.info(f"Requête réussie - Code: {response.status_code}")
        else:
            logging.critical(f"Erreur de requête - Code: {response.status_code}")
            response.raise_for_status()
        
        return response.json()
        
    except requests.exceptions.RequestException as e:
        logging.critical(f"Erreur lors de la requête HTTP: {e}")
        raise
