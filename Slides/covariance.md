---
marp: true
theme: default
paginate: true
class: lead
---

# Covariance et ANOVA

**Comprendre le lien entre variables et comparer des groupes**

---

## Pourquoi ce chapitre ?

Jusqu'ici, vous savez :

- décrire une variable (moyenne, dispersion),
- visualiser des distributions.

On va maintenant répondre à deux nouvelles questions :

1. **Deux variables évoluent-elles ensemble ?** → *Covariance*
2. **Plusieurs groupes ont-ils la même moyenne ?** → *ANOVA*

---

# PARTIE 1 — COVARIANCE

---

## Problème posé

On observe deux variables sur les mêmes individus :

- taille et poids
- temps d'entraînement et performance
- âge et salaire

👉 **Quand l'une augmente, que fait l'autre ?**

---

## Exemple simple

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5])   # heures de travail
y = np.array([10, 12, 15, 18, 20])  # score
```

---

## Visualisation indispensable

```python
import matplotlib.pyplot as plt

plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
```

---

## Intuition de la covariance

> La covariance mesure **si deux variables varient ensemble**.

- si x ↑ et y ↑ → covariance **positive**
- si x ↑ et y ↓ → covariance **négative**
- si pas de lien clair → covariance ≈ 0

---

## Définition mathématique

$$
\text{Cov}(X,Y)
= \frac{1}{n} \sum (x_i - \bar x)(y_i - \bar y)
$$

👉 On compare les **écarts à la moyenne**.

---

## Lecture intuitive du produit

- (x − moyenne) et (y − moyenne) **même signe** → produit positif
- signes opposés → produit négatif

Donc :

- majorité de produits positifs → covariance positive
- majorité négatifs → covariance négative

---

## Calcul en Python

```python
np.cov(x, y)
```

La covariance recherchée est :

```python
np.cov(x, y)[0, 1]
```

---

## Problème majeur de la covariance ⚠️

> **La covariance dépend des unités.**

Exemple :

- cm × kg
- heures × points

👉 Impossible de comparer directement deux covariances.

C'est pour cela que l'on introduira ensuite la **corrélation**.

---

## Exercice 1 — Covariance

```python
a = np.array([2, 4, 6, 8])
b = np.array([8, 6, 4, 2])
```

1. Tracez le nuage de points
2. Calculez la covariance
3. Interprétez le signe

```python
# TODO
```

---

## Résumé Covariance

1. Mesure la variation conjointe de deux variables
2. Signe → sens de la relation
3. Valeur brute → dépend des unités
4. Outil fondamental avant corrélation et ACP

---

# PARTIE 2 — ANOVA (Analyse de la variance)

---

## Problème posé

On a **plusieurs groupes** et on veut savoir :

> **Ont-ils la même moyenne ou pas ?**

Exemples :

- méthodes pédagogiques
- traitements médicaux
- machines
- groupes d'individus

---

## Exemple concret

```python
A = np.array([12, 13, 11, 12])
B = np.array([16, 17, 15, 16])
C = np.array([10, 9, 11, 10])
```

---

## Moyennes par groupe

```python
A.mean(), B.mean(), C.mean()
```

On observe des différences…
👉 mais sont-elles **réelles** ou **dues au hasard** ?

---

## Pourquoi le hasard peut tromper

Même si les **vraies moyennes** sont égales :

- les données sont dispersées,
- les moyennes observées fluctuent.

👉 L'ANOVA sert à décider **objectivement**.

---

## Principe fondamental de l'ANOVA

L'ANOVA compare :

1. la **variabilité entre les groupes**
2. la **variabilité à l'intérieur des groupes**

---

## Intuition clé

> Si les groupes sont très différents **entre eux**,
> mais homogènes **en leur sein**,
> alors les moyennes sont probablement différentes.

---

## Schéma conceptuel

![Image](https://www.researchgate.net/publication/329788831/figure/fig2/AS%3A711397558206464%401546621803288/Graphical-representation-of-the-rationale-behind-the-analysis-of-variance-ANOVA-A.png)

---

![Image](https://stpltrsrcscmnprdwus001.blob.core.windows.net/rsrcs/srm/images/research-methods-statistics-for-public-nonprofit-administrators-practical-guide/10.4135_9781544307763-fig10-1.jpg)

- dispersion interne = bruit
- dispersion entre groupes = signal

---

## Hypothèses statistiques

- **H₀** : toutes les moyennes sont égales
- **H₁** : au moins une moyenne est différente

---

## Statistique F

$$
F = \frac{\text{Variance entre groupes}}
{\text{Variance intra-groupes}}
$$

- F ≈ 1 → pas de différence claire
- F grand → différence probable

---

## ANOVA en Python (SciPy)

```python
from scipy.stats import f_oneway

f_stat, p_value = f_oneway(A, B, C)
f_stat, p_value
```

---

## Interprétation de la p-value

- p < 0.05 → différence significative
- p ≥ 0.05 → pas de conclusion claire

👉 **ANOVA ≠ dire quels groupes diffèrent**,
mais **dire qu'il existe une différence**.

---

## Exercice 2 — ANOVA

```python
G1 = np.array([10, 11, 10, 9])
G2 = np.array([12, 13, 14, 13])
G3 = np.array([10, 9, 8, 9])
```

1. Calculez les moyennes
2. Lancez l'ANOVA
3. Concluez

```python
# TODO
```

---

## Conditions d'application (simplifiées)

ANOVA est pertinente si :

1. données quantitatives
2. groupes indépendants
3. distributions à peu près normales
4. dispersions comparables

---

## Lien avec ce que vous connaissez déjà

- variance → dispersion
- écart-type → homogénéité
- centrage-réduction → comparaison équitable
- ANOVA → généralisation du test de moyenne

---

## Résumé général

### Covariance

- mesure la variation conjointe
- dépend des unités
- base de la corrélation

### ANOVA

- compare plusieurs moyennes
- s'appuie sur la variance
- distingue hasard / effet réel

Parfait. Voici la **suite naturelle du cours**, toujours **débutant Bac S**, structurée **comme vos slides**, avec **intuition → maths → Python → exercices**, couvrant :

1. **Corrélation = covariance normalisée**
2. **Lien covariance ↔ matrice**
3. **ACP avec matrices, valeurs propres et vecteurs propres (sans lourdeur inutile)**

---

# Corrélation et ACP

**Du lien entre variables à la réduction de dimension**

---

# PARTIE 1 — CORRÉLATION

*(normalisation de la covariance)*

---

## Problème de la covariance (rappel)

La covariance indique :

- le **sens** du lien,
- mais dépend des **unités**.

👉 Impossible de dire si une covariance est “forte” ou “faible”.

---

## Idée clé de la corrélation

> **La corrélation est une covariance rendue sans unité.**

On divise la covariance par les dispersions des deux variables.

---

## Formule de la corrélation de Pearson

$$
r = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}
$$

où :

- (\sigma_X) = écart-type de X
- (\sigma_Y) = écart-type de Y

---

## Propriétés fondamentales

- ( -1 \le r \le 1 )
- r > 0 → lien croissant
- r < 0 → lien décroissant
- r ≈ 0 → pas de lien linéaire

---

## Intuition géométrique (très importante)

> La corrélation mesure **l'alignement** des points.

<img src="https://qi.elft.nhs.uk/wp-content/uploads/2014/08/scatter-plot-31.png" width="800" />

---



<img src="https://www.itl.nist.gov/div898/handbook/eda/section3/gif/scatplo3.gif" width="800" />

---

- nuage aligné → |r| proche de 1
- nuage circulaire → r proche de 0

---

## Corrélation = covariance de données centrées-réduites

Si X et Y sont **centrées-réduites** :

$$
\text{Cov}(X,Y) = r
$$

👉 C'est pour cela que la **corrélation est centrale en ACP**.

---

## Calcul en Python

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 12, 15, 18, 20])

np.corrcoef(x, y)[0, 1]
```

---

## Exercice 1 — Corrélation

```python
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])
```

1. Calculez la corrélation
2. Interprétez le signe et la valeur

```python
# TODO
```

---

## Corrélation ≠ causalité (rappel essentiel)

- forte corrélation ≠ cause
- corrélation mesure **co-variation**, pas mécanisme

👉 Toujours regarder le **contexte** et le **nuage de points**.

---

# PARTIE 2 — MATRICES & COVARIANCE MULTIVARIÉE

---

## Plusieurs variables = matrice de données

$$
X =
\begin{pmatrix}
x_{11} & x_{12} & \dots \
x_{21} & x_{22} & \dots \
\vdots & \vdots & \ddots
\end{pmatrix}
$$

- lignes → individus
-  colonnes → variables

---

## Matrice de covariance

> Généralisation de la variance et de la covariance.

```python
Xc = X - X.mean(axis=0)
Cov = np.cov(Xc, rowvar=False)
```

---

## Lecture de la matrice de covariance

- diagonale → variances
- hors diagonale → covariances
- symétrique

---

## Version normalisée : matrice de corrélation

```python
Corr = np.corrcoef(X, rowvar=False)
```

- diagonale = 1
- valeurs entre −1 et 1

👉 **Base de l'ACP normalisée**

---

# PARTIE 3 — ACP (Analyse en Composantes Principales)

---

## Problème posé par l'ACP

- beaucoup de variables
- variables corrélées
- difficile à visualiser

👉 **résumer l'information sans trop la perdre**

---

## Idée géométrique centrale

> L'ACP cherche **les directions où les données varient le plus**.

<img src="https://www.researchgate.net/publication/320201024/figure/fig1/AS%3A668939172474885%401536498935431/D-scatter-plot-of-principal-component-analysis-PCA-projected-i-vectors-for-different.png" width="700" />


---


![Image](https://miro.medium.com/1%2A_wcd4AGrcovM0m_WypIYtQ.png)

---

## Étape 1 — Centrage (obligatoire)

```python
Xc = X - X.mean(axis=0)
```

---

## Étape 2 — (souvent) Réduction

```python
Xs = Xc / X.std(axis=0)
```

Utilisée quand :

- unités différentes
- échelles incomparables

---

## Étape 3 — Matrice de covariance

```python
Cov = np.cov(Xs, rowvar=False)
```

---

## Étape 4 — Valeurs propres et vecteurs propres

```python
vals, vecs = np.linalg.eig(Cov)
```

### Interprétation

- **vecteurs propres** → directions principales
- ***valeurs propres** → quantité de variance expliquée

---

## Sens géométrique

- vecteur propre = axe de projection
- valeur propre = importance de cet axe

👉 PC1 = direction la plus “longue” du nuage

---

## Étape 5 — Tri par importance

```python
idx = np.argsort(vals)[::-1]
vals = vals[idx]
vecs = vecs[:, idx]
```

---

## Étape 6 — Projection des données

```python
X_proj = Xs @ vecs
```

- nouvelles coordonnées
- mêmes individus
- nouvelles variables : PC1, PC2, …

---

## Exercice 2 — ACP minimale

```python
X = np.array([
    [170, 65],
    [180, 80],
    [160, 55],
    [175, 75]
], dtype=float)
```

1. Centrez les données
2. Calculez la covariance
3. Trouvez PC1
4. Projetez les données

```python
# TODO
```

---

## Combien de composantes garder ?

Variance expliquée :

```python
vals / vals.sum()
```

- PC1 + PC2 ≈ 80–90 % → souvent suffisant

---

## Résumé ACP 

1. L'ACP travaille sur les **corrélations**
2. Elle cherche des **axes optimaux**
3. Elle remplace plusieurs variables par quelques-unes
4. Elle repose sur :

   - matrices
   - valeurs propres
   - vecteurs propres

---

## Résumé global du chapitre

### Corrélation

- covariance normalisée
- sans unité
- base de l'analyse multivariée

---

### ACP

- rotation du nuage
- réduction de dimension
- outil central en data science


---

# Cercle de corrélation

**Interprétation graphique de l'ACP**

---

## Pourquoi le cercle de corrélation ?

Après l'ACP, on a :

- des **individus projetés** (PC1, PC2),
- mais aussi des **variables d'origine**.

👉 Le cercle de corrélation sert à répondre à ces questions :

1. Quelles variables expliquent **PC1** ? **PC2** ?
2. Quelles variables sont **corrélées entre elles** ?
3. Quelles variables sont **indépendantes** ?
4. Quelles variables sont **bien ou mal représentées** ?

---

## Idée clé (à retenir absolument)

> Le cercle de corrélation représente **les corrélations entre les variables d'origine et les axes principaux (PC1, PC2)**.

Ce ne sont **pas les individus**,
ce sont **les variables**.

---

## Pourquoi un cercle de rayon 1 ?

Les données sont **centrées-réduites** :

- variance = 1
- corrélations ∈ [−1, +1]

👉 Les coordonnées des variables sont des **corrélations**
👉 Elles sont donc **bornées par 1**

---

## Schéma conceptuel


<img src="https://www.researchgate.net/publication/328464392/figure/fig5/AS%3A941885082329088%401601574311006/PCA-correlation-circle-variables-points-and-samples-circles-Percent-on-each.png" width="500" />

---

![Image](https://i.sstatic.net/AdtVP.png)

- chaque flèche = une variable
- longueur = qualité de représentation
- angle = corrélation entre variables

---

## Construction mathématique (simple)

Après l'ACP :

- `vecs` = vecteurs propres
- `vals` = valeurs propres

Les coordonnées des variables dans le cercle :

$$
\text{corr}(X_j, PC_k) = \sqrt{\lambda_k} \cdot v_{jk}
$$

En Python :

```python
corr = vecs * np.sqrt(vals)
```

---

## Coordonnées pour PC1–PC2

```python
corr_circle = corr[:, :2]
```

Chaque ligne :

- une variable
- colonne 1 → PC1
- colonne 2 → PC2

---

## Exemple concret

Variables :

- Vitesse
- Force
- Endurance
- Agilité

---

Coordonnées possibles :

| Variable  | PC1  | PC2   |
| --------- | ---- | ----- |
| Vitesse   | 0.85 | 0.10  |
| Force     | 0.88 | 0.05  |
| Endurance | 0.82 | 0.20  |
| Agilité   | 0.60 | −0.60 |

---

## Lecture fondamentale — longueur de la flèche

> Plus une flèche est proche du cercle unité,
> mieux la variable est expliquée par PC1 et PC2.

- proche du cercle → information bien résumée
- proche du centre → information mal captée

---

## Lecture fondamentale — angle entre deux flèches

> L'angle entre deux variables ≈ corrélation entre elles

- angle ≈ 0° → corrélation forte positive
- angle ≈ 180° → corrélation forte négative
- angle ≈ 90° → variables non corrélées

---

## Interprétation visuelle

![Image](https://i.sstatic.net/2pjd8.png)

---

![Image](https://www.researchgate.net/publication/362246632/figure/fig2/AS%3A11431281275524642%401725413786376/Graphical-results-from-the-Principal-Component-Analysis-PCA-a-Variables-factor-map.tif)

---

## Exemple d'interprétation (typique)

1. Vitesse, Force, Endurance :

   - flèches longues
   - même direction
     → **fortement corrélées**
     → expliquent principalement PC1

2. Agilité :

   - orientation différente
   - composante PC2 marquée
     → information complémentaire

---

## Code complet de tracé

```python
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 6))

theta = np.linspace(0, 2*np.pi, 300)
ax.plot(np.cos(theta), np.sin(theta))

ax.axhline(0)
ax.axvline(0)

for i, var in enumerate(variables):
    x, y = corr_circle[i]
    ax.arrow(0, 0, x, y, head_width=0.03, length_includes_head=True)
    ax.text(x*1.1, y*1.1, var)

ax.set_aspect("equal")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_title("Cercle de corrélation")
plt.show()
```

---

## Erreurs fréquentes à éviter

❌ Confondre individus et variables
❌ Interpréter une flèche courte
❌ Oublier le centrage-réduction
❌ Interpréter PC3 sur un cercle PC1–PC2

---

## Exercice 1 — Lecture guidée

On observe un cercle où :

- A et B sont alignées
- C est orthogonale à A
- D est proche du centre

Questions :

1. Quelles variables sont corrélées ?
2. Quelle variable est mal expliquée ?
3. Quelle variable explique PC2 ?

---

## Exercice 2 — Analyse complète

À partir du cercle de corrélation que vous avez obtenu :

1. Identifiez les groupes de variables corrélées
2. Donnez une interprétation de PC1
3. Donnez une interprétation de PC2
4. Proposez un nom à chaque axe

---

## Résumé

1. Le cercle représente les **variables**
2. Les coordonnées sont des **corrélations**
3. Longueur = qualité de représentation
4. Angle = corrélation entre variables
5. PC1 et PC2 résument l'essentiel
