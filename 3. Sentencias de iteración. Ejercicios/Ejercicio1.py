"""1º Escribe un programa que recoja un texto y escriba cada letra del texto 
en una línea distinta."""

texto = str(input("Introduce un texto: "));
sizeTexto = len(texto);
x = 0;

while x < sizeTexto:
    print (texto[x]);
    x += 1;



