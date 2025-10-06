# 6. Escribe un programa que recoja las notas de las tres evaluaciones de un
# alumno. A continuación debe calcular y mostrar la nota final, teniendo en
# cuenta que la primera evaluación cuenta un 20% de la nota final, la segunda
# evaluación un 35% y la tercera evaluación un 45%.

print ("-- Programa que calcula la nota final con sus respectivos porcentajes --");
# Pedir al usuario las notas de las 3 evaluaciones
nota1 = int(input("Introduce la nota del primer trimestre: "));
nota2 = int(input("Introduce la nota del segundo trimestre: "));
nota3 = int(input("Introduce la nota del tercer trimestre: "));

# Mostramos la nota final
notaFinal = int((nota1 * 0.20) + (nota2 * 0.35) + (nota3 * 0.45));
print ("\nLa nota final es un: ", str(notaFinal));