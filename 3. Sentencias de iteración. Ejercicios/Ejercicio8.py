"""8º Escribe un programa que recoja un número y calcule si es primo."""

import math

numero = int(input("Introduce un número: "))
resultado = ""
es_primo = True
divisor_encontrado = None

if numero < 2:
    es_primo = False
    resultado = "El número NO es primo. Debe ser un entero positivo mayor o igual a 2."
elif numero >= 2: 
    if numero % 2 == 0 and numero > 2:
        es_primo = False
        divisor_encontrado = 2
        resultado = f"El número NO es primo (es divisible por {divisor_encontrado})."
    else:
        limite = math.isqrt(numero)
        
        for divisor in range(3, limite + 1, 2):
            if es_primo: 
                if numero % divisor == 0:
                    es_primo = False
                    divisor_encontrado = divisor
                    resultado = f"El número NO es primo (es divisible por {divisor_encontrado})."

if es_primo and not resultado:
    resultado = "El número es primo."



print(resultado)