"""8º Escribe un programa que recoja un número y calcule si es primo."""

# Creo que hay que revisarlo, o_0

numero = int(input("Introduce un número: "))
resultado = "";

if numero < 2:
    print ("ERROR: No es un número entero.");
elif numero == 2:
    print ("El número es primo.");
else:
    if numero % 2 == 0:
        resultado = "El número es primo.";
    else:
        resultado = "El número no es primo.";

print (resultado);




