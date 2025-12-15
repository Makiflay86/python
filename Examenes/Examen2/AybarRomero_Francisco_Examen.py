""" NOMBRE Y APELLIDOS:
Desarrolla un programa en Python que gestione un sistema de biblioteca.No hace falta que
comentes cada cosa que realices pero sí lo que consideres debería saber otro compañero
tuyo, para cuando te vayas de vacaciones y tu compañero debe manipular tu código. Este
programa debe cumplir los siguientes requisitos:
1.Define una clase base Material que tenga atributos comunes a todos los materiales de
la biblioteca, como:
id (único para cada material)
título
autor
año de publicación
2.Crea dos clases que hereden de Material:
Libro: Incluye atributos adicionales como género (debe seleccionarse entre una lista
predefinida: "Ficción", "No Ficción", "Terror", "Ciencia") y número de páginas (debe ser
mayor a 0).
Revista: Incluye atributos adicionales como número de edición y mes de publicación (debe
seleccionarse entre los meses válidos: "Enero", "Febrero", ..., "Diciembre")
3.Utiliza un diccionario para almacenar los materiales, donde la clave sea el id y el
valor sea un objeto de tipo Libro o Revista.
4.Mantén una lista de todos los id existentes para verificar que no se repitan al agregar
nuevos materiales.
5. Generar Estadísticas:debe devolver todos estos valores
Total de materiales registrados.
Número de libros y revistas.
Promedio de páginas para los libros.
Ayuda: se puede usar la siguiente función: Ej: isinstance(m, Libro)--> devuelve true si
el objeto m es de tipo Libro
6.Implementa un menú que permita al usuario realizar las siguientes acciones:
Agregar Material: Permite al usuario agregar un nuevo Libro o Revista.
Listar Materiales: Muestra una lista de todos los materiales registrados con sus detalles.
Elije la forma de presentación más adecuada para que el usuario lo vea claro.
Buscar Material por ID: Permite al usuario buscar un material específico por su id.
Eliminar Material: Elimina un material específico usando su id.
Generar Estadísticas
Salir: Termina la ejecución del programa.
FORMATO DEL MENÚ
a) Agregar Material.
b) Listar Materiales.
c) Buscar Material por ID.
d) Eliminar Material.
e) Generar Estadísticas.
f) Salir. """


# 1 - Clase Material

   

class Material:
    def __init__(self, titulo, autor, anioPublicacion, id):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        if anioPublicacion < 0:
            raise ValueError("ERROR: El año de publicación debe ser mayor a 0.")
        else:
            self.anioPublicacion = anioPublicacion


    def toString(self):
        print(f"Identificador: {self.id}; Titulo: {self.titulo}; Autor: {self.autor}; Año de Publicación: {self.anioPublicacion}")



class Libro(Material):
    
    def __init__(self, titulo, autor, anioPublicacion, genero, numPaginas, id):
        super().__init__(titulo, autor, anioPublicacion, id)
        self.genero = genero
        if numPaginas < 0:
            raise ValueError("ERROR: El número de páginas debe ser mayor a 0.")
        else:
            self.numPaginas = numPaginas
        
    def toString(self):
        print(f"Identificador: {self.id}; Titulo: {self.titulo}; Autor: {self.autor}; Año de Publicación: {self.anioPublicacion}; Genero: {self.genero}; Número de Páginas: {self.numPaginas}.")

    
    def getNumPaginas(self):
        return self.numPaginas



class Revista(Material):
    def __init__(self, titulo, autor, anioPublicacion, numEdicion, mesPubli, id):
        super().__init__(titulo, autor, anioPublicacion, id)
        if numEdicion < 0:
            raise ValueError("ERROR: El número de edición debe ser mayor a 0.")
        else:
            self.numEdicion = numEdicion

        self.mesPubli = mesPubli
    
    def toString(self):
        print(f"Identificador: {self.id}; Titulo: {self.titulo}; Autor: {self.autor}; Año de Publicación: {self.anioPublicacion}; Número de Edición: {self.numEdicion}; Mes de Publicación: {self.mesPubli}.")


lista = {}
lista[1] = Libro("Las increibles aventuras de Doraemon y Novita", "Francisco", 1805, "Ficción", 280, 1)
lista[2] = Revista("IronMan vs SpiderMan", "Seldon", 1950, 5, 12, 2)

ides = {}
ides[1] = 1
ides[2] = 2

def addId():
    iMax = 0
    for i in ides.keys():
        iMax += ides[i]

    ides[iMax] = iMax
    
    return iMax






def agregarMaterial():
    print("")
    print(" - Agregar un nuevo Libro o Revista - ")
    print("=" * 40)
    salir = False
    while not salir:
        try:
            print("¿Qué quieres añadir?")
            print("1. Libro")
            print("2. Revista")
            opcion = int(input("Opcion: "));

            match (opcion):
                case 1:
                    print()
                    print("Añadiendo un Libro")

                    titulo = input("Introduce un titulo: ").strip()
                    autor = input("Introduce el autor: ").strip()
                    anioPubli = int(input("Introduce el año de publicación: ").strip())
                    if anioPubli < 0:
                        salir = False
                        raise ValueError("ERROR: El año de publicación debe ser mayor a 0.")
                    

                    gen = False
                    while not gen:
                        print("Elige el genero... ")
                        print("1. Ficción")
                        print("2. No Ficción")
                        print("3. Terror")
                        print("4. Ciencia")
                    
                        opcion = int(input("Opción: "))
                        if (opcion == 1): genero = "Ficción"
                        elif (opcion == 2): genero = "No Ficción"
                        elif (opcion == 3): genero = "Terror"
                        elif (opcion == 4): genero = "Ciencia"
                        else: print("ERROR: Opción incorrecta."); gen = False

                        gen = True


                    numPaginas = int(input("Introduce el número de páginas: ").strip())
                    idee = addId();

                    lista[idee] = Libro(titulo, autor, anioPubli, genero, numPaginas, idee)
                    print("Libro añadida")


                    print("")
                    input("Enter para continuar...")
                    print("")

                    salir = True
                    pass

                case 2:
                    print()
                    print("Añadiendo una Revista")

                    titulo = input("Introduce un titulo: ").strip()
                    autor = input("Introduce el autor: ").strip()
                    anioPubli = int(input("Introduce el año de publicación: ").strip())
                    numEdicion = int(input("Introduce el numero de edición: ").strip())
                    
                    mes = False
                    while not mes:
                        print("Elige el mes... ")
                        print("1. Enero")
                        print("2. Febrero")
                        print("3. Marzo")
                        print("4. Abril")
                        print("5. Mayo")
                        print("6. Junio")
                        print("7. Julio")
                        print("8. Agosto")
                        print("9. Septiembre")
                        print("10. Octubre")
                        print("11. Noviembre")
                        print("12. Diciembre")
                        
                        opcion = int(input("Opción: "))
                        if (opcion == 1): mesPubli = "Enero"
                        elif (opcion == 2): mesPubli = "Febrero"
                        elif (opcion == 3): mesPubli = "Marzo"
                        elif (opcion == 4): mesPubli = "Abril"
                        elif (opcion == 5): mesPubli = "Mayo"
                        elif (opcion == 6): mesPubli = "Junio"
                        elif (opcion == 7): mesPubli = "Julio"
                        elif (opcion == 8): mesPubli = "Agosto"
                        elif (opcion == 9): mesPubli = "Septiembre"
                        elif (opcion == 10): mesPubli = "Octubre"
                        elif (opcion == 11): mesPubli = "Noviembre"
                        elif (opcion == 12): mesPubli = "Diciembre"
                        else: print("ERROR: Opción incorrecta."); mes = False

                        mes = True

                    idee = addId();

                    
                    lista[idee] = Revista(titulo, autor, anioPubli, numEdicion, mesPubli, idee)
                    print("Revista añadida")


                    print("")
                    input("Enter para continuar...")
                    print("")

                    salir = True
                    pass

                case _:
                    print("Opción incorrecta.")
                    print()

                    input("Enter para continuar...")
                    print("")

                    salir = False

            
            

        except ValueError:
            print("ERROR: Ocurrió un problema inesperado.")
            print("")
            salir = False

    return False



def listarMateriales():
    print("")
    print(" - Listar todos la lista de materiales - ")
    print("=" * 40)
    salir = False
    while not salir:
        try:
            if not lista:
                print("ERROR: No existe ninguna lista de materiales.")
            else:
                for i in lista.keys():
                    lista[i].toString()

            print("")
            input("Enter para continuar...")
            print("")

            salir = True

        except ValueError:
            print("ERROR: Ocurrió un problema inesperado.")
            print("")
            salir = False

    return False



def buscarId():
    print("")
    print(" - Buscar por ID el material - ")
    print("=" * 40)

    salir = False
    while not salir:
        try:
            if not lista:
                print("ERROR: No existe ninguna lista de materiales.")
            else:
                ida = int(input("Introduce el id a buscar: ").strip())
                
                for i in lista.keys():
                    if ida in lista.keys():
                        lista[ida].toString()
                        break
                else:
                    print("No se ha encontrado")


            print("")
            input("Enter para continuar...")
            print("")
            salir = True

        except ValueError:
            print("ERROR: Ha ocurrido un error inesperado.")
            print("")
            salir = False

    return False


def delMaterial():
    print("")
    print(" - Eliminar un material por ID - ")
    print("=" * 40)

    salir = False
    while not salir:
        try:
            if not lista:
                print("ERROR: No existe ninguna lista de materiales.")
            else:
                ida = int(input("Introduce el id a eliminar: ").strip())
                
                if ida in lista.keys():
                    del lista[ida]
                    print("Eliminado")
                else:
                    print("No se ha encontrado")



            print("")
            input("Enter para continuar...")
            print("")
            salir = True

        except ValueError:
            print("ERROR: Ha ocurrido un error inesperado.")
            print("")
            salir = False

    return False



def generarStats():
    print("")
    print(" - Generar la estadistica - ")
    print("=" * 40)

    print("Total de materiales registrados")
    
    print()
    

    print("Número de libros y revistas")
    print(Material.totalCreados())
    print()


    print("Promedio de páginas para los libros")
    promedio = 0
    totalPaginas = 0
    totalLibros = 0
    for i in lista.keys():
        if isinstance(i, Libro):
            totalLibros+=1
            totalPaginas += i.getNumPaginas()
    
    if totalLibros == 0:
        print("Promedio -> 0")
    else:
        promedio = totalPaginas / totalLibros
        print("Promedio -> ",promedio)

    
    print("")
    input("Enter para continuar...")
    print("")

    return False





def menu():
    print("")
    print("-- MENú DE OPCIONES --")
    print("a) Agregar Material.")
    print("b) Listar Materiales.")
    print("c) Buscar Material por ID.")
    print("d) Eliminar Material.")
    print("e) Generar Estadísticas.")
    print("f) Salir.")



def opcion():
    salir = False
    while not salir:
        try:
            op = input("Opción: ").lower()
            print("")

            match op:
                case "a":
                    salir = agregarMaterial()
                    
                case "b":
                    salir = listarMateriales()

                case "c":
                    salir = buscarId()

                case "d":
                    salir = delMaterial()
                
                case "e":
                    salir = generarStats()
                
                case "f":
                    salir = True
                
                case _:
                    print("ERROR: No es una opción válida.")
                    print("")
                    input("Pulsa enter para continuar...")        
                    salir = False

    
            return salir
        except ValueError:
            print("ERROR: Ocurrió un problema inesperado.")



salir = False;

while not salir:
    menu()
    
    if not opcion():
        salir = False
    else:
        salir = True

else:
    print("")
    print("FINALIZANDO PROGRAMA...")
