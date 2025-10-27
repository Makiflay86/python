""" 1. Al arrancar debe mostrar un menú de opciones como el siguiente:
MENÚ DE OPCIONES
a) Mostrar un rombo.
b) Adivinar un número.
c) Resolver una ecuación de segundo grado.
d) Tabla de números.
e) Cálculo del número factorial de un número.
f) Cálculo de un número de la sucesión de Fibonacci.
g) Tabla de multiplicar.
h) Salir """


""" import math

opcion = "";

while (opcion != "h"):
    print ("a) Mostrar un rombo")
    print ("b) Adivinar un número")
    print ("c) Resolver una ecuación de segundo grado")
    print ("d) Tabla de números")
    print ("e) Cálculo del número factorial de un número")
    print ("f) Cálculo de un número de la sucesión de Fibonacci")
    print ("g) Tabla de multiplicar")
    print ("h) Salir")
    opcion = (input("Opción: ")).lower();
 """


""" a) Mostrar un rombo """
""" def mostrarRombo():
    for i in range(1, 7 + 1):
        espacios = 7 - i
        asteriscos = 2 * i - 1
        print(" " * espacios + "*" * asteriscos)

    for i in range(7 - 1, 0, -1):
        espacios = 7 - i 
        asteriscos = 2 * i - 1
        print(" " * espacios + "*" * asteriscos)
 """

"""b) Adivinar un número"""
""" def adivinarNum(n):
    numero = 3
    adivinar = True

    if (n != numero):
        adivinar = False

    return adivinar
 """

""" c) Resolver una ecuación de segundo grado """
""" def ecuacion2Grado(a, b, c):
    error = False
    resultado = ""
    
    if a == 0:
        error = True
        resultado = "ERROR: Operación no válida, 'a' no puede ser 0."
    
    if not error:
        discriminante = (b ** 2) - (4 * a * c)
        divisor = 2 * a

        if discriminante < 0:
            error = True
            resultado = "ERROR: Operación no válida, la raíz (discriminante) es negativa (soluciones complejas)."
        
        if not error:
            raizfin = math.sqrt(discriminante)
            
            solucionPositiva = (-b + raizfin) / divisor
            solucionNegativa = (-b - raizfin) / divisor
    
    if error:
        print(resultado)
    else:
        print("Tenemos dos posibles soluciones:")
        print("Solucion Positiva:", solucionPositiva) 
        print("Solucion Negativa:", solucionNegativa)
 """

""" d) Tabla de números """










import random
import math
from math import sqrt


def menu():
    print("")
    print("Menu de Opciones")
    print("a) Mostrar un rombo.")
    print("b) Adivinar un número.")
    print("c) Resolver una ecuación de segundo grado.")
    print("d) Tabla de números.")
    print("e) Cálculo del número factorial de un número.")
    print("f) Cálculo de un número de la sucesión de Fibonacci.")
    print("g) Tabla de multiplicar.")
    print("h) Salir")


def LeerOpcion():
    opciones_validas = set("abcdefgh")
    while True:
        opcion = input(
            "Introduce el cálculo que desea realizar la letra por favor: "
        ).lower()
        if opcion in opciones_validas:
            return opcion
        else:
            print(
                "Por favor, introduzca una letra válida del menú (de la 'a' a la 'h')."
            )


# funcion para comprobar que el sea numero lo que se introduce por teclado.
def obtener_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debes introducir un valor numérico entero. Intenta de nuevo.")


def rombo():
    numero = 0
    while numero % 2 == 0:
        numero = obtener_numero("Introduce un número impar: ")

    filas = int((numero + 1) / 2)

    # Parte superior del rombo
    for i in range(1, filas + 1):
        print(" " * (filas - i) + "*" * (2 * i - 1))

    # Parte inferior del rombo
    for i in range(filas - 1, 0, -1):
        print(" " * (filas - i) + "*" * (2 * i - 1))


def tablaNumeros():
    filas = obtener_numero("Filas: ")
    columnas = obtener_numero("Columnas: ")
    contador = 1
    for _ in range(filas):  # for anidados para sacar la filas y la columnas
        for _ in range(columnas):
            print(contador, end="\t")
            contador += 1
        print(" ")


def factorial():
    numero = obtener_numero("¿De qué número quieres su factorial?: ")
    factorial = 1
    if numero < 0:
        {print("Numero negativos no está permitido")}
    else:
        for i in range(2, numero + 1):
            factorial *= i
        print("El factorial de", numero, "es", factorial)


def adivinarNumero():
    numeroAdivinar = random.randint(1, 100)

    salir = False

    while not salir:
        numero = obtener_numero("Adivina el número: ")

        if numero < numeroAdivinar:
            print("El número es mayor.")
        elif numero > numeroAdivinar:
            print("El número es menor.")
        else:
            print("¡Enhorabuena, lo has conseguido!")
            salir = True


def multiplicar():
    while True:
        entrada = input("¿De qué número quieres la tabla de multiplicar?: ")
        if entrada.isnumeric():  # esta funcion comrueba que sea numero
            numero = int(entrada)
            for i in range(1, 11):
                resultado = numero * i
                print(numero, " x ", i, " = ", resultado)
            return
        else:
            print("Error: Debes introducir numero entero. Intenta de nuevo.")


def resolverEcuacion():
    a = obtener_numero("Dame el valor del coeficiente a: ")
    b = obtener_numero("Dame el valor del coeficiente b: ")
    c = obtener_numero("Dame el valor del coeficiente c: ")

    # calculamos por si el valor es negativo ya que si lo es no se puede calcular
    discriminante = b * b - 4 * a * c

    if discriminante < 0:  # comprobamos si no existen soluciones reales
        print(f"La ecuación no tiene soluciones reales.")

    else:
        raiz = sqrt(discriminante)  # calculamos la raíz si no es negativa
        x1 = (-b + raiz) / (2 * a)  # calculamos una primera solución

        if discriminante != 0:  # comprobamos si hay otra solución
            x2 = (-b - raiz) / (2 * a)  # calculamos la segunda solución
            print(f"Las soluciones son {x1} y {x2}.")  # mostramos las dos soluciones
        else:
            print(f"La única solución es x = {x1}")  # mostramos la única solución


def fibonacci():
    numero = obtener_numero("¿Qué posición quiere hallar en la sucesión de Fibonacci? ")

    a, b = 0, 1
    print("Secuencia de Fibonacci:")
    for _ in range(numero):
        a, b = b, a + b  # formula para sacar el fibonacci
        print ("el valor de a",a)
        print ("el valor de b",b)
    print(a, end=" ")
    print()


"""def fibonacci():
    posicion = int(input("¿De qué número quieres la serie fibonacci?: "))
    if posicion == 0:
        print(0)
    elif posicion == 1:
        print(1)
    else:
        resultado = fibonacci(posicion - 1) + fibonacci(posicion - 2)
        print(resultado)"""


def EjecutarOpcion(opcion):
    if opcion == "a":
        print("Has seleccionado Mostrar un rombo.")
        rombo()
        x = input("Pulsa una tecla para continuar.......")
    elif opcion == "b":
        print("Has seleccionado Adivinar un número.")
        adivinarNumero()
        x = input("Pulsa una tecla para continuar.......")
    elif opcion == "c":
        print("Has seleccionado Resolver una ecuación de segundo grado.")
        resolverEcuacion()
        x = input("Pulsa una tecla para continuar.......")
    elif opcion == "d":
        print("Has seleccionado Tabla de números.")
        tablaNumeros()
        x = input("Pulsa una tecla para continuar.......")
    elif opcion == "e":
        print("Has seleccionado Cálculo del número factorial de un número.")
        factorial()
        x = input("Pulsa una tecla para continuar.......")
    elif opcion == "f":
        print("Has seleccionado Cálculo de un número de la sucesión de Fibonacci.")
        fibonacci()
        x = input("Pulsa una tecla para continuar.......")
    elif opcion == "g":
        print("Has seleccionado Tabla de multiplicar.")
        multiplicar()
        x = input("Pulsa una tecla para continuar.......")
    else:
        print("Opción inválida. Inténtalo de nuevo.")


salir = False
while not salir:
    menu()
    opcion = LeerOpcion()
    if opcion == "h":
        salir = True
    else:
        EjecutarOpcion(opcion)
else:
    print("Saliendo del programa. ¡CHAO!")