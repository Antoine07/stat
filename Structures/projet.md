# Ce que Tableau ne doit PAS faire (règle claire)

❌ nettoyer les données
❌ recalculer des moyennes complexes
❌ refaire le centrage-réduction
❌ masquer des outliers

👉 Tableau consomme, Python prépare.

```
tableau_project/
│
├── data/
│   ├── raw/
│   │   └── data_raw.csv           # données brutes (jamais modifiées)
│   │
│   ├── processed/
│   │   └── data_clean.csv         # données nettoyées pour Tableau
│   │
│   └── external/
│       └── metadata.csv           # dictionnaire de données (optionnel)
│
├── scripts/
│   ├── 01_explore.py              # exploration rapide
│   ├── 02_clean.py                # nettoyage / centrage-réduction
│   ├── 03_features.py             # indicateurs calculés
│   └── run_all.py                 # pipeline simple
│
├── tableau/
│   ├── dashboard.twbx             # fichier Tableau
│   └── README_tableau.md          # consignes Tableau
│
├── outputs/
│   └── figures/                   # exports éventuels
│
├── README.md
└── requirements.txt
```