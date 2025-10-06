""" 6º Escribe un programa que recoja un número de filas y columnas, y muestre una
tabla con tantas filas y columnas como indicadas, numerando las celdas de
izquierda a derecha y de arriba abajo. Por ejemplo, si se introducen 2 filas y 3
columnas, se debe mostrar:"""

row = int(input("Introduce el número de fila: "))
col = int(input("Introduce el número de columna: "))
x = 1;

for i in range(row):
    for j in range(col):
        print(x, end="\t")
        x += 1;
    print()
