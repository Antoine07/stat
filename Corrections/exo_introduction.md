## Correction Exercice 1 — Centrage simple

```python
x = np.array([4, 6, 8, 10])
mu = np.mean(x)          # 7
x_c = x - mu             # [-3, -1, 1, 3]
np.mean(x_c)             # 0
```

* Moyenne : (\mu = (4+6+8+10)/4 = 7)
* Données centrées : ([-3, -1, +1, +3])
* Vérification : moyenne = 0

---

## Correction Exercice 2 — Interprétation après centrage

```python
x_c = np.array([-3, -1, 0, 2, 2])
```

* Valeur négative : en dessous de la moyenne initiale
* Valeur 0 : exactement la moyenne initiale
* Plus éloignées : `-3` et `2` (distance 3 vs 2), donc **-3** est la plus éloignée

---

## Correction Exercice 3 — Effet du centrage

```python
x = np.array([100, 102, 104, 106])
mu = np.mean(x)          # 103
x_c = x - mu             # [-3, -1, 1, 3]
```

* Écarts avant : 106−100 = 6
* Écarts après : 3−(−3) = 6
* Conclusion : le centrage **ne change pas la dispersion**, il translate juste les valeurs autour de 0.

---

## Correction Exercice 4 — Réduction seule (erreur conceptuelle)

```python
x = np.array([3, 5, 7])
x_r = x / np.std(x)
np.mean(x_r)  # ≠ 0
```

1. La moyenne n’est **pas nulle** car on n’a pas retiré la moyenne.
2. Ce n’est pas une normalisation centrée-réduite : on ne fait que changer l’échelle.
3. Il manque le **centrage** :

```python
z = (x - np.mean(x)) / np.std(x)
```

---

## Correction Exercice 5 — Centrage-réduction complet

```python
x = np.array([20, 22, 24, 26, 28])
mu = np.mean(x)          # 24
sigma = np.std(x)        # ≈ 2.828 (si ddof=0)
z = (x - mu) / sigma
np.mean(z)               # ≈ 0
np.std(z)                # ≈ 1
```

* Moyenne = 24
* Écart-type (population) ≈ 2.828
* Résultat : ([-1.414, -0.707, 0, 0.707, 1.414]) (approx.)

---

## Correction Exercice 6 — Comparaison de deux variables

```python
height = np.array([160, 165, 170, 175, 180])
weight = np.array([55, 60, 70, 80, 90])

h_z = (height - np.mean(height)) / np.std(height)
w_z = (weight - np.mean(weight)) / np.std(weight)
```

Interprétation :

* `height` est régulier (progression uniforme)
* `weight` est plus dispersé (55 à 90)

En z-scores, l’individu le plus atypique est généralement l’extrême (180 pour taille, 90 pour poids) mais **celui du poids** ressort souvent davantage car la série est plus étalée et moins symétrique selon la distribution (ici, typiquement 55 et 90 sont les plus éloignés en z-score).

Pour trancher : comparer `abs(h_z)` et `abs(w_z)`.

---

## Correction Exercice 7 — Valeurs atypiques

```python
z = np.array([-0.4, 0.2, 0.5, 1.8, -2.3])
```

* Atypiques : souvent (|z| > 2)
* Donc : **-2.3** est atypique (et 1.8 est élevé mais pas “outlier” selon seuil 2)

Règle simple :

* atypique si (|z| > 2) (ou (|z| > 3) en règle stricte)

---

## Correction Exercice 8 — Visualisation mentale

1. `+3` : très rare (3 écarts-types au-dessus de la moyenne)
2. `-0.2` : très proche de la moyenne (écart faible, pas significatif en pratique)
3. “Universelle” : car on exprime tout en **écarts-types**, indépendamment des unités.

---

## Correction Exercice 9 — Données bruitées

```python
x = np.array([10, 10.2, 9.9, 10.1, 15])
mu = np.mean(x)
sigma = np.std(x)
z = (x - mu) / sigma
z
```

* La valeur aberrante est **15**
* Après normalisation, 15 aura un z-score nettement plus élevé que les autres.
* Normaliser aide car tout est mis sur une échelle comparable : une valeur très éloignée apparaît immédiatement via (|z|).
