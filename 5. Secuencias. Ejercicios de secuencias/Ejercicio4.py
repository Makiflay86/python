""" 4. Escribe un programa que lea dos textos y compruebe si una es palíndromo de
la otra. El programa debe preguntar si se desea comprobar teniendo en cuenta
mayúsculas/minúsculas o no. """


import string

def es_palindromo_de(texto1: str, texto2: str, ignorar_mayus: bool) -> bool:
    
    tabla_limpieza = str.maketrans('', '', string.punctuation + ' ')
    
    s1_procesada = texto1.translate(tabla_limpieza)
    s2_procesada = texto2.translate(tabla_limpieza)
    
    if ignorar_mayus:
        s1_final = s1_procesada.lower()
        s2_final = s2_procesada.lower()
    else:
        s1_final = s1_procesada
        s2_final = s2_procesada
        
    s1_reversa = s1_final[::-1]
    
    return s1_reversa == s2_final





print("--- Comprobador de Palíndromo (Texto A vs. Texto B) ---")

texto_a = input("Introduce el Texto A: ")
texto_b = input("Introduce el Texto B: ")

while True:
    opcion = input("¿Desea ignorar mayúsculas/minúsculas? (S/N): ").lower()
    if opcion in ('s', 'si'):
        ignorar_mayusculas = True
        break
    elif opcion in ('n', 'no'):
        ignorar_mayusculas = False
        break
    else:
        print("Opción no válida. Por favor, introduce S (Sí) o N (No).")

print("-" * 50)

resultado = es_palindromo_de(texto_a, texto_b, ignorar_mayusculas)



if resultado:
    print(f"¡El Texto A es el palíndromo del Texto B!")
else:
    print(f"El Texto A NO es el palíndromo del Texto B.")

if ignorar_mayusculas:
    print("   (La comprobación IGNORA la diferencia entre mayúsculas y minúsculas.)")
else:
    print("   (La comprobación DISTINGUE entre mayúsculas y minúsculas.)") 
