# 10.Escribe un programa que recoja la edad del usuario y muestre la edad que
# tendrá dentro de 5, 10 y 15 años.

print ("-- Programa que pide una edad y muestra la que tendra en un futuro --");
# Pedir al usuario una edad
edad = int(input("Introduce tu edad: "));

# Mostrar la edad que tendra en 5, 10 y 15 años
print ("\nEn 5 años tendrás: ", str(edad + 5), "años.");
print ("En 10 años tendrás: ", str(edad + 10), "años.");
print ("En 15 años tendrás: ", str(edad + 15), "años.");