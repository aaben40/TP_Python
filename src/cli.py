import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--protocol', type=str, choices=['http', 'https'], required=True, help='Protocole')
    parser.add_argument('--hostname', type=str, required=True, help='Nom d\'hôte')
    parser.add_argument('--uri', type=str, required=True, help='URI de la ressource')
    parser.add_argument('--threshold', type=int, required=True, help='Seuilde temps d\'exécution (secondes)')
    args = parser.parse_args()
    return args
