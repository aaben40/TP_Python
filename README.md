# Mini-Projet Python API

## Installation et utilisation

### 1. Télécharger le projet
```bash
# Via Git
git clone https://github.com/aaben40/TP_Python.git
cd TP_Python

# Ou télécharger le ZIP depuis GitHub et extraire
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Utilisation
```bash
# Test avec l'API DummyJSON (succès)
python main.py --protocol https --hostname dummyjson.com --uri /products --threshold 10

# Test avec timeout (échec volontaire)
python main.py --protocol https --hostname google.fr:9443 --uri / --threshold 5
```

### 4. Lancer les tests
```bash
python test/test_api.py
```

## Paramètres

- `--protocol` : http ou https
- `--hostname` : nom d'hôte (ex: dummyjson.com)
- `--uri` : URI de la ressource (ex: /products)
- `--threshold` : seuil de timeout en secondes

## Structure 

```
TP_Python/
├── main.py              # Point d'entrée principal
├── requirements.txt     # Dépendances Python
├── src/
│   ├── api.py          # Fonctions HTTP et formatage URL
│   ├── cli.py          # Gestion des arguments CLI
│   └── exceptions.py   # Exception personnalisée
└── test/
    └── test_api.py     # Tests unitaires
```

## Exemples 

```bash
# API publique (succès attendu)
python main.py --protocol https --hostname httpbin.org --uri /get --threshold 5

# Serveur inaccessible (timeout attendu)
python main.py --protocol https --hostname example.com:9999 --uri / --threshold 3
```