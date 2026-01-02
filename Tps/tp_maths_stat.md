# TP de révision

## Dispersion – Corrélation – Matrices

**Durée : 2 heures**
**Rendu : Notebook (Jupyter / Colab)**
**Travail : individuel ou binôme (2 personnes maximum)**

---

## Contraintes techniques

* Langage : **Python**
* Bibliothèques autorisées : `numpy`, `pandas`, `matplotlib` (facultatif pour visualisation)
* Toute cellule doit être **commentée** (raisonnement + interprétation)
* Le notebook doit être **exécutable de bout en bout**

---

## Dispersion

On considère le jeu de données suivant :

```python
import numpy as np

X = np.array([12, 15, 14, 10, 18, 20, 16, 14, 13, 17])
```

### Questions

1. Calculer :

   * la moyenne ;
   * la variance ;
   * l’écart-type.
2. Refaire les calculs **sans utiliser `np.var` ni `np.std`**.
3. Interpréter :

   * que signifie une variance élevée ?
   * que peut-on dire de la dispersion de `X` ?

---

## Corrélation 

On introduit un second jeu de données :

```python
Y = np.array([8, 11, 10, 7, 14, 15, 12, 10, 9, 13])
```

### Questions

1. Tracer le **nuage de points** (X,Y).
2. Calculer le **coefficient de corrélation de Pearson**.
3. Vérifier le résultat par un calcul **manuel** à partir des formules.
4. Interpréter :

   * signe de la corrélation ;
   * intensité ;
   * limites de la corrélation linéaire.

---

## Matrices

On considère la matrice de données :

```python
D = np.column_stack((X, Y))
```

### Matrice de covariance

1. Centrer les données.
2. Calculer la **matrice de covariance**.
3. Interpréter chaque coefficient.

---

### Valeurs propres et vecteurs propres

On note (C) la matrice de covariance.

1. Calculer les **valeurs propres** de (C).
2. Calculer les **vecteurs propres associés**.
3. Vérifier :
   $$
   Cv = \lambda v
   $$

### Questions d’analyse

* Quelle valeur propre est dominante ?
* Que représente le vecteur propre associé ?
* Lien avec la dispersion maximale des données.

---

## Synthèse et recul critique (15 min)

Répondre **rédigé** aux questions suivantes :

1. Lien entre variance, covariance et corrélation.
2. Apport des matrices dans l’analyse statistique.
3. Intérêt des valeurs propres en analyse de données (intuition).

---

##  Dispersion et corrélation sur un jeu de données réel (Penguins)

Cette partie vise à appliquer les notions précédentes à un **jeu de données réel multivarié**.

### Données

```python
import pandas as pd
import seaborn as sns

penguins = sns.load_dataset("penguins")
penguins = penguins.dropna()
penguins.head()
```

Variables quantitatives :

* `bill_length_mm`
* `bill_depth_mm`
* `flipper_length_mm`
* `body_mass_g`

Variable qualitative :

* `species`

---

### 4.1 Dispersion univariée

1. Donner les **statistiques descriptives** des variables quantitatives.
2. Calculer variance et écart-type pour chaque variable.
3. Comparer les niveaux de dispersion :

   * quelle variable est la plus dispersée ?
   * laquelle est la plus homogène ?

---

### 4.2 Boxplots et interprétation graphique

1. Tracer les **boxplots des variables quantitatives**.
2. Tracer des **boxplots par espèce** pour :

   * `body_mass_g`
   * `flipper_length_mm`
3. Interpréter :

   * présence de valeurs aberrantes ;
   * différences de dispersion entre espèces ;
   * séparation (ou non) des médianes.

---

### 4.3 Corrélation multivariée

1. Calculer la **matrice de corrélation** des variables quantitatives.

2. Identifier :

   * corrélations fortes ;
   * corrélations faibles ou négatives.

3. Représenter la matrice de corrélation sous forme de **heatmap**.

4. Interpréter les relations observées.

---

## Synthèse et recul critique

Répondre **de manière rédigée et argumentée** :

1. Lien entre variance, covariance et corrélation.
2. Apport des matrices dans l’analyse statistique.
3. Intérêt des valeurs propres en analyse de données (intuition).
4. Différence entre analyse sur données simples et données réelles.

---
