"""10º Escribe un programa que recoja un número y muestre un triángulo formado por
secuencias decrecientes de números impares. Por ejemplo, si se introduce el
5 se debe mostrar:"""

numero = int(input("Introduce un número: "))

for i in range(1, numero + 1):
    print(" ".join(map(str, range(2 * i - 1, 0, -2))))