# 6. Escribe un programa que muestre la nota final de un alumno a partir de su 
# calificación numérica (valor decimal), teniendo en cuenta que: 
    # a. Nota menor de 5 es suspenso. 
    # b. Nota entre 5 y 6 (sin llegar) es suficiente. 
    # c. Nota entre 6 y 7 (sin llegar) es bien. 
    # d. Nota entre 7 y 9 (sin llegar) es notable. 
    # e. Nota entre 9 y 10 (sin llegar) es sobresaliente. 
    # f. Nota igual a 10 es matrícula de honor. 
    # g. Cualquier otro valor numérico fuera de este rango es un error. 

print ("-- Programa que da el resultado de la nota final --");

nota = int(input("Introduce la nota: "));

if (nota < 5):
    print ("Suspenso, tu nota es: ", nota);
elif (nota < 6):
    print ("Suficiente, tu nota : ", nota);
elif (nota < 7):
    print ("Bien, tu nota es: ", nota);
elif (nota < 9):
    print ("Notable, tu nota es: ", nota);
elif (nota < 10):
    print ("Sobresaliente, tu nota es: ", nota);
elif (nota == 10):
    print ("Matrícula de honor, tu nota es: ", nota);
else:
    print ("ERROR, nota incorrecta o no proporcionada.");