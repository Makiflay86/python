# 9. Escribe un programa que recoja un año e indique si se trata de un año 
# bisiesto o no. Un año es bisiesto si cumple estas condiciones: 
    # a. El año es divisible por 4. 
    # b. Si además el año es divisible por 100, debe ser también divisible por 400.
# Ejemplos:
# - 1992 es bisiesto (cumple el caso a. Al no ser divisible por 100 no aplica 
# el caso b) 
# - 2023 no es bisiesto (no cumple ningún caso) 
# - 2000 es bisiesto (cumple los casos a y b) 
# - 1900 no es bisiesto (cumple el caso a, pero no el b porque es divisible 
# por 100 y no por 400) 



year = int(input("Introduce un año (YYYY): "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"El año {year} es bisiesto.")
else:
    print(f"El año {year} no es bisiesto.")
