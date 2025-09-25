# 2. Escribe un programa que recoja un número por teclado y muestre el día de la
# semana que es (1 = Lunes, 2 = Martes...). En caso de introducir un número
# incorrecto, mostrará el mensaje “Día de la semana incorrecto”.

print ("-- Programa que diga el día de la semena mediante un número que le pasemos --");
# Pedir al usuario un número (1 al 7)
numero = int(input("Introduce un número (1 - 7): "));

# Mostrar el día dependiendo del número
match numero:
    case 1:
        print ("El día de hoy es 'Lunes'.");
    
    case 2:
        print ("El día de hoy es 'Martes'.");

    case 3:
        print ("El día de hoy es 'Miércoles'.");

    case 4:
        print ("El día de hoy es 'Jueves'.");

    case 5:
        print ("El día de hoy es 'Viernes'.");

    case 6:
        print ("El día de hoy es 'Sábado'.");

    case 7:
        print ("El día de hoy es 'Domingo'.");

    case _:
        print ("ERROR: Ese número no está en el rango establecido.");

