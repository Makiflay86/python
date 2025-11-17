class Persona:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def toString(self):
        print(f"Nombre: {self.nombre} Dirección: {self.direccion} Teléfono: {self.telefono}.")



""" Diccionario para los contactos, tiene contactos de ejemplo """
contactos = {}
contactos["FRANCISCO"] = Persona("FRANCISCO", "oefjw32 32 r2oij", "632341223")
contactos["AITOR"] = Persona("AITOR", "jaen linaejioej 3rr", "23622545")
contactos["MARIO"] = Persona("MARIO", "santani3or20r dwefw", "523453423")
    


""" Creo el objeto persona p1 y le asigno valores """
p1 = Persona("Francisco", "MI CASA", "123321"); 

""" Llamo la función toString() del objeto Persona p1 """
p1.toString(); 






""" Ejercicio """

""" Listar los contacto de la A-Z """
def listarContactosAZ():
    if not contactos:
        print("ERROR: No existe ningún contacto.")
    else:
        for nombre in sorted(contactos.keys()):
            contactos[nombre].toString()
        
    print("")
    input("Pulsa [ENTER] para continuar...")
    
    return False



""" Añadir un contacto """
def addContacto():
    salir = False
    while not salir:
        try:
            nombre = input("Introduce el nombre: ").strip().upper()
            direccion = input("Introduce la direccion: ").strip()
            telefono = input("Introduce el telefono: ").strip()

            clave = nombre

            if clave in contactos:
                print("WARNING: El contacto ya existe.")
                print("")
                salir = False
            else:
                contactos[clave] = Persona(nombre, direccion, telefono)
                print("Añadiendo contacto...")
                print("")
                input("Pulsa [ENTER] para continuar...")
                salir = True

        except ValueError:
            print("ERROR: Ha ocurrido un error inesperado.")
            print("")
            input("Pulsa [ENTER] para continuar...")
            salir = False

    return False



""" Modificar un contacto """
def modContacto():
    try:
        contacto = input("¿Qué contacto quieres modificar? ").upper()
        if not contacto in contactos:
            print("ERROR: No existe ningún contacto.")
        else:
            salir = False
            while not salir:
                print("¿Qué quieres modificar?")
                print("1. Dirección")
                print("2. Teléfono")
                opcionMod = int(input("Opción: ").strip())

                if opcionMod == 1:
                    print("")
                    direccion = input("Introduce la nueva dirección: ").strip()
                    contactos[contacto].direccion = direccion
                    print("Dirección modificada correctamente.")
                    salir = True
                elif opcionMod == 2:
                    print("")
                    telefono = input("Introduce el nuevo teléfono: ").strip()
                    contactos[contacto].telefono = telefono
                    print("Teléfono modificado correctamente.")
                    salir = True
                else:
                    print("WARNING: Opción no válida.")
                    print("")
                    salir = False

        print("")
        input("Pulsa [ENTER] para continuar...")

    except ValueError:
        print("ERROR: Ha ocurrido un error inesperado.")
        print("")
        input("Pulsa [ENTER] para continuar...")
    
    return False



""" Buscar un contacto a partir de su teléfono """
def searchTelf():
    try:
        if not contactos:
            print("ERROR: No existe ningún contacto.")
        else:
            telefono = input("Introduce el teléfono: ").strip()
            encontrado = False

            for persona in contactos.values():
                if persona.telefono == telefono:
                    print(f"El teléfono {telefono} pertenece a {persona.nombre}.")
                    encontrado = True
                    break

            if not encontrado:
                print("ERROR: No se encontró ningún contacto con ese teléfono.")

        print("")
        input("Pulsa [ENTER] para continuar...")

    except ValueError:
        print("ERROR: Ha ocurrido un error inesperado.")
        print("")
        input("Pulsa [ENTER] para continuar...")
    
    return False



""" Eliminar un contacto """
def delContacto():
    try:
        if not contactos:
            print("ERROR: No existe ningún contacto.")
        else:
            contacto = input("Introduce el nombre del contacto a eliminar: ").strip().upper()
            
            if contacto in contactos:
                nombre = contactos[contacto].nombre
                del contactos[contacto]
                print(f"El contacto {nombre} ha sido eliminado correctamente.")
            else:
                print("ERROR: No se encontró ningún contacto con ese nombre.")

        print("")
        input("Pulsa [ENTER] para continuar...")

    except ValueError:
        print("ERROR: Ha ocurrido un error inesperado.")
        print("")
        input("Pulsa [ENTER] para continuar...")

    return False




def menu():
    print("")
    print("-- MENú DE OPCIONES --")
    print("a) Listado de contactos por orden alfabético.")
    print("b) Añadir un nuevo contacto.")
    print("c) Modificar un contacto.")
    print("d) Buscar un contacto por su número de teléfono.")
    print("e) Eliminar un contacto.")
    print("f) Salir.")



def opcion():
    salir = False
    while not salir:
        try:
            op = input("Opción: ")

            match op:
                case "a":
                    print("")
                    print("=== Listado de contactos por orden alfabético ===")
                    salir = listarContactosAZ()
                    
                case "b":
                    print("")
                    print("=== Añadir un nuevo contacto ===")
                    salir = addContacto()

                case "c":
                    print("")
                    print("=== Modificar un contacto ===")
                    salir = modContacto()

                case "d":
                    print("")
                    print("=== Buscar un contacto por su número de teléfono ===")
                    salir = searchTelf()
                
                case "e":
                    print("")
                    print("=== Eliminar un contacto ===")
                    salir = delContacto()
                
                case "f":
                    salir = True
                
                case _:
                    print("ERROR: No es una opción válida.")
                    print("")
                    input("Pulsa [ENTER] para continuar...")     
                    salir = False

    
            return salir
        except ValueError:
            print("ERROR: Ocurrió un problema inesperado.")
            print("")
            input("Pulsa [ENTER] para continuar...")     



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

