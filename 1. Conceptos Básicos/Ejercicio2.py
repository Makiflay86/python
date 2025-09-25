# 2 Escribe un programa que recoja dos números enteros por teclado 
# y muestre los siguientes resultados: suma, resta, multiplicación, 
# división real, división entera, resto de la división entera y 
# potencia.

print ("-- Programa que pida dos números y hace unas operaciones --");
numero1 = int(input("Introduce el número 1: "));
numero2 = int(input("Introduce el número 2: "));
# print ("Los números son: " + numero1 + " y " + numero2);

# Sumamos los dos números
calculo = numero1 + numero2;
print ("Suma: ", calculo);

# Restamos los dos números
calculo = numero1 - numero2;
print ("Resta: ", calculo);

# Multiplicamos los dos números
calculo = numero1 * numero2;
print ("Multiplicación: ", calculo);

# Dividimos (real) los dos números
calculo = numero1 / numero2;
print ("División Real: ", calculo);

# Dividimos (entera) los dos números
calculo = numero1 // numero2;
print ("División Entera: ", calculo);

# Resto de los dos números
calculo = numero1 % numero2;
print ("Resto: ", calculo);

# Potencia de los dos números
calculo = numero1 ** numero2;
print ("Potencia: ", calculo);