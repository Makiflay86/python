# 7. Escribe un programa que recoja la hora del día y devuelva un saludo, 
# según las siguientes reglas:
    # Intervalo de horas        Saludo
    #       [7, 12]          Buenos días
    #       [12, 20]        Buenas tardes
    #    En otro caso       Buenas noches

print ("-- Programa que coge la hora del día y devulve un saludo --");

hora = int(input("Introduce la hora del día(HH): "));

if (hora >= 7 and hora <= 12):
    print ("Buenos días");
elif (hora > 12 and hora <= 20):
    print ("Buenas tardes");
else:
    print ("Buenas noches");