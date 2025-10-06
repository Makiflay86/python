"""5º Escribe un programa que recoja un número por teclado y muestre los primeros
cuadrados hasta llegar al número introducido. Por ejemplo, si se ha introducido
el valor 5, se debe mostrar:"""

numero = int(input("Introduce un número: "))
x = 1;

for i in range(numero):
    print (x*x, end=" ");
    x += 1;

