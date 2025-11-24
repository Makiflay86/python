""" Clase Persona """

class Persona:
    def __init__(self, nombre = "", apellido = "", dni = "", edad = 0):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__edad = edad

        self.__nombreCompleto = f"{nombre} {apellido}"



    """ GETTERS """

    """ Mostrar nombre """
    def getNombre(self):
        return self.__nombre

    """ Mostrar apellido """
    def getApellido(self):
        return self.__apellido
    
    """ Mostrar dni """
    def getDni(self):
        return self.__dni
    
    """ Mostrar edad """
    def getEdad(self):
        return self.__edad
    
    """ Mostrar nombre completo """
    def getNombreCompleto(self):
        return self.__nombreCompleto
    


    """ SETTERS """

    """ Cambiar nombre """
    def setNombre(self, nombre):
        if len(nombre) < 0:
            return ("ERROR: El nombre no puede estar vacío.")
        else:
            self.__nombre = nombre.upper()

    """ Cambiar apellido """
    def setApellido(self, apellido):
        if len(apellido) < 0:
            return ("ERROR: El apellido no puede estar vacío.")
        else:
            self.__apellido = apellido.upper()

    """ Cambiar dni """
    def setDni(self, dni):
        if len(dni) < 0:
            return ("ERROR: El dni no puede estar vacío.")
        else:
            self.__dni = dni.upper()

    """ Cambiar edad """
    def setEdad(self, edad):
        if edad < 0:
            return ("ERROR: La edad no puede ser menor a 0.")
        else:
            self.__edad = edad



    """ El toString() de toda la vida """
    def mostrar(self):
        print(f"Nombre Completo: {self.getNombreCompleto} DNI: {self.getDni} Edad: {self.getEdad}.")



    """ Es mayor de edad """
    def mayorDeEdad(self, edad):
        mensaje = False
        if edad >= 18:
            mensaje = True
        
        return mensaje
    





""" Clase Cuenta """

class Cuenta(Persona):
    def __init__(self, titular, cantidad):
        self.__titular = titular
        self.__cantidad = cantidad



    """ GETTERS """

    """ Mostrar titular """
    def getTitular(self):
        return self.__titular

    """ Mostrar cantidad """
    def getCantidad(self):
        return self.__cantidad
    


    """ SETTERS """

    """ Cambiar titular """
    def setTitular(self, nombre):
        pass #Tiene que ser una persona

    

    """ El toString() de toda la vida """
    def mostrar(self):
        print(f"a")



    """ Es mayor de edad """
    def mayorDeEdad(self, edad):
        mensaje = False
        if edad >= 18:
            mensaje = True
        
        return mensaje
    
