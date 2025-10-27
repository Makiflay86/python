""" 2. Repite el ejercicio anterior, pero ahora lo que se leen son textos. La condición
de finalización será la cadena vacía. """


def pedirTexto():
    listaTextos = []
    print("Introduce textos (deja vacío y presiona Enter para salir):")
    while True: 
        entrada = input("Texto: ")
        
        if not entrada: 
            break 
        else:
            listaTextos.append(entrada)
            
    return listaTextos


def mostrar_menu():
    """Imprime el menú de opciones."""
    print("\n-- Menú --")
    print("a. En el orden en que se introdujeron.")
    print("b. En orden creciente (alfabético A-Z).")
    print("c. En orden decreciente (alfabético Z-A).")
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





textos = pedirTexto()

if not textos:
    print("\nNo se introdujo ningún texto. Finalizando programa...")
else:
    salir = False
    
    textos_originales = list(textos) 

    while not salir:
        mostrar_menu()
        opcion = leerOpcion()

        print("\n--- Resultado ---")
        if opcion == "d":
            salir = True
        
        elif opcion == "a":
            print("a. En el orden en que se introdujeron:")
            print(" - ".join(textos_originales))
            
        elif opcion == "b":
            textos_creciente = sorted(textos_originales)
            print("b. En orden creciente (A-Z):")
            print(" - ".join(textos_creciente))

        elif opcion == "c":
            textos_decreciente = sorted(textos_originales, reverse=True)
            print("c. En orden decreciente (Z-A):")
            print(" - ".join(textos_decreciente))

        print("-----------------\n")

    print("FINALIZANDO PROGRAMA... ¡Adiós!")