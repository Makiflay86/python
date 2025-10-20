""" 
    1. Escribe un programa que recoja números de teclado hasta que se introduce un
    cero. Luego debe mostrar la secuencia de números de tres modos:
    a. En el orden en que se introdujeron.
    b. En orden creciente.
    c. En orden decreciente.
 """



def pedirNumero():
    salir = False
    listaNumero = []
    while (not salir):
        try:
            entrada = input("Introduce un número(0=salir): ")
            numero = int(entrada)
            if (numero == 0):
                salir = True
            else:
                listaNumero.append(numero)
        except:
            print("ERROR: Debes introducir un número entero")
            print("")
            salir = False
    return listaNumero


def menu():
    print("")
    print("-- Menú --")
    print("a. En el orden en que se introdujeron.")
    print("b. En orden creciente.")
    print("c. En orden decreciente.")
    print("d. Salir.")



def leerOpcion():
    opciones_validas = set("abcd")
    salir = False
    while (not salir):
        opcion = input("Opción: ").lower()
        if (opcion in opciones_validas):
            salir = True
        else:
            salir = False
            print("ERROR: Opción incorrecta(a-d)")
            print("")
    return opcion



salir = False
numeros = pedirNumero()

while (not salir):
    print(menu())
    opcion = leerOpcion()
    if (opcion == "d"):
        salir = True
    elif (opcion == "a"):
        print(" ")
        print("a. En el orden en que se introdujeron.")
        for i in range(len(numeros)):
            print(numeros[i], end=" ")
        print(" ")
        salir = False
    elif (opcion == "b"):
        print(" ")
        print("b. En orden creciente.")
        for i in range(len(numeros)):
            numeros.sort()
            print(numeros[i], end=" ")
        print(" ")
        salir = False
    elif (opcion == "c"):
        print(" ")
        print("c. En orden decreciente.")
        for i in range(len(numeros)):
            numeros.sort(reverse=True)
            print(numeros[i], end=" ")
        print(" ")
        salir = False
    else:
        print("ERROR: Elige una opción correcta")
        print(" ")
        salir = False
else:
    print(" ")
    print("FINALIZANDO PROGRAMA...")
    








""" 
salir = False
listaNumero = []
while (not salir):
    try:
        entrada = input("Introduce un número(0=salir): ")
        numero = int(entrada)
        if (numero == 0):
            salir = True
        else:
            listaNumero.append(numero)
    except:
        print("ERROR: Debes introducir un número entero")
        salir = False


print("a. En el orden en que se introdujeron.")
for i in range(len(listaNumero)):
    print(listaNumero[i], end=" ")

print("")
print("")

print("b. En orden creciente.")
for i in range(len(listaNumero)):
    listaNumero.sort()
    print(listaNumero[i], end=" ")

print("")
print("")

print("c. En orden decreciente.")
for i in range(len(listaNumero)):
    listaNumero.sort(reverse=True)
    print(listaNumero[i], end=" ") """