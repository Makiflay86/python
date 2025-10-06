"""4º Escribe un programa que recoja un número y muestre un triángulo. Por
    ejemplo, si se ha introducido el valor 5, se debe mostrar:"""

numero = int(input("Introduce un número: "));

for i in range(numero):
    for j in range(i+1):
        print("*", end="")
    print()
