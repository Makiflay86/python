"""9º Escribe un programa que recoja un número impar. Debe asegurarse de que
sea impar, en caso de no serlo debe descartarlo y pedirlo de nuevo. Una vez
tenga el número impar debe mostrar una pirámide de asteriscos cuya base es
igual al número introducido. Por ejemplo, si se introduce el valor 7 se debe
mostrar:"""

numeroImpar = int(input("Introduce un número impar: "))

while(numeroImpar % 2 == 0):
    print ("ERROR: No es un número impar, vuelva a intentarlo a continuación.")
    numeroImpar = int(input("Introduce un número impar: "))

# El triangulo debe de ser centrado y no como sale, corregir

for i in range(numeroImpar):
    for j in range(i+1):
        print ("*", end="");
    print()