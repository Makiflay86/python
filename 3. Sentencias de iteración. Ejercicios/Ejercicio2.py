"""2º Escribe un programa que recoja un número y calcule su factorial."""

numero = int(input("Introduce un número: "));
# 1. Manejar casos base 0 y 1.
if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0 or numero == 1:
    factorial = 1
    print(f"El factorial de {numero} es: {factorial}")
else:
    # 2. Inicializar el factorial a 1 para la multiplicación.
    factorial = 1
    # 3. Iterar desde 1 hasta el número (inclusive).
    for i in range(1, numero + 1):
        # 4. Multiplicar el factorial acumulado por el número actual (i).
        print (f"{factorial} x {i} = {factorial * i}")
        factorial *= i
    
    print (f"El factorial de {numero} es: {factorial}")