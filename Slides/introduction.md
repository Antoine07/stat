---
marp: true
theme: default
paginate: true
class: lead
---


# Statistiques 

## Centrer les données

```python
temps = np.array([15.2, 15.5, 15.1, 15.3, 15.4, 
                  25.8, 26.1, 25.9, 
                  15.2, 15.3, 15.1])
```

1. Centrez les données 

Méthode: retirer la moyenne des températures aux températures de `temps`.

```python 
# TODO 
```

---

# Questions

1. Que représente maintenant une valeur positive ? Une valeur négative ?

1. Trouvez les températures basses et hautes ?

---

# Jeu de données très simple

On prend deux valeurs :

```python
x = [8, 12]
```

---

# **Centrer**

On enlève la moyenne.

La moyenne vaut :

$$
\mu = \frac{8+12}{2} = 10
$$

---

Données centrées :

$$
x_c = [,8-10,;12-10,] = [-2,; +2]
$$

---

Centrer = déplacer les données pour les ramener autour de 0.
Mais **l'écart entre les valeurs reste le même** (4 unités).

---

# **Réduire**

On divise par l'écart-type :

Écart-type des valeurs `[8, 12]` :

$$
\sigma = 2
$$

---

Réduction :

$$
x_s = \frac{x_c}{\sigma}
= [-2/2,; +2/2]
= [-1,; +1]
$$

---

#  **Interprétation intuitive**

Après réduction, les données deviennent :

```python
[-1, +1]
```

---

### Pourquoi est-ce intéressant ?

1. La **moyenne devient 0**
1. L'**écart-type devient 1**
1. Les valeurs ne s'expriment plus "en unités (km/h, kg, degrés…)"
  mais en **écarts-types par rapport à la moyenne**

Donc :

1. –1 = *une valeur située un écart-type sous la moyenne*
1. +1 = *une valeur située un écart-type au-dessus de la moyenne*

**On ne regarde plus l'unité, mais la position relative.**

---

# Ce que la réduction "corrige" que le centrage seul ne corrige pas

### Exemple :

Données A : `x = [50, 60]`
Données B : `y = [1, 2]`

Si on les centre :

x_c = [-5, +5]
y_c = [-0.5, +0.5]

---

On ne peut **toujours pas** les comparer :
les deux variables ont des amplitudes différentes (10 vs 1).

**La réduction met les deux variables sur la même échelle**,
avec un écart-type de 1.

---

# Résumé pédagogique 

1. **Centrer** → enlever la moyenne → ramener les données autour de 0.
1. **Réduire** → diviser par l'écart-type → mettre les données sur une échelle comparable.
1. Après centrage-réduction :

moyenne = 0
écart-type = 1
les valeurs expriment *combien d'écarts-types elles s'éloignent de la moyenne*.

---

## **Comprendre l'intérêt du centrage-réduction**

On dispose de deux jeux de données mesurés sur les mêmes individus :

1. **Température corporelle (°C)**
2. **Fréquence cardiaque (bpm)**

```python
import numpy as np

temp = np.array([36.8, 37.1, 36.9, 37.5, 38.2, 36.7, 37.0])
heart = np.array([62, 70, 65, 74, 90, 60, 68])
```

---

## Grandeurs 

Les deux grandeurs ne sont **pas du tout sur la même échelle** :

1. la température varie autour de **37°C**,
1. la fréquence cardiaque varie autour de **65–80 bpm**.

Donc on ne peut pas les comparer directement.


Centrez les données

```python
# TODO
```

---

# Questions

1. Que représente maintenant une valeur positive ?
1. Et une valeur négative ?

---

## **Réduire normalisation de l'écart-type**

On divise chaque série centrée par son écart-type, utilisez `np.std`

```python
#TODO temp_scaled et heart_scaled
```
Pourquoi est-il maintenant pertinent de comparer `temp_scaled` et `heart_scaled` ?

Identifier dans chaque série normalisée :

1. les valeurs proches de **0**
1. les valeurs supérieures à **+1**
1. les valeurs inférieures à **–1**

Que peut-on conclure ?

---

## Résumé de la méthode

Les données centrées-réduites ont :

1. **moyenne = 0**
1. **écart-type = 1**
1. les valeurs s'expriment en **écarts-types par rapport à la moyenne**

Ainsi :

1. `+2` signifie : *2 écarts-types au-dessus de la moyenne* → valeur **très atypique**
1. `–1` signifie : *1 écart-type en dessous de la moyenne* → valeur **un peu faible**
1. `0` signifie : *dans la moyenne*

Les deux variables sont maintenant exprimées **sur la même échelle**, donc comparables.
