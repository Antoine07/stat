---
marp: true
theme: default
paginate: true
class: lead
---

# Exercices supplémentaires — Centrage & Réduction

---

## Exercice 1 — Centrage simple (calcul manuel)

Soit le jeu de données suivant :

```python
x = np.array([4, 6, 8, 10])
```

1. Calculez la moyenne de `x`
2. Centrez les données
3. Vérifiez que la moyenne des données centrées est nulle

---

## Exercice 2 — Interprétation après centrage

On considère les données centrées suivantes :

```python
x_c = np.array([-3, -1, 0, 2, 2])
```

1. Que signifie une valeur négative ?
2. Que représente la valeur 0 ?
3. Quelle(s) valeur(s) est(sont) la(les) plus éloignée(s) de la moyenne initiale ?

---

## Exercice 3 — Effet du centrage

Soit :

```python
x = np.array([100, 102, 104, 106])
```

1. Centrez les données
2. Comparez l’écart entre les valeurs avant et après centrage
3. Que peut-on conclure sur l’effet du centrage sur la dispersion ?

---

## Exercice 4 — Réduction seule (erreur conceptuelle)

On applique uniquement une division par l’écart-type :

```python
x = np.array([3, 5, 7])
x_r = x / np.std(x)
```

1. La moyenne de `x_r` est-elle nulle ?
2. Pourquoi cette transformation n’est-elle **pas** une vraie normalisation ?
3. Que manque-t-il ?

---

## Exercice 5 — Centrage-réduction complet

Soit :

```python
x = np.array([20, 22, 24, 26, 28])
```

1. Calculez la moyenne et l’écart-type
2. Appliquez le centrage-réduction
3. Vérifiez que la moyenne vaut 0 et l’écart-type vaut 1

---

## Exercice 6 — Comparaison de deux variables

```python
height = np.array([160, 165, 170, 175, 180])
weight = np.array([55, 60, 70, 80, 90])
```

1. Centrez puis réduisez chaque variable
2. Comparez les individus extrêmes
3. Qui est le plus atypique par rapport à son groupe ?

---

## Exercice 7 — Détection de valeurs atypiques

On observe la série centrée-réduite suivante :

```python
z = np.array([-0.4, 0.2, 0.5, 1.8, -2.3])
```

1. Quelles valeurs peuvent être considérées comme atypiques ?
2. Justifiez votre réponse
3. Quelle règle simple peut-on utiliser en pratique ?

---

## Exercice 8 — Centrage-réduction et visualisation mentale

Sans calcul précis, répondez :

1. Une valeur égale à `+3` est-elle courante ou rare ?
2. Une valeur égale à `–0.2` est-elle significativement différente de la moyenne ?
3. Pourquoi parle-t-on d’échelle *universelle* ?

---

## Exercice 9 — Données bruitées

```python
x = np.array([10, 10.2, 9.9, 10.1, 15])
```

1. Appliquez un centrage-réduction
2. Identifiez la valeur aberrante
3. Expliquez comment la normalisation facilite cette détection

---

## Exercice 10 — Cas réel (Machine Learning)

On entraîne un modèle avec deux variables :

* revenu annuel (en €)
* nombre d’achats mensuels

1. Pourquoi le centrage-réduction est-il indispensable avant l’entraînement ?
2. Que se passerait-il sans normalisation ?
3. Citez au moins un algorithme particulièrement sensible à l’échelle des données
