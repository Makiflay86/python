""" 10.Escribe un programa que a partir de información de un donante determine si
puede donar sangre. Las condiciones para donar son:
a. No se debe donar en ayunas.
b. Edad: Comprendida entre los 18 y 65 años.
c. Peso: Superior a 50kg.
d. Tensión arterial: dentro de límites adecuados para la extracción.
i. Tensión diastólica (baja): entre 50mm Hg y 100 mm Hg
ii. Tensión sistólica (alta): entre 90mm y 180mm Hg
e. Pulso (frecuencia cardiaca): entre 50 y 110 pulsaciones
f. Valores de hemoglobina:
i. En hombres: superior a 13,5 gramos por litro
ii. En mujeres: superior a 12,5 gramos por litro.
g. Plaquetas: más de 150.000 cc
h. Proteínas totales: más de 6 gr/dl. """

import sys



print("--- Programa de Verificación de Donante de Sangre ---")

apto_para_donar = True
motivo_rechazo = ""



# No en ayunas
ayunas = input("¿Ha comido algo en las últimas 4 horas? (Sí/No): ").strip().lower()

# Edad
edad = int(input("Introduce la edad del donante (años): "))

# Peso
peso = float(input("Introduce el peso del donante (kg): "))

# Tensión Arterial
sistolica = int(input("Introduce la tensión sistólica (alta, mm Hg): "))
diastolica = int(input("Introduce la tensión diastólica (baja, mm Hg): "))

# Pulso
pulso = int(input("Introduce el pulso (pulsaciones por minuto): "))

# Sexo y Hemoglobina
sexo = input("Introduce el sexo (H/M): ").strip().lower()
hemoglobina = float(input("Introduce el valor de Hemoglobina (gramos por litro): "))

# Plaquetas
plaquetas = int(input("Introduce el valor de Plaquetas (por cc, ej. 180000): "))

# Proteínas totales
proteinas = float(input("Introduce el valor de Proteínas totales (gr/dl): "))



# No ayunas
if ayunas != 'si':
    apto_para_donar = False
    motivo_rechazo = "Debe haber comido en las últimas 4 horas (no donar en ayunas)."

# Edad (entre 18 y 65)
elif not (18 <= edad <= 65):
    apto_para_donar = False
    motivo_rechazo = "La edad debe estar entre 18 y 65 años."

# Peso (superior a 50kg)
elif peso <= 50:
    apto_para_donar = False
    motivo_rechazo = "El peso debe ser superior a 50 kg."

# Diastólica (baja): entre 50 y 100
elif not (50 <= diastolica <= 100):
    apto_para_donar = False
    motivo_rechazo = "La tensión diastólica debe estar entre 50 y 100 mm Hg."
    
# Sistólica (alta): entre 90 y 180
elif not (90 <= sistolica <= 180):
    apto_para_donar = False
    motivo_rechazo = "La tensión sistólica debe estar entre 90 y 180 mm Hg."

# Pulso (entre 50 y 110)
elif not (50 <= pulso <= 110):
    apto_para_donar = False
    motivo_rechazo = "El pulso debe estar entre 50 y 110 pulsaciones por minuto."

# Hombres: > 13.5 / f.ii. Mujeres: > 12.5
elif (sexo == 'h' and hemoglobina <= 13.5):
    apto_para_donar = False
    motivo_rechazo = "Hemoglobina en hombres debe ser superior a 13.5 g/L."

elif (sexo == 'm' and hemoglobina <= 12.5):
    apto_para_donar = False
    motivo_rechazo = "Hemoglobina en mujeres debe ser superior a 12.5 g/L."

# Plaquetas (> 150.000 cc)
elif plaquetas <= 150000:
    apto_para_donar = False
    motivo_rechazo = "El recuento de plaquetas debe ser superior a 150.000 cc."

# Proteínas totales (> 6 gr/dl)
elif proteinas <= 6:
    apto_para_donar = False
    motivo_rechazo = "Las proteínas totales deben ser superiores a 6 gr/dl."



print("\n" + "="*40)
if apto_para_donar:
    print("¡APTO PARA DONAR! El donante cumple todas las condiciones.")
else:
    print("NO APTO PARA DONAR.")
    print(f"Motivo de exclusión: {motivo_rechazo}")
print("="*40)