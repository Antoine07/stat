# Analyse descriptive complète du jeu de données *Iris*

On utilise le jeu de données **Iris** :

```python
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names
```

---

##  Description du jeu de données

1. Combien y a-t-il d'observations ?
2. Combien de variables quantitatives sont mesurées ?
3. Que représente chaque ligne du tableau `X` ?

---

## Moyenne

Calculer la **moyenne** de la longueur des pétales.

* Que représente cette valeur ?
* Est-elle représentative de toutes les espèces ?

---

##  Médiane

Calculer la **médiane** de la longueur des pétales.

* Comparer moyenne et médiane.
* Que peut-on dire de la **symétrie** de la distribution ?

---

## Quartiles

Calculer les quartiles **Q1, Q2, Q3** de la longueur des pétales.

* Que représente l'intervalle ([Q1 ; Q3]) ?
* Quelle proportion des données contient-il ?

---

## Dispersion

Calculer :

* l'**étendue**
* l'**écart-type**

Puis répondre :

* La dispersion est-elle faible ou forte ?
* Pourquoi l'écart-type est-il plus pertinent que l'étendue ?

---

## Boxplot 

Tracer le **diagramme en boîte** de la longueur des pétales.

```python
# TODO
```

Questions :

1. Où se situe la médiane ?
2. La boîte est-elle large ou étroite ?
3. Observe-t-on des valeurs atypiques ?

---

## Lien boxplot ↔ dispersion

À partir du boxplot :

* la dispersion semble-t-elle **faible ou forte** ?
* la distribution semble-t-elle **symétrique** ?

👉 Justifier uniquement à partir du graphique.

---

## Valeurs atypiques : deux méthodes

### a) Méthode écart-type

Identifier les valeurs telles que :

$$
|x - \mu| > 2\sigma
$$

* Combien de valeurs sont détectées ?

### b) Méthode des quartiles

Identifier les valeurs telles que :

$$
x < Q1 - 1.5 \times IQR \quad \text{ou} \quad x > Q3 + 1.5 \times IQR
$$

* Les valeurs détectées apparaissent-elles sur le boxplot ?

---

## Question 9 – Centrage-réduction

Centrer et réduire la longueur des pétales.

- Quelle est la moyenne des valeurs centrées-réduites ?
- Comment interpréter une valeur centrée-réduite égale à **−1,5** ?

---

## Question 10 – Boxplots comparatifs (groupes)

Tracer les **boxplots par espèce**.

```python
#TODO
```

Questions :

1. Quelle espèce a les pétales les plus longs ?
2. Quelle espèce est la plus dispersée ?
3. Peut-on conclure à une causalité ? Pourquoi ?



