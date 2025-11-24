""" Hay que realizar 3 ejercicios con diccionarios, le pediremos al usuario
que ejercicio quiere realizar y este mostrar el ejercicio elegido, termina 
cuando el usuario selecione salir. """



# =======================================================
# Ejercicio 1
# =======================================================

def ejercicio1():
    print("")
    print("========================================================================")
    print("-- Ejercicio 1 --")
    print("========================================================================")
    nombre = pedir_nombre()
    edad = pedir_edad()
    direccion = pedir_direccion()
    telefono = pedir_telefono()

    print("")
    print(f"{nombre} tiene {edad} años, vive en {direccion} y su número de teléfono es {telefono}.")

    return False



# Pedir nombre
def pedir_nombre():
    nombre = input("Introduce tu nombre: ")

    return nombre



# Pedir edad
def pedir_edad():
    edad = input("Introduce tu edad: ")

    return edad



# Pedir dirección
def pedir_direccion():
    direccion = input("Introduce tu dirección: ")

    return direccion



# Pedir teléfono
def pedir_telefono():
    telefono = input("Introduce tu teléfono: ")

    return telefono



# mostrar información
def toString(nombre, edad, direccion, telefono):
    return (f"{nombre} tiene {edad} años, vive en {direccion} y su número de teléfono es {telefono}.")




# =======================================================
# Ejercicio 2
# =======================================================

def ejercicio2():
    print("")
    print("========================================================================")
    print("-- Ejercicio 2 --")
    print("========================================================================")
    dic = { # Datos precargado para testear
    "Mario": (18, "Cantabria", "8777"),
    "Lucía": (25, "Sevilla", "1234"),
    "Carlos": (30, "Valencia", "5678"),
    "Ana": (22, "Barcelona", "9101")
    }


    salir = False
    while not salir:
        try:
            nombre = pedir_nombre()
            edad = pedir_edad()
            direccion = pedir_direccion()
            telefono = pedir_telefono()

            if not nombre.strip() or not edad.strip() or not direccion.strip() or not telefono.strip():
                print("WARNING: Usuario no añadido porque faltan datos.")
            else:
                print("Usuario añadido.")
                dic[nombre] = edad, direccion, telefono

            print("")
            print("¿Quieres añadir otro usuario? (S/N)")
            op = input("Opción: ").upper()
            if (op == "S"):
                salir = False
            else:
                print("")
                for nombre, (edad, direccion, telefono) in dic.items():
                    print(toString(nombre, edad, direccion, telefono))


                print("")
                input("Pulsa enter para continuar...")
                          
                salir = True  
        
        except ValueError:
            print("ERROR: No es una opción válida.")
            salir = False
            print("")
            input("Pulsa enter para continuar...")

    return False    



# =======================================================
# Ejercicio 3
# =======================================================

def ejercicio3():
    print("")
    print("========================================================================")
    print("-- Ejercicio 3 --")
    print("========================================================================")
    nombre_tienda = "El Gran Bazar"
    ventas = {
        "Abanico de papel": {
            1: 12, 2: 34, 3: 5, 4: 88, 5: 23, 6: 45, 7: 67, 8: 1, 9: 99, 10: 50,
            11: 21, 12: 7, 13: 42, 14: 68, 15: 91, 16: 3, 17: 55, 18: 78, 19: 29, 20: 83,
            21: 14, 22: 60, 23: 37, 24: 95, 25: 19, 26: 72, 27: 48, 28: 8, 29: 63, 30: 31
        },
        "Gato de la suerte": {
            1: 22, 2: 11, 3: 44, 4: 77, 5: 9, 6: 33, 7: 56, 8: 89, 9: 2, 10: 65,
            11: 41, 12: 18, 13: 73, 14: 30, 15: 85, 16: 13, 17: 51, 18: 93, 19: 27, 20: 61,
            21: 4, 22: 49, 23: 82, 24: 16, 25: 70, 26: 38, 27: 96, 28: 24, 29: 58, 30: 80
        },
        "Farolillo rojo": {
            1: 5, 2: 15, 3: 25, 4: 35, 5: 45, 6: 55, 7: 65, 8: 75, 9: 85, 10: 95,
            11: 10, 12: 20, 13: 30, 14: 40, 15: 50, 16: 60, 17: 70, 18: 80, 19: 90, 20: 100,
            21: 13, 22: 23, 23: 33, 24: 43, 25: 53, 26: 63, 27: 73, 28: 83, 29: 93, 30: 0
        },
        "Juego de té": {
            1: 8, 2: 19, 3: 28, 4: 39, 5: 48, 6: 59, 7: 68, 8: 79, 9: 88, 10: 99,
            11: 17, 12: 26, 13: 37, 14: 46, 15: 57, 16: 66, 17: 77, 18: 86, 19: 97, 20: 6,
            21: 24, 22: 35, 23: 44, 24: 55, 25: 64, 26: 75, 27: 84, 28: 95, 29: 4, 30: 52
        }
    }

    print(f"Informe de ventas para la tienda: '{nombre_tienda}'\n")
    for producto, registro_diario in ventas.items():
        print(f"--- Ventas para '{producto}' ---")
        total_ventas_producto = 0
        for dia, cantidad in registro_diario.items():
            total_ventas_producto += cantidad
        print(f"Ventas totales del mes: {total_ventas_producto} unidades.")
        print("-" * 40 + "\n")
    
    print("")
    input("Pulsa enter para continuar...")








# Opción para que elija
def opcion():
    salir = False
    while not salir:
        try:
            op = input("Opción: ")
            match op:
                case "1":
                    salir = ejercicio1()
                    break
                case "2":
                    salir = ejercicio2()
                    break
                case "3":
                    salir = ejercicio3()
                    break
                case "4":
                    salir = True
                case "":
                    salir = True
                    break
                case _:
                    print("ERROR: No es una opción válida.")

        except ValueError:
            print("ERROR: No es una opción válida.")
            print("")
            input("Pulsa enter para continuar...")

    return salir









""" TESTING """

salir = False
while not salir:
    try:
        print("")
        print("========================================================================")
        print("-- Elige el ejercicio --")
        print("========================================================================")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Salir")
        op = opcion()        
        
        if (op == True):
            salir = True
        else:
            salir = False
            

    
    except ValueError:
        print("ERROR: No es una opción válida.")
        salir = False
        print("")
        input("Pulsa enter para continuar...")
        
else:
    print("")
    print("FINALIZANDO PROGRAMA...")