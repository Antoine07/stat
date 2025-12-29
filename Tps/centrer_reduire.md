## Exercice — Comparaison de performances hétérogènes

On observe les résultats de **7 étudiants** à deux épreuves très différentes :

* **Mathématiques** (note sur 20)
* **Temps au 100 m** (en secondes)

```python
import numpy as np

maths = np.array([8, 10, 9, 14, 18, 7, 11])
sprint = np.array([14.2, 13.5, 13.8, 12.9, 12.1, 14.5, 13.6])
```

---

## Partie A — Analyse brute

1. Calculer :

   * la moyenne et l’écart-type des notes de maths
   * la moyenne et l’écart-type des temps au sprint

2. En observant uniquement les valeurs brutes :

   * Peut-on comparer directement les performances en maths et en sprint ?
   * Pourquoi cette comparaison est-elle problématique ?

---

## Partie B — Centrage et réduction

3. Centrer et réduire les deux variables :

   ```python
   maths_cr = (maths - maths.mean()) / maths.std()
   sprint_cr = (sprint - sprint.mean()) / sprint.std()
   ```

4. Vérifier numériquement que :

   * la moyenne de chaque série centrée-réduite est proche de 0
   * l’écart-type est proche de 1

---

## Partie C — Interprétation statistique

5. Pour chaque étudiant :

   * indiquer si sa performance en maths est **au-dessus** ou **en dessous** de la moyenne
   * faire de même pour le sprint

6. Identifier :

   * un étudiant **au-dessus de la moyenne dans les deux disciplines**
   * un étudiant **en difficulté relative dans les deux**
   * un étudiant avec un **profil contrasté**

---

## Partie D — Sens des valeurs centrées-réduites

7. Interpréter les affirmations suivantes :

   a)

   > Un étudiant a une valeur centrée-réduite de +1.5 en maths.

   b)

   > Un étudiant a une valeur centrée-réduite de −1 en sprint.

8. Expliquer pourquoi une valeur centrée-réduite négative en sprint peut correspondre à une **bonne performance**.

---

## Partie E — Comparaison fine

9. Comparer deux étudiants ayant :

   * des notes brutes différentes
   * mais des valeurs centrées-réduites proches

   Que peut-on en conclure sur leur **position relative dans le groupe** ?

10. Calculer la corrélation entre les deux séries centrées-réduites.
    Que dit-elle sur le lien entre réussite scolaire et performance sportive dans cet échantillon ?
