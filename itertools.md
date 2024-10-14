# Fonctions Itertools en Python

Ce document présente un aperçu de quatre fonctions puissantes du module `itertools` de Python : `product()`,
`permutations()`, `combinations()`, et `combinations_with_replacement()`.

## Table des matières

1. [product()](#product)
2. [permutations()](#permutations)
3. [combinations()](#combinations)
4. [combinations_with_replacement()](#combinations_with_replacement)

## product()

La fonction `product()` calcule le produit cartésien des itérables d'entrée.

### Utilisation

```python
from itertools import product

resultat = product('ABCD', repeat=2)
# result = product('ABCD', 'ABCD')
```

### Exemple

```python
print(' '.join(''.join(p) for p in product('ABCD', repeat=2)))
# Sortie : AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
```

### Explication

Cette fonction génère toutes les combinaisons possibles en répétant les éléments. Dans ce cas, elle produit toutes les
combinaisons de deux lettres où chaque lettre peut être utilisée plusieurs fois.

## permutations()

La fonction `permutations()` génère toutes les permutations possibles d'une longueur spécifiée à partir d'un itérable.

### Utilisation

```python
from itertools import permutations

resultat = permutations('ABCD', 2)
```

### Exemple

```python
print(' '.join(''.join(p) for p in permutations('ABCD', 2)))
# Sortie : AB AC AD BA BC BD CA CB CD DA DB DC
```

### Explication

Cette fonction génère toutes les façons de choisir 2 éléments où l'ordre importe, sans répétition.

## combinations()

La fonction `combinations()` génère toutes les combinaisons possibles d'une longueur spécifiée à partir d'un itérable.

### Utilisation

```python
from itertools import combinations

resultat = combinations('ABCD', 2)
```

### Exemple

```python
print(' '.join(''.join(c) for c in combinations('ABCD', 2)))
# Sortie : AB AC AD BC BD CD
```

### Explication

Cette fonction génère toutes les façons de choisir 2 éléments où l'ordre n'importe pas, sans répétition.

## combinations_with_replacement()

La fonction `combinations_with_replacement()` génère toutes les combinaisons possibles d'une longueur spécifiée à partir
d'un itérable, en permettant la répétition.

### Utilisation

```python
from itertools import combinations_with_replacement

resultat = combinations_with_replacement('ABCD', 2)
```

### Exemple

```python
print(' '.join(''.join(c) for c in combinations_with_replacement('ABCD', 2)))
# Sortie : AA AB AC AD BB BC BD CC CD DD
```

### Explication

Similaire à `combinations()`, mais permet de répéter les éléments (ex : AA).

---


# Résumé

```python
product() : Génère toutes les combinaisons possibles, avec répétition. C'est comme un "et" entre chaque élément.
permutations() : Génère tous les arrangements possibles, où l'ordre compte, sans répétition.
combinations() : Génère toutes les combinaisons possibles, où l'ordre ne compte pas, sans répétition.
combinations_with_replacement() : Comme combinations(), mais permet la répétition des éléments.
```