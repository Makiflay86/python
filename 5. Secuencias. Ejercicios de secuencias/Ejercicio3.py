""" 3. Escribe un programa lea un texto y determine si es un palíndromo. Procura
crear una función palindromo(s) -> Bool. """


import string

def palindromo(s: str) -> bool:
    s_limpia = s.lower()
    tabla_limpieza = str.maketrans('', '', string.punctuation + ' ')
    s_procesada = s_limpia.translate(tabla_limpieza)
    s_reversa = s_procesada[::-1]
    
    return s_procesada == s_reversa




print("--- Comprobador de Palíndromos ---")

texto_entrada = input("Introduce un texto: ")

es_palindromo = palindromo(texto_entrada)

print("-" * 35)

if es_palindromo:
    print(f"¡El texto \"{texto_entrada}\" ES un palíndromo!")
else:
    print(f"El texto \"{texto_entrada}\" NO es un palíndromo.")