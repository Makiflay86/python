# 1. Escribe un programa que recoja un número e indique si se trata de un número
# par o impar.

print ("-- Programa que dice si un número es par o impar --");
#Pedimos al usuario un número.
numero = int(input("Introduce un número: "));

# Muestra si es par o impar
# Opción 1
'''if numero % 2 == 0:
    print("El número",numero,"es par")
else:
    print("El número",numero,"es impar")'''

# Opción 2
'''if numero % 2 == 0:
    print("El número {} es par".format(numero))
else:
    print("El número {} es impar".format(numero))'''

# Opción 3
'''if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")'''

# Opción 4
if numero % 2 == 0:
    print("El número %d es par"%numero);
else:
    print("El número %d es impar"%numero);