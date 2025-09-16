import logging
import json
from src.cli import parse_args
from src.api import format_url, http_get
from src.exceptions import ThresholdExceededException

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def main():
    setup_logging()
    
    try:
        args = parse_args()
        
        url = format_url(args.protocol, args.hostname, args.uri)
        print(f"URL: {url}")
        
        result = http_get(url, args.threshold)
        
        print("Répons JSON:")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        
    except ThresholdExceededException as e:
        print(f"ERREUR - Seuil dépassé: {e}")
        return 1
    except ValueError as e:
        print(f"ERREUR - Paramètre invalide: {e}")
        return 1
    except Exception as e:
        print(f"ERREUR - Une erreur s'est produite: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
