from itertools import product

result = product('AB', 'XY')
print(list(result))
# Sortie: [('A', 'X'), ('A', 'Y'), ('B', 'X'), ('B', 'Y')]
# génère toutes les paires possibles où le premier élément vient de 'AB' et le second de 'XY'.