# 7. Escribe un programa que recoja un número y muestre su representación en
# código binario.

print ("-- Programa que pide un número y muestra su binario --");
# Pedir al usuario un número
numero = int(input("Introduce un número: "));

# Mostrar el binario del número
numeroBinario = bin(numero);
print ("\nEl número '" + str(numero) + "' en binario es: ", str(numeroBinario));