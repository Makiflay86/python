# 5. Escribe un programa que recoja un número y muestre su valor absoluto.

print ("-- Programa que pide un número y muestra su valor absoluto --");
# Pedir al usuario un número
numero = int(input("Introduce un número: "));

# Mostrar el valor absoluto de dicho número
numero_abs = abs(numero);
print ("El valor absoluto de '" + str(numero) + "' es: ", str(numero_abs));
