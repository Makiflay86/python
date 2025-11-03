""" DICIONARIOS """
""" Crea un programa que utilice un diccionario para crear un listín telefónico. El
diccionario estará formado por pares (nombre, teléfono). """


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



def listado():
    print("")
    print("-- Listado de nombres y sus teléfonos --")
    for nombre, telefono in lista.items():
        print(f"Nombre: {nombre} - Teléfono: {telefono}")

    print("")
    input("Pulsa enter para continuar...")
    return False



def listadoAZ():
    print("")
    print("-- Listado de nombres y sus teléfonos (A-Z) --")
    for nombre in sorted(lista, key=lambda x: x[0].lower()): # El key=lamba sirve para ordenar la lista ignorando las mayusculas, porque le asigna a la letra inicial en minúscula (lower())
        print(f"Nombre: {nombre} - Teléfono: {lista[nombre]}")

    print("")
    input("Pulsa enter para continuar...")
    return False



lista = {}
def addUser():
    salir = False
    while not salir:
        try:
            print("")
            print("-- Datos del usuario --")
            nombre = input("Introduce su nombre: ")
            telefono = input("Introduce su teléfono: ")

            if nombre in lista:
                print("WARNING: Ya existe este usuario con ese teléfono")
                actualizar = input("¿Quieres actualizar su número de teléfono? (S/N)").upper()
                if (actualizar == "S"):
                    lista[nombre] = telefono
                    print("Teléfono modificado.")
                    print("")
                    input("Pulsa enter para continuar...")
                    salir = True
                else:
                     print("Usuario no añadido porque ya existe y tampoco se le cambió el número de teléfono.")   
                     print("")
                     input("Pulsa enter para continuar...")
                     salir = True
            else:
                lista[nombre] = telefono
                print("Añadiendo usuario... Usuario añadido")
                print("")
                input("Pulsa enter para continuar...")
                salir = True

        except ValueError:
            salir = False
            print("ERROR: Nombre de usuario o teléfono incorrecto.")

    return False



def modTelef():
    print("")
    print("-- Modificar el número de teléfono --")
    nombre = input("Introduce el nombre: ")
    telefono = input("Introduce el teléfono: ")

    if (nombre in lista):
        lista[nombre] = telefono
        print("Teléfono modificado.")
        print("")
        input("Pulsa enter para continuar...")
    else:
        print("WARNING: No existe el usuario.")
        add = input("¿Quieres añadirlo? (S/N) ").upper()
        if (add == "S"):
            lista[nombre] = telefono
            print("Usuario añadido.")
        else:
            print("Usuario no añadido.")

        print("")
        input("Pulsa enter para continuar...")
            
    return False



def searchTelef():
    print("")
    print("-- Buscar contacto por número de teléfono --")
    telefono = input("Introduce el número de teléfono: ")

    encontrado = False
    for nombre, numero in lista.items():
        if (numero == telefono):
            print(f"El número pertenece a: {nombre}")
            encontrado = True
            break

    if not encontrado:
        print("No se ha encontrado ningún contacto con ese número.")

    print("")
    input("Pulsa enter para continuar...")

    return False



def delUser():
    print("")
    nombre = input("¿Qué usuario quieres eliminar? ")

    if (nombre in lista):
        print(f"El usuario '{nombre}' a sido eliminado.")
        del lista[nombre]
    else:
        print("No se ha encontrado ningún usuario con ese nombre.")

    print("")
    input("Pulsa enter para continuar...")

    return False



def delListTelef():
    print("")
    borrar = input("¿Seguro que quieres eliminar todos los teléfonos? (S/N) ").upper()
    if (borrar == "S"):
        lista.clear()
        print("Eliminando todos los teléfonos...")
    else:
        print("Vale, no elimino nada :P.")
        
    print("")
    input("Pulsa enter para continuar...")

    return False



def opcion():
    salir = False
    while not salir:
        try:
            op = input("Opción: ")

            match op:
                case "a":
                    salir = listado()
                    
                case "b":
                    salir = listadoAZ()

                case "c":
                    salir = addUser()

                case "d":
                    salir = modTelef()
                
                case "e":
                    salir = searchTelef()
                
                case "f":
                    salir = delUser()

                case "g":
                    salir = delListTelef()

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

