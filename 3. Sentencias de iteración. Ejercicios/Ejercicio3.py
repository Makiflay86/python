"""3º Escribe un programa que recoja números por teclado hasta que se introduzca
el valor cero. A continuación, debe mostrar el número de valores introducidos,
el valor mínimo introducido, el máximo, la suma de todos ellos y su media
aritmética (todos los cálculos sin contar el cero)"""

# 1. Inicializar una lista vacía para almacenar los números.
valores_introducidos = []
entrada = -1 # Inicializamos con un valor distinto de 0

# 2. Bucle para recoger números hasta que se introduzca el 0.
while entrada != 0:
    try:
        entrada = int(input("Introduce un número (0 para salir): "))
        
        # 3. Guardar el número si no es cero.
        if entrada != 0:
            valores_introducidos.append(entrada)
            
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")

# 4. Procesar los resultados (sin contar el 0).
print("\n--- Resultados ---")

if not valores_introducidos:
    print("No se introdujo ningún número para analizar (aparte del cero inicial).")
else:
    # A. Número de valores introducidos (sin el 0)
    conteo = len(valores_introducidos)
    
    # B. Valor mínimo
    minimo = min(valores_introducidos)
    
    # C. Valor máximo
    maximo = max(valores_introducidos)
    
    # D. Suma de todos ellos
    suma = sum(valores_introducidos)
    
    # E. Media aritmética
    media = suma / conteo
    
    print(f"Número de valores introducidos: {conteo}")
    print(f"Valor mínimo introducido: {minimo}")
    print(f"Valor máximo introducido: {maximo}")
    print(f"Suma de todos los valores: {suma}")
    # Formatear la media a dos decimales
    print(f"Media aritmética: {media:.2f}")