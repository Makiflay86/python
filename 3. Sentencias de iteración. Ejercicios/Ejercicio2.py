"""2º Escribe un programa que recoja un número y calcule su factorial."""

numero = int(input("Introduce un número: "));
factorial = numero;
x = 1;

for i in range(numero):
    print (numero, " x ", x, " = ", numero*x);
    factorial = numero * x;
    x += 1;

print ("El factorial de ", numero, " es: ", factorial)
