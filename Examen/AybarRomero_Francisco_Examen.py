""" EXAMEN """
import random


""" Reemplazar vocales de una frase """
def reemplazarVocales():
    print("")
    print("Reemplazar vocales de una frase.")
    print("=" * 40)
    salir = False
    while not salir:
        try:
            texto = input("Introduce una frase: ")
 
            for p in texto:
                match (p.lower()):
                    case "a" | "e" | "i" | "o" | "u" | "á" | "é" | "í" | "ó" | "ú":
                        p = "*"
                print(p, end="")

            
            print("")
            input("Enter para continuar...")
            print("")
            
            salir = True

        except ValueError:
            print("ERROR: Ocurrió un problema inesperado.")
            print("")
            salir = False

    return False



""" Pedir un número y si es menor que el anterior le salta un avisos """
def pedirNumero():
    print("")
    print("Mensaje cuando el número introducido no sea mayor que el primero.")
    print("=" * 40)
    salir = False
    mayor = 0
    while not salir:
        try:
            numero = int(input("Introduce un número(<0=>salir): "))
        
            if (numero < 0):
                print("")
                input("Enter para continuar...")
                print("")
                
                salir = True
            else:
                if numero < mayor:
                    print("ERROR: El número es menor que el anterior introducido.")
                    print("")
                else:
                    mayor = numero
            
        except ValueError:
            print("ERROR: Ocurrió un problema inesperado.")
            print("")
            salir = False

    return False



""" Conocer la palabra más larga de la frase """
def palabraLarga():
    print("")
    print("Encontrar la primera palabra más larga.")
    print("=" * 40)
    salir = False
    while not salir:
        try:
            texto = input("Introduce una texto: ")
            texto_separado = texto.split(" ")
            palabra = ""
            sizePalabra = 0

            for p in texto_separado:
                if len(p) > sizePalabra:
                    sizePalabra = len(p)
                    palabra = p

            print("La palabra más larga es: ", palabra)

            print("")
            input("Enter para continuar...")
            print("")

            salir = True

        except ValueError:
            print("ERROR: Ocurrió un problema inesperado.")
            print("")
            salir = False

    return False



""" Generar un número random entre 0 - 100 pero solo devuelve los impares """
def nRandom():
    salir = False
    while not salir:
        n = int(random.random()*100)
        if n % 3 == 0:
            salir = True

    return n



""" Tabla con números impares """
def rectangulo():
    print("")
    print("Mostrar rectángulo con números impares entre 0 y 100.")
    print("=" * 40)
    salir = False
    while not salir:
        try:
            """ Columnas y fila """
            row = int(input("Introduce el número de fila: "))
            col = int(input("Introduce el número de columna: "))

            print("")
            for i in range(row):
                for j in range(col):
                    print(nRandom(), end="\t")
                print()

            print("")
            input("Enter para continuar...")
            print("")

            salir = True

        except ValueError:
            print("ERROR: Ocurrió un problema inesperado.")
            print("")
            salir = False

    return False
    


def contarCaracter():
    print("")
    print("Contar la aparición de cada carácter en una palabra. Mostrar diccionario y el carácter con más apariciones.")
    print("=" * 40)
    salir = False
    while not salir:
        try:


            print("")
            input("Enter para continuar...")
            print("")

            salir = True

        except ValueError:
            print("ERROR: Ocurrió un problema inesperado.")
            print("")
            salir = False

    return False



def menu():
    print("")
    print("-- MENú DE OPCIONES --")
    print("a) Reemplazar vocales de una frase.")
    print("b) Mensaje cuando el número introducido no sea mayor que el primero.")
    print("c) Encontrar la primera palabra más larga.")
    print("d) Mostrar rectángulo con números impares entre 0 y 100.")
    print("e) Contar la aparición de cada carácter en una palabra. Mostrar diccionario y el carácter con más apariciones.")
    print("f) Salir.")



def opcion():
    salir = False
    while not salir:
        try:
            op = input("Opción: ")
            print("")

            match op:
                case "a":
                    salir = reemplazarVocales()
                    
                case "b":
                    salir = pedirNumero()

                case "c":
                    salir = palabraLarga()

                case "d":
                    salir = rectangulo()
                
                case "e":
                    salir = contarCaracter()
                
                case "f":
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

