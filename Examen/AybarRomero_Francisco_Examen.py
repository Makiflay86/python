""" EXAMEN """


def menu():
    print("")
    print("-- MENú DE OPCIONES --")
    print("a) Listado de teléfonos, usando el orden por defecto.")
    print("b) Listado de teléfonos por orden alfabético.")
    print("c) Añadir un nuevo contacto.")
    print("d) Modificar el teléfono de un contacto.")
    print("e) Buscar un número de teléfono.")
    print("f) Eliminar un contacto.")
    print("g) Borrar el listín telefónico.")
    print("h) Salir")



def opcion():
    salir = False
    while not salir:
        try:
            op = input("Opción: ")

            match op:
                case "a":
                    salir = False
                    
                case "b":
                    salir = False

                case "c":
                    salir = False

                case "d":
                    salir = False
                
                case "e":
                    salir = False
                
                case "f":
                    salir = False

                case "g":
                    salir = False

                case "h":
                    salir = True
                
                case _:
                    print("ERROR: No es una opción válida.")
                    print("")
                    input("Pulsa enter para continuar...")        
                    salir = False

    
            return salir
        except ValueError:
            print("ERROR: Ocurrió un problema inesperado.")



salir = False;

while not salir:
    menu()
    
    if not opcion():
        salir = False
    else:
        salir = True

else:
    print("")
    print("FINALIZANDO PROGRAMA...")

