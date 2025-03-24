def addition(x, y):
  """Additionne deux nombres."""
  return x + y

def soustraction(x, y):
  """Soustrait deux nombres."""
  return x - y

def multiplication(x, y):
  """Multiplie deux nombres."""
  return x * y

def division(x, y):
  """Divise deux nombres."""
  return x / y

print("Sélectionnez l'opération.")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

while True:
  choix = input("Entrez le choix(1/2/3/4): ")

  if choix in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Entrez le premier nombre: "))
      num2 = float(input("Entrez le deuxième nombre: "))
    except ValueError:
      print("Entrée invalide. Veuillez entrer des nombres.")
      continue

    if choix == '1':
      print(num1, "+", num2, "=", addition(num1, num2))

    elif choix == '2':
      print(num1, "-", num2, "=", soustraction(num1, num2))

    elif choix == '3':
      print(num1, "*", num2, "=", multiplication(num1, num2))

    elif choix == '4':
      if num2 == 0:
        print("On ne peut pas diviser par zéro.")
      else:
        print(num1, "/", num2, "=", division(num1, num2))
    break
  else:
    print("Entrée invalide. Veuillez entrer un nombre entre 1 et 4.")
