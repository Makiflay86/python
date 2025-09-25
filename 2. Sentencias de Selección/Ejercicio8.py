# 8. Escribe un programa que recoja un mes del año (en número) y devuelva el 
# número de días que tiene el mes. En caso de indicar un mes incorrecto deberá 
# mostrar un mensaje de error. 

print ("-- Programa que recoge un mes del año y devuelve el nº de días del mes --");

mes = int(input("Introduce el mes del año(MM): "));

match (mes):
    case 1:
        print ("Enero(", mes, ") tiene 31 días.");
    case 2:
        print ("Febrero(", mes, ") tiene 28 días.");
    case 3:
        print ("Marzo(", mes, ") tiene 31 días.");
    case 4:
        print ("Abril(", mes, ") tiene 30 días.");
    case 5:
        print ("Mayor(", mes, ") tiene 31 días.");
    case 6:
        print ("Junio(", mes, ") tiene 30 días.");
    case 7:
        print ("Julio(", mes, ") tiene 31 días.");
    case 8:
        print ("Agosto(", mes, ") tiene 31 días.");
    case 9:
        print ("Septiembre(", mes, ") tiene 30 días.");
    case 10:
        print ("Octubre(", mes, ") tiene 31 días.");
    case 11:
        print ("Noviembre(", mes, ") tiene 30 días.");
    case 12:
        print ("Diciembre(", mes, ") tiene 31 días.");
    case _:
        print ("ERROR: No es un mes correcto.");

