""" Clase Persona """

class Persona:
    def __init__(self, nombre = "", apellido = "", dni = "", edad = 0):
        if len(nombre) == 0:
            raise ValueError ("ERROR: El nombre no puede estar vacío.")
        else:
            self.__nombre = nombre

        if len(apellido) == 0:
            raise ValueError ("ERROR: El apellido no puede estar vacío.")
        else:
            self.__apellido = apellido

        if len(dni) == 0:
            raise ValueError ("ERROR: El dni no puede estar vacío.")
        else:
            self.__dni = dni

        if isinstance(edad,int) and edad > 0:
            self.__edad = edad
        else:
            raise ValueError ("ERROR: La edad no puede ser negativa.")



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
        return (f"{self.__nombre} {self.__apellido}")
    


    """ SETTERS """

    """ Cambiar nombre """
    def setNombre(self, nombre):
        if len(nombre) == 0:
            raise ValueError ("ERROR: El nombre no puede estar vacío.")
        else:
            self.__nombre = nombre.upper()

    """ Cambiar apellido """
    def setApellido(self, apellido):
        if len(apellido) == 0:
            raise ValueError ("ERROR: El apellido no puede estar vacío.")
        else:
            self.__apellido = apellido.upper()

    """ Cambiar dni """
    def setDni(self, dni):
        if len(dni) == 0:
            raise ValueError ("ERROR: El dni no puede estar vacío.")
        else:
            self.__dni = dni.upper()

    """ Cambiar edad """
    def setEdad(self, edad):
        if isinstance(edad,int) and edad > 0:
            self.__edad = edad
        else:
            raise ValueError ("ERROR: La edad no puede ser negativa.")



    """ El toString() de toda la vida """
    def mostrar(self):
        return (f"Nombre Completo: {self.getNombreCompleto()} DNI: {self.getDni()} Edad: {self.getEdad()}")



    """ Es mayor de edad """
    def mayorDeEdad(self, edad):
        mensaje = False
        if edad >= 18:
            mensaje = True
        
        return mensaje
    


# ========================================================



""" Clase Cuenta """

class Cuenta:
    def __init__(self, titular, cantidad = 0.0):
        if isinstance(titular, Persona):
            self.__titular = titular
        else:
            raise ValueError("ERROR: El titular debe ser un objeto de la clase Persona.")
        
        self.__cantidad = float(cantidad)



    """ GETTERS """

    """ Mostrar titular """
    def getTitular(self):
        return self.__titular

    """ Mostrar cantidad """
    def getCantidad(self):
        return self.__cantidad
    


    """ SETTERS """

    """ Cambiar titular """
    def setTitular(self, titular):
        if isinstance(titular, Persona):
            self.__titular = titular
        else:
            raise ValueError("ERROR: El titular debe ser una Persona")



    """ Ingresar dinero """
    def ingresar(self, cantidad):
        if cantidad <= 0:
            return ("ERROR: La cantidad tiene que ser mayor que 0.")
        else:
            self.__cantidad += cantidad
    


    """ Retirar dinero """
    def retirar(self, cantidad): # Puede quedarse en número rojo, es decir la cantidad en negativo
        if cantidad < 0:
            return ("ERROR: La cantidad tiene que ser mayor que 0.")
        else:
            self.__cantidad -= cantidad

    

    """ El toString() de toda la vida """
    def mostrar(self):
        return (f"{self.__titular.mostrar()} Cantidad: {self.getCantidad():.2f}€") # ':.2f' -> Muestra 2 decimales




# ========================================================



""" Clase CuentaJoven """

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad = 0.0, bonificacion = 0):
        super().__init__(titular, cantidad)
        if titular.getEdad() >= 25:
            raise ValueError("ERROR: El titular debe tener menos de 25 años.")

        if bonificacion >= 0 and bonificacion <= 100:
            self.__bonificacion = bonificacion
        else:
            raise ValueError("ERROR: La bonificación debe estar en el rango 0 - 100.")



    """ GETTERS """

    """ Mostrar bonificación """
    def getBonificacion(self):
        return self.__bonificacion



    """ El toString() de toda la vida """
    def mostrar(self):
        return (f"{super().mostrar()} Bonificación: {self.getBonificacion()}%")








""" TESTING """

print("")

try:
    print("Intento crear un 'objeto persona' con edad de negativa")
    p0 = Persona("Francisco", "Aybar", "46351096Q", -19)
    print(p0.mostrar())

except ValueError as e:
    print(e)


print("")
print(25 * "=")
print("")


try:
    print("Intento crear un 'objeto persona' con valores correcto")
    p1 = Persona("Ana", "García", "12345678A", 20)
    cuenta = Cuenta(p1, 1500.50)
    print(cuenta.mostrar())

except ValueError as e:
    print(e)


print("")
print(25 * "=")
print("")


try:
    print("Ingresar 200€")
    cuenta.ingresar(200)
    print(cuenta.mostrar())

except ValueError as e:
    print(e)


print("")
print(25 * "=")
print("")


try:
    print("Retirar 1000€")
    cuenta.retirar(1000)
    print(cuenta.mostrar())

except ValueError as e:
    print(e)


print("")
print(25 * "=")
print("")


try:
    print("Intento crear un objeto 'cuenta joven' con edad de 25")
    p2 = Persona("Marcos", "Gonzaléz", "01234567L", 25)
    cuentaJoven = CuentaJoven(p2, 333, 5)
    print(cuentaJoven.mostrar())

except ValueError as e:
    print(e)

