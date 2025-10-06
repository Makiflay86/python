# 4. Escribe un programa que recoja tres números y calcule su media aritmética.

print ("-- Programa que calcula lal media aritmética de 3 números --");
# Pedir al usuario tres números
numero1 = int(input("Introduce el número1: "));
numero2 = int(input("Introduce el número2: "));
numero3 = int(input("Introduce el número3: "));

# Calcular y Mostrar el resultado final
mediaAritmetica = int((numero1 + numero2 + numero3) / 3);
print ("La media aritmética es: ", mediaAritmetica);