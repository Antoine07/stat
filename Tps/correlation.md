# Exercice – Corrélation et ajustement linéaire 

On considère deux variables numériques `x` et `y`.

```python
import numpy as np
import matplotlib.pyplot as plt
```

---

## Partie A – Relation linéaire

On définit les données suivantes :

```python
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([3, 5, 7, 9, 11, 13, 15, 17, 19])
```

### Questions

1. Tracer le nuage de points ((x, y)).
2. Calculer le coefficient de corrélation linéaire `r`.
3. Interpréter la valeur de `r`.
4. À l'aide de `np.polyfit(x, y, 1)` :

   * déterminer la pente `a`,
   * déterminer l'ordonnée à l'origine `b`.
5. Écrire l'équation de la droite ajustée.
6. Superposer la droite au nuage de points.
7. Expliquer le lien entre :

   * la corrélation obtenue,
   * la forme du nuage,
   * la droite ajustée.

---

## Partie B – Relation non linéaire (piège classique)

On conserve les mêmes valeurs de `x` et on définit :

```python
y2 = x**2
```

### Questions

8. Tracer le nuage de points ((x, y2)).
9. Calculer la corrélation entre `x` et `y2`.
10. La corrélation est-elle élevée ? Pourquoi ?
11. Ajuster une droite avec `np.polyfit(x, y2, 1)` et tracer-la.
12. La droite est-elle un bon modèle ? Justifier.
13. Que conclure sur le lien entre corrélation élevée et relation linéaire ?

---

## Partie C – Comparaison des modèles

14. Ajuster maintenant un polynôme de degré 2 :

```python
np.polyfit(x, y2, 2)
```

15. Comparer visuellement :

* le modèle linéaire (degré 1),
* le modèle quadratique (degré 2).

16. Quel modèle est le plus pertinent pour `y2` ? Pourquoi ?

---

## Partie D – Question de synthèse (rédaction)

17. Compléter les phrases suivantes :

* La corrélation mesure uniquement un lien __________.
* Une corrélation élevée n'implique pas forcément une relation __________.
* `np.polyfit(x, y, 1)` ajuste une __________.
* Le paramètre `1` correspond au __________ du polynôme.

---

## Indications attendues (sans calcul)

* Partie A : corrélation proche de +1, droite très pertinente.
* Partie B : corrélation élevée mais relation non linéaire.
* Partie C : le modèle quadratique explique la courbure.
* Conclusion : **toujours tracer les données avant d'interpréter la corrélation**.

---

## Phrase clé à retenir (objectif pédagogique)

> La corrélation mesure l'alignement linéaire des données, pas la forme réelle de la relation.
