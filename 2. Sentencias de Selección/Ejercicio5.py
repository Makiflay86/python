# 5. Escribe un programa que calcule el precio de entrada a un museo a partir de
# la edad del visitante, teniendo en cuenta que:
#   a. Menores de 5 años entran gratis.
#   b. Niños entre 5 años y 18 (sin llegar a los 18) pagan 3€.
#   c. Mayores de edad hasta los 65 (sin llegar a los 65) pagan 6€.
#   d. Jubilados entran gratis.

print ("-- Programa que calcula el precio de entrada al museo --")
# Pedir al usuario la edad
edad = int(input("Introdcue la edad: "))

# Calcular el precio de la entrada basandonos en la edad
precioEntrada = 0; 
if (edad < 5):
    precioEntrada = 0;
elif (edad < 18):
    precioEntrada = 3;
elif (edad < 65):
    precioEntrada = 6;
else :
    precioEntrada = 0;

# Mostramos el resultado
print ("El precio de la entrada es de: ", str(precioEntrada), "€.");
