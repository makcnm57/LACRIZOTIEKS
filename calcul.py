import calcul

# Définir une fonction qui calcule l'exponentielle d'un nombre
def exponentielle(x):
    return calcul.exp(x)

# Exemple d'utilisation
x = float(input("Entrez un nombre pour calculer son exponentielle: "))
resultat = exponentielle(x)
print(f"L'exponentielle de {x} est {resultat}")