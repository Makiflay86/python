"""7º Escribe un programa que recoja una cadena de texto por teclado y una letra a
buscar. Luego debe buscar dicha letra por la cadena y al finalizar debe indicar
el número de veces que se repite la letra en el texto."""

cadena = (input("Introduce una cadena de carácteres: "));
letra = input("Introduce una letra a buscar: ")
contador = 0;
x = 0;

while(x != len(cadena)):
    if (cadena[x] == letra):
        contador += 1;
    x += 1;

if (contador < 1):
    vez = "vez";
else:
    vez = "veces";

print ("Se han encontrado", contador, vez, "la letra", letra)
