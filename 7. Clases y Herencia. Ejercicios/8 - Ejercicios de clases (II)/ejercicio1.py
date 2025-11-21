class Persona:
    def __init__(self, nombre, apellido, dni, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad

        self.nombreCompleto = f"{nombre} {apellido}"



    """ Getters y Setters """
 





    """ Este es el métodoo mostrar() """
    def toString(self):
        print(f"Nombre Completo: {self.nombreCompleto} DNI: {self.dni} Edad: {self.edad}.")
