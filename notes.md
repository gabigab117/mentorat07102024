## Ex 1

Opa est une chaîne aléatoire très longue, composée de plus de dix millions de caractères.

Parmi les opérations suivantes, laquelle est la plus lente ?
a.strip()

a[::-1]

sorted(a) celle ci, on parcourt et trie tous les caractères de a

a.upper()

- Parcours les caractères de a et les trie en ordre croissant. sorted(a) est la plus lente car elle a une complexité
  O(n*log(n)), où n est la longueur de la chaîne a. Les autres opérations ont une complexité linéaire O(n), où n est la
  longueur de la chaîne a.


## Ex 2

Parmi les expressions suivantes, lesquelles définissent un set?
{1, 2, 3} oui

{1: 1, 2: 2, 3: 3}

{}

set() oui

[1, 2, 3]

(1, 2, 3)


## Ex 3

Revenir sur itertools
https://docs.python.org/fr/3.10/library/itertools.html


## Ex 5

Laquelle (ou lesquelles) des réponses suivantes affiche(nt) +*-*** ?

print('+', '-', '**', sep='*', end='') oui

for x in ['+', '-', '*']: oui

print(x, end='*')

print(['+*-', '***'], end='') non

print('+*', '-*', end='**', sep='') oui


# Ex 6

Parmi les opérations suivantes, quelles sont celles dont le temps d'exécution dépend de la taille de l'ensemble s (qui
ont une complexité O(len(s))) ?

s et v sont deux ensembles de longueur similaire

element est un élément de l'ensemble s

s.pop() # temps constant, élément random

element in set # temps constant

s == v # On parcourt tout les éléments de s et v


# Ex 7

Définissez la méthode get_status() dans la classe Boat, de sorte qu'elle renvoie les données recueillies par la méthode
parente Vehicle.get_status() et l'attribut floatability de l'instance Boat. Ce champ sera stocké à la clé floatability
du dict status.

L'implémentation devra rester correcte même si le contenu du dict retourné par Vehicle.get_status() change dans le
futur.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return "Véhicule de marque %s" % self.brand

    def get_status(self) -> dict:
        return dict(brand=self.brand,
                    condition="good")


class Boat(Vehicle):

    def __init__(self, brand, floatability):
        super().__init__(brand)
        self.floatability = floatability

    # ----------NE MODIFIEZ PAS LE CODE AU DESSUS DE CETTE LIGNE, IL SERA REINITIALISE LORS DE l'EXECUTION----------
    def get_status(self):
        status = super().get_status()  # Récupérer le status de la classe parente
        status['floatability'] = self.floatability  # On ajoute la nouvelle clé sans modifier le dict de la classe parente
        return status  # Même si Vehicule get status est modifié ça fonctionne
# ----------NE MODIFIEZ PAS LE CODE EN DESSOUS DE CETTE LIGNE, IL SERA REINITIALISE LORS DE l'EXECUTION----------
```