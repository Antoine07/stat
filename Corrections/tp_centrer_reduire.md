## 1. Analyse des données brutes

* **Maths**

  * moyenne ≈ 11
  * écart-type ≈ 3.55
    → dispersion importante, notes très étalées.

* **Sprint**

  * moyenne ≈ 13.5 s
  * écart-type ≈ 0.75 s
    → dispersion faible, performances plus homogènes.

👉 À ce stade, **toute comparaison directe est invalide** :

* unités différentes,
* amplitudes différentes,
* variabilité différente.

---

## 2. Effet du centrage-réduction

Après transformation :

* moyenne = 0
* écart-type = 1 pour les deux variables

Interprétation immédiate :

* on raisonne en **position relative dans le groupe**
* une valeur indique **combien d’écarts-types** séparent l’observation de la moyenne

Exemple :

* Maths CR = +1.97
  → presque **2 écarts-types au-dessus de la moyenne**
* Sprint CR = −1.89 (avant inversion)
  → performance exceptionnellement bonne (temps très faible)

---

## 3. Lecture observation par observation

* **Étudiant 5**

  * très au-dessus de la moyenne en maths
  * très au-dessus en performance sprint
    → profil d’excellence globale

* **Étudiant 6**

  * nettement en dessous en maths
  * nettement au-dessus en sprint
    → profil contrasté

* **Étudiant 1**

  * faible en maths
  * faible en sprint
    → difficulté relative dans les deux domaines

👉 Ces comparaisons seraient **impossibles** avec les valeurs brutes.

---

## 4. Sens des signes (point clé pédagogique)

Pour le sprint :

* une **valeur brute faible** = bonne performance
* donc une **valeur centrée-réduite négative** = bonne performance

C’est pourquoi on inverse le signe (`-sprint_cr`) pour raisonner en **niveau de performance**.

👉 Cela montre que :

> le centrage-réduction est mathématique, mais l’interprétation reste métier / contexte.

---

## 5. Visualisation comparative

Le graphique montre :

* la position relative de chaque étudiant
* l’écart entre maths et sprint
* la cohérence ou l’opposition des profils

Les segments verticaux matérialisent l’**écart relatif entre disciplines**.

---

## 6. Corrélation

Corrélation ≈ **0.99**

Interprétation :

* très forte relation linéaire
* dans cet échantillon, les étudiants bons en maths sont aussi bons en sprint

⚠️ Important :

* échantillon très petit
* aucune causalité
* simple illustration pédagogique

---

## Conclusion pédagogique synthétique

> Le centrage-réduction transforme des mesures hétérogènes en positions comparables, exprimées en écarts-types, permettant une analyse relative, une comparaison juste et une interprétation fine des profils individuels.

Si vous le souhaitez, je peux proposer :

* une version **QCM**,
* une variante **clustering / PCA**,
* ou un exercice miroir avec une **corrélation faible** pour contraster.

```python
# Exercice corrigé – centrage-réduction et comparaison
# Script prêt à être copié dans un notebook

import numpy as np
import matplotlib.pyplot as plt

# =============================
# Données
# =============================
maths = np.array([8, 10, 9, 14, 18, 7, 11])
sprint = np.array([14.2, 13.5, 13.8, 12.9, 12.1, 14.5, 13.6])

# =============================
# Statistiques descriptives
# =============================
maths_mean = maths.mean()
maths_std = maths.std()

sprint_mean = sprint.mean()
sprint_std = sprint.std()

print("STATISTIQUES BRUTES")
print(f"Maths   : moyenne = {maths_mean:.2f}, écart-type = {maths_std:.2f}")
print(f"Sprint  : moyenne = {sprint_mean:.2f}, écart-type = {sprint_std:.2f}")

# =============================
# Centrage-réduction
# =============================
maths_cr = (maths - maths_mean) / maths_std
sprint_cr = (sprint - sprint_mean) / sprint_std

print("\nSTATISTIQUES APRES CENTRAGE-REDUCTION")
print(f"Maths CR  : moyenne = {maths_cr.mean():.2f}, écart-type = {maths_cr.std():.2f}")
print(f"Sprint CR : moyenne = {sprint_cr.mean():.2f}, écart-type = {sprint_cr.std():.2f}")

# =============================
# Analyse individuelle
# =============================
print("\nANALYSE PAR ETUDIANT")
for i in range(len(maths)):
    print(
        f"Etudiant {i+1} | "
        f"Maths CR = {maths_cr[i]:+.2f} | "
        f"Sprint CR = {sprint_cr[i]:+.2f}"
    )

# =============================
# Inversion du sprint (performance)
# =============================
# Temps faible = bonne performance
sprint_perf_cr = -sprint_cr

# =============================
# Visualisation comparative
# =============================
x = np.arange(len(maths))

plt.figure()
plt.scatter(x, maths_cr, label="Maths (CR)")
plt.scatter(x, sprint_perf_cr, label="Sprint (performance CR)")
plt.vlines(x, maths_cr, sprint_perf_cr)
plt.axhline(0)

plt.xlabel("Etudiant")
plt.ylabel("Ecart à la moyenne (en écart-type)")
plt.title("Comparaison après centrage-réduction")
plt.legend()
plt.show()

# =============================
# Corrélation
# =============================
corr = np.corrcoef(maths_cr, sprint_perf_cr)[0, 1]
print(f"\nCORRELATION Maths / Sprint (performance) = {corr:.2f}")
```