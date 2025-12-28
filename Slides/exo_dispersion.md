# Exercices supplémentaires — Statistiques descriptives

---

## Exercice 1 — Lecture de statistiques

On considère la série suivante :

```python
data = np.array([5, 7, 9, 10, 10, 11, 14])
```

1. Calculez la moyenne, la médiane et l'écart-type
2. Quelle mesure décrit le mieux la valeur “typique” ?
3. Justifiez votre choix

```python
# TODO
```

---

## Exercice 2 — Sensibilité aux valeurs extrêmes

```python
A = np.array([10, 11, 11, 12, 12])
B = np.array([10, 11, 11, 12, 50])
```

1. Comparez moyenne et médiane
2. Quelle série est la plus représentative de son centre ?
3. Quelle mesure est la plus robuste ici ?

```python
# TODO
```

---

## Exercice 3 — Quartiles et dispersion

```python
data = np.array([2, 4, 5, 6, 7, 9, 10, 12])
```

1. Calculez Q1, Q2, Q3
2. Calculez l'IQR
3. Interprétez la dispersion de la série

```python
# TODO
```

---

## Exercice 4 — Étendue vs écart-type

```python
A = np.array([10, 10, 10, 20])
B = np.array([5, 11, 12, 12])
```

1. Calculez l'étendue pour A et B
2. Calculez l'écart-type pour A et B
3. Expliquez pourquoi ces deux mesures ne racontent pas la même chose

```python
# TODO
```

---

## Exercice 5 — Analyse graphique d'un histogramme

```python
data = np.array([3, 4, 5, 5, 6, 7, 8, 20])
```

1. Tracez l'histogramme
2. Décrivez la forme de la distribution
3. Reliez votre analyse à la moyenne et à la médiane

```python
# TODO
```

---

## Exercice 6 — Boxplot et valeurs atypiques

```python
data = np.array([10, 11, 12, 12, 13, 13, 14, 30])
```

1. Tracez le boxplot
2. Calculez Q1, Q3 et l'IQR
3. Identifiez les valeurs atypiques
4. Comparez avec la règle des 2 écarts-types

```python
# TODO
```

---

## Exercice 7 — Asymétrie et interprétation

```python
A = np.array([8, 9, 10, 11, 12])
B = np.array([8, 9, 10, 11, 25])
```

1. Comparez moyenne et médiane
2. Calculez la skewness
3. Identifiez le type d'asymétrie
4. Interprétez en contexte réel possible

```python
# TODO
```

---

## Exercice 8 — Concentration des données

```python
A = np.random.normal(50, 5, 1000)
B = np.random.normal(50, 15, 1000)
```

1. Comparez écart-type et kurtosis
2. Quelle distribution est la plus concentrée ?
3. Quelle est la plus susceptible de produire des valeurs extrêmes ?

```python
# TODO
```

---

## Exercice 9 — Comparaison de groupes

```python
groupe_A = np.array([12, 13, 14, 15, 16])
groupe_B = np.array([10, 11, 12, 18, 25])
```

1. Comparez moyenne, médiane, écart-type
2. Tracez boxplots et histogrammes
3. Quelle comparaison est la plus fiable ? Pourquoi ?

```python
# TODO
```

---

## Exercice 10 — Analyse critique complète

```python
data = np.array([6, 7, 7, 8, 9, 9, 10, 25])
```

Réalisez une analyse complète :

1. Statistiques descriptives
2. Histogramme et boxplot
3. Forme de la distribution
4. Présence de valeurs atypiques
5. Conclusion synthétique (5 lignes max)

```python
# TODO
```
