---
marp: true
theme: default
paginate: true
class: lead
---

# Statistiques descriptives – bases indispensables

---

## Objectif du chapitre

1. Décrire un jeu de données
2. Résumer l'information par quelques nombres clés
3. Comprendre la dispersion
4. Visualiser correctement les données

---

## Jeu de données simple

```python
import numpy as np

notes = np.array([8, 9, 10, 10, 11, 12, 13, 15, 18])
```

---

## Moyenne – idée intuitive

> La moyenne représente le **niveau global** de la série.

Formule :

$$
\mu = \frac{1}{n} \sum_{i=1}^n x_i
$$

```python
notes.mean()
```

---

## Exercice 1 – Moyenne

```python
temps = np.array([12.3, 12.5, 12.7, 13.1, 14.8])
```

1. Calculez la moyenne
2. Interprétez-la

```python
# TODO
```

---

## Médiane

> La médiane est la valeur qui **coupe la série en deux parties égales**.

- 50 % des valeurs sont en dessous
- 50 % sont au-dessus

```python
np.median(notes)
```

---

## Moyenne vs médiane

Exemple :

```python
data = np.array([10, 10, 11, 11, 12, 30])
```

- moyenne élevée
- médiane stable

👉 La médiane est **robuste aux valeurs extrêmes**.

---

## Quartiles

> Les quartiles découpent la série en **4 parts égales**.

- Q1 : 25 %
- Q2 : médiane
- Q3 : 75 %

```python
np.percentile(notes, [25, 50, 75])
```

---

## Exercice 2 – Quartiles

```python
data = np.array([4, 6, 7, 9, 10, 12, 14, 18])
```

1. Calculez Q1, Q2, Q3
2. Interprétez chaque valeur

```python
# TODO
```

---

## Dispersion – pourquoi c'est essentiel ?

Deux séries peuvent avoir :

- la **même moyenne**,
- mais des comportements très différents.

Exemples :

A : `[10, 10, 10, 10]`
B : `[5, 10, 15, 10]`

---

## Étendue

> Différence entre la plus grande et la plus petite valeur.

```python
notes.max() - notes.min()
```

---

## Variance

> Mesure la **dispersion moyenne autour de la moyenne**.

Formule :

$$
\sigma^2 = \frac{1}{n} \sum (x_i - \mu)^2
$$

```python
notes.var()
```

---

## Écart-type

> Racine carrée de la variance
> → même unité que les données.

```python
notes.std()
```

---

## Interprétation de l'écart-type

- faible → données regroupées
- élevé → données dispersées

Lien direct avec le **centrage-réduction**.

---

## Exercice 3 – Dispersion

```python
A = np.array([10, 10, 10, 10])
B = np.array([7, 10, 13, 10])
```

1. Calculez moyenne et écart-type
2. Comparez les dispersions

```python
# TODO
```

---

## Visualisation : histogramme

```python
import matplotlib.pyplot as plt

plt.hist(notes, bins=5)
plt.xlabel("Valeurs")
plt.ylabel("Fréquence")
plt.show()
```

---

## Interprétation de l'histogramme

- symétrique ?
- étalé ?
- présence de valeurs extrêmes ?

---

## Diagramme en boîte (boxplot)

> Résume la série avec les quartiles et la dispersion.

```python
plt.boxplot(notes, vert=False)
plt.show()
```

---

## Lecture du boxplot

1. Boîte = Q1 → Q3
2. Trait central = médiane
3. Moustaches = valeurs normales
4. Points isolés = valeurs atypiques

---

## Exercice 4 – Boxplot comparatif

```python
groupe_A = np.array([10, 11, 12, 12, 13])
groupe_B = np.array([8, 9, 10, 15, 20])
```

1. Tracez les boxplots
2. Comparez médiane et dispersion

```python
# TODO
```

---

## Résumé 

1. **Moyenne** → niveau global
2. **Médiane** → valeur centrale robuste
3. **Écart-type** → dispersion
4. **Histogramme** → forme de la distribution
5. **Boxplot** → synthèse visuelle

---

# Statistiques descriptives – approfondissement

---

## Pourquoi aller plus loin ?

Deux séries peuvent avoir :

- même moyenne,
- même écart-type,
- mêmes quartiles,

👉 **mais des formes très différentes**.

On va maintenant :

1. décrire la **forme** des distributions,
2. détecter les **valeurs atypiques**,
3. comparer **plusieurs groupes** proprement.

---

## Forme d'une distribution

Trois notions clés :

1. Symétrie / dissymétrie
2. Asymétrie (skewness)
3. Concentration (kurtosis)

---

## Distribution symétrique

Exemple typique : loi normale.

```python
x = np.random.normal(0, 1, 1000)
```

- moyenne ≈ médiane
- histogramme équilibré
- boxplot centré

---

## Distribution asymétrique (skewed)

Deux cas :

### Asymétrie à droite (skew positif)

- queue longue vers les grandes valeurs
- moyenne > médiane

Exemples :

- revenus
- temps d'attente

---

### Asymétrie à gauche (skew négatif)

- queue longue vers les petites valeurs
- moyenne < médiane

Exemples :

- notes plafonnées
- scores avec effet plafond

---

## Illustration simple

```python
data = np.array([1, 2, 2, 3, 3, 4, 20])
```

- médiane ≈ 3
- moyenne tirée vers 20

👉 la moyenne est **sensible aux valeurs extrêmes**

---

## Mesure de l'asymétrie (skewness)

```python
from scipy.stats import skew

skew(data)
```

Interprétation :

- ≈ 0 → symétrique
- > 0 → asymétrie à droite
- < 0 → asymétrie à gauche

---

## Exercice 5 – Asymétrie

```python
A = np.array([9, 10, 10, 11, 12])
B = np.array([9, 10, 10, 11, 30])
```

1. Comparez moyenne et médiane
2. Calculez l'asymétrie
3. Interprétez la forme des distributions

```python
# TODO
```

---

## Concentration des valeurs (kurtosis)

> Mesure si les valeurs sont :

- très concentrées autour de la moyenne
- ou très étalées avec des extrêmes

```python
from scipy.stats import kurtosis

kurtosis(data)
```

Interprétation (simplifiée) :

- proche de 0 → forme “normale”
- > 0 → beaucoup de valeurs extrêmes
- < 0 → distribution aplatie

---

## Valeurs atypiques (outliers)

Une valeur atypique :

- n'est pas forcément fausse
- mais **doit être expliquée**

Exemples :

- erreur de mesure
- situation exceptionnelle
- individu particulier

---

## Détection avec l'écart-type

Règle simple (approximative) :

> |x − moyenne| > 2 × écart-type → valeur suspecte
> |x − moyenne| > 3 × écart-type → valeur très atypique

---

## Détection avec les quartiles (boxplot)

Méthode robuste :

$$
\text{IQR} = Q3 - Q1
$$

Valeurs atypiques si :

- < Q1 − 1.5 × IQR
- > Q3 + 1.5 × IQR

---

## Exercice 6 – Outliers

```python
data = np.array([10, 11, 12, 12, 13, 14, 50])
```

1. Calculez Q1, Q3, IQR
2. Identifiez les valeurs atypiques
3. Comparez avec la méthode écart-type

```python
# TODO
```

---

## Comparer plusieurs groupes (descriptif)

On reste **sans test statistique**.

```python
groupe_A = np.array([10, 11, 12, 13, 14])
groupe_B = np.array([8, 9, 10, 20, 25])
```

---

## Comparaison numérique

Comparer :

1. moyenne
2. médiane
3. écart-type
4. étendue

```python
for g in [groupe_A, groupe_B]:
    print(g.mean(), g.std(), np.median(g))
```

---

## Comparaison graphique (indispensable)

```python
plt.boxplot([groupe_A, groupe_B], labels=["A", "B"])
plt.show()
```

---

## Lecture comparative

Questions clés :

1. Quel groupe est plus dispersé ?
2. Les médianes sont-elles proches ?
3. Y a-t-il des valeurs atypiques ?
4. Les distributions sont-elles comparables ?

---

## Exercice 7 – Analyse complète

```python
A = np.array([12, 13, 14, 15, 16])
B = np.array([10, 11, 12, 20, 22])
```

Réaliser :

1. statistiques descriptives complètes
2. histogrammes
3. boxplots
4. interprétation écrite

---

## Résumé 

1. La moyenne décrit le **niveau**
2. L'écart-type décrit la **dispersion**
3. L'asymétrie décrit la **forme**
4. Les outliers nécessitent **analyse critique**
5. Les graphiques sont **indispensables**
