# 3. Escribe un programa que lea tres números y que muestre los números mayor
# y menor.

print ("-- Programa que pide 3 números y dice el mayor y el menor --");
# Pedir al usuario los 3 números
numero1 = int(input("Introduce el número1: "));
numero2 = int(input("Introduce el número2: "));
numero3 = int(input("Introduce el número3: "));

# Usando funcion max y min
# numeroMayor = max(numero1, numero2, numero3);
# numeroMenor = min(numero1, numero2, numero3);

# Usando if-else
# Encontrar el número mayor
numeroMayor = 0;
numeroMenor = 0;

if numero1 >= numero2 and numero1 >= numero3:
    numeroMayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    numeroMayor = numero2
else:
    numeroMayor = numero3

# Encontrar el número menor
if numero1 <= numero2 and numero1 <= numero3:
    numeroMenor = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    numeroMenor = numero2
else:
    numeroMenor = numero3

# Muestra el número mayor y el número menor
print ("El número mayor es: ", numeroMayor);
print ("El número menor es: ", numeroMenor);