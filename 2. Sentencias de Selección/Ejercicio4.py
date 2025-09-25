# 4. Escribe un programa que recoja dividendo y divisor, y realice su división
# siempre que el divisor sea distinto de cero.

print ("-- Programa que recoja diviendo y divisor --");
# Pedir al usuario dividendo y divisor
dividendo = int(input("Introduce el dividendo: "));
divisor = int(input("Introduce el divisor (no puede ser cero):"));

# Comprobar que el divisor no sea cero y si no realizamos el calculo y lo mostramo
if (divisor == 0):
    print ("ERROR: Divisor es igual a 0.");
else :
    print ("La división de '" + str(dividendo) + " entre " + str(divisor) + "' es: ", str(dividendo / divisor));
