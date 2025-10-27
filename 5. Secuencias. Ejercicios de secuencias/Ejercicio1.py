""" 
    1. Escribe un programa que recoja números de teclado hasta que se introduce un
    cero. Luego debe mostrar la secuencia de números de tres modos:
    a. En el orden en que se introdujeron.
    b. En orden creciente.
    c. En orden decreciente.
 """


def pedirNumero():
    listaNumero = []
    while True: 
        try:
            entrada = input("Introduce un número (0 => salir): ")
            numero = int(entrada)
            if numero == 0:
                break 
            else:
                listaNumero.append(numero)
        except ValueError: 
            print("ERROR: Debes introducir un número entero.")
            print("")
    return listaNumero


def mostrar_menu():
    """Imprime el menú de opciones."""
    print("\n-- Menú --")
    print("a. En el orden en que se introdujeron.")
    print("b. En orden creciente.")
    print("c. En orden decreciente.")
    print("d. Salir.")


def leerOpcion():
    """Pide y valida la opción del menú."""
    opciones_validas = set("abcd")
    while True:
        opcion = input("Opción: ").lower()
        if opcion in opciones_validas:
            return opcion
        else:
            print("ERROR: Opción incorrecta (a-d).")
            print("")


numeros = pedirNumero()

if not numeros:
    print("\nNo se introdujo ningún número. Finalizando programa...")
else:
    salir = False
    
    numeros_originales = list(numeros) 

    while not salir:
        mostrar_menu()
        opcion = leerOpcion()

        print("\n--- Resultado ---")
        if opcion == "d":
            salir = True
        
        elif opcion == "a":
            print("a. En el orden en que se introdujeron:")
            print(*numeros_originales)
            
        elif opcion == "b":
            numeros_creciente = sorted(numeros_originales)
            print("b. En orden creciente:")
            print(*numeros_creciente)

        elif opcion == "c":
            numeros_decreciente = sorted(numeros_originales, reverse=True)
            print("c. En orden decreciente:")
            print(*numeros_decreciente)

        print("-----------------\n")

    print("FINALIZANDO PROGRAMA...")
    






