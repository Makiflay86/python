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

import math

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



""" a) Mostrar un rombo """
def mostrarRombo():
    for i in range(1, 7 + 1):
        espacios = 7 - i
        asteriscos = 2 * i - 1
        print(" " * espacios + "*" * asteriscos)

    for i in range(7 - 1, 0, -1):
        espacios = 7 - i 
        asteriscos = 2 * i - 1
        print(" " * espacios + "*" * asteriscos)


"""b) Adivinar un número"""
def adivinarNum(n):
    numero = 3
    adivinar = True

    if (n != numero):
        adivinar = False

    return adivinar


""" c) Resolver una ecuación de segundo grado """
def ecuacion2Grado(a, b, c):
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


""" d) Tabla de números """

