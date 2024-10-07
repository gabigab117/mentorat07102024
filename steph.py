# Le but est de créer un script permettant de remplir une liste d'aliments
# Il faut donc créer une boucle qui s'arrêtera lorsque l'utilisateur entrera "quit"

# D'abord on crée la liste qui accueillera les aliments
foods = []

# Ensuite on créer une boucle while qui s'arrêtera lorsque l'utilisateur entre "quit"
while True:
    # on demande à l'utilisateur d'enter un aliment
    food = input("Entrez un aliment: ")
    # on vérifie que la valeur entrée par l'utilisateur est déférente de "quit"
    if food == "quit":
        # on quitte la boucle
        break
    # Sinon on ajoute l'élément à la liste
    foods.append(food)

# Solution avec walrus
while (food := input("Entrez un aliment: ")) != "quit":
    foods.append(food)
