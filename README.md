# TP DataOps ETL

Pipeline ETL DataOps réalisé avec :

- Python
- pandas
- PostgreSQL
- Docker
- pytest
- GitHub Actions

## Objectif

Mettre en place un pipeline ETL :

Extract → Transform → Load

- Extract : lecture d’un fichier CSV
- Transform : nettoyage et agrégation avec pandas
- Load : chargement dans PostgreSQL

---

# Structure du projet

```bash
TP_DataOps_ETL/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── run.py
│
├── data/
│   └── ventes.csv
│
├── tests/
│   ├── conftest.py
│   ├── test_transforms.py
│   └── test_load.py
│
├── .github/workflows/
│   └── ci.yml
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Technologies utilisées

- Python 3.12
- pandas
- PostgreSQL 15
- SQLAlchemy
- psycopg2
- pytest
- Docker

---

# Installation

## 1. Cloner le projet

```bash
git clone https://github.com/thaninabel/TP_DataOps_ETL.git
cd TP_DataOps_ETL
```

## 2. Créer un environnement virtuel

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# Démarrer PostgreSQL avec Docker

```bash
docker compose up -d
```

Vérifier :

```bash
docker ps
```

---

# Lancer le pipeline ETL

```bash
python src/run.py
```

---

# Lancer les tests

## Tests complets

```bash
PYTHONPATH=. pytest -v
```

## Couverture des tests

```bash
PYTHONPATH=. pytest --cov=src
```

---

# Fonctionnalités

## Extract

- Lecture du CSV avec pandas

## Transform

- Nettoyage des emails
- Suppression des lignes invalides
- Conversion des types
- Agrégation mensuelle
- Agrégation par catégorie

## Load

- Chargement dans PostgreSQL
- Création automatique des tables
- Logging des étapes ETL

---

# CI/CD

Le projet utilise GitHub Actions pour :

- lancer automatiquement les tests
- vérifier le pipeline ETL
- valider les transformations pandas

---

# Auteur

Thanina BELLAHSENE