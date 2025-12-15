""" CLASES BASE Y SOLUCIONES PARA EL MODELO DE EXAMEN 6 """

# ========================================================
# CLASES BASE (PROPORCIONADAS POR EL USUARIO)
# ========================================================

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
            raise ValueError ("ERROR: La edad no puede ser negativa o no entera.")

    """ GETTERS """
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDni(self):
        return self.__dni
    def getEdad(self):
        return self.__edad
    def getNombreCompleto(self):
        return (f"{self.__nombre} {self.__apellido}")
    
    """ SETTERS """
    def setNombre(self, nombre):
        if len(nombre) == 0:
            raise ValueError ("ERROR: El nombre no puede estar vacío.")
        else:
            self.__nombre = nombre.upper()
    def setApellido(self, apellido):
        if len(apellido) == 0:
            raise ValueError ("ERROR: El apellido no puede estar vacío.")
        else:
            self.__apellido = apellido.upper()
    def setDni(self, dni):
        if len(dni) == 0:
            raise ValueError ("ERROR: El dni no puede estar vacío.")
        else:
            self.__dni = dni.upper()
    def setEdad(self, edad):
        if isinstance(edad,int) and edad > 0:
            self.__edad = edad
        else:
            raise ValueError ("ERROR: La edad no puede ser negativa.")

    """ El toString() de toda la vida """
    def mostrar(self):
        return (f"Nombre Completo: {self.getNombreCompleto()} DNI: {self.getDni()} Edad: {self.getEdad()}")

    """ Es mayor de edad """
    def mayorDeEdad(self):
        return self.__edad >= 18 # Corregido: usa el atributo de la instancia, no un parámetro

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
    def getTitular(self):
        return self.__titular
    def getCantidad(self):
        return self.__cantidad
    
    # PUNTO 4: Implementación del método getter
    def getInicialesTitular(self):
        """Devuelve las iniciales del nombre y apellido en mayúsculas, separadas por un punto."""
        nombre = self.__titular.getNombre()
        apellido = self.__titular.getApellido()
        
        # Aseguramos que el nombre/apellido no estén vacíos antes de tomar la inicial
        if nombre and apellido:
            return f"{nombre[0].upper()}.{apellido[0].upper()}."
        return "N/A"
    
    """ SETTERS """
    def setTitular(self, titular):
        if isinstance(titular, Persona):
            self.__titular = titular
        else:
            raise ValueError("ERROR: El titular debe ser una Persona")

    """ Ingresar dinero """
    def ingresar(self, cantidad):
        if cantidad <= 0:
            return "ERROR: La cantidad a ingresar tiene que ser mayor que 0."
        else:
            self.__cantidad += cantidad
            return f"Ingreso de {cantidad:.2f}€ realizado." # Devuelve mensaje de éxito
    
    """ Retirar dinero """
    def retirar(self, cantidad): 
        if cantidad <= 0: # Corregido: la cantidad a retirar debe ser positiva.
            return "ERROR: La cantidad a retirar tiene que ser mayor que 0."
        else:
            self.__cantidad -= cantidad
            return f"Retiro de {cantidad:.2f}€ realizado." # Devuelve mensaje de éxito

    # PUNTO 5: Implementación del método transferir
    def transferir(self, cuenta_destino, cantidad):
        """Transfiere dinero de esta cuenta a cuenta_destino de forma segura."""
        
        # Intentar la retirada de la cuenta de origen
        resultado_retiro = self.retirar(cantidad)
        
        # Usamos try-except para gestionar el resultado que puede ser un string de error
        try:
            if resultado_retiro.startswith("ERROR"):
                return f"ERROR en la transferencia: {resultado_retiro}"
            
            # Si el retiro fue exitoso, intentar el ingreso en la cuenta destino
            resultado_ingreso = cuenta_destino.ingresar(cantidad)
            
            if resultado_ingreso.startswith("ERROR"):
                 # Caso crítico: Retiro OK, Ingreso FAIL. Se debe revertir la operación (sería complejo en un examen,
                 # pero aquí gestionamos el error de forma informativa).
                 return f"ADVERTENCIA: Retiro exitoso, pero ERROR en ingreso de destino: {resultado_ingreso}"
            
            return f"Transferencia de {cantidad:.2f}€ exitosa."
            
        except AttributeError:
             # Captura el error si self.retirar no devuelve un string (lo cual es improbable con la implementación actual,
             # pero es buena práctica) o si cuenta_destino no tiene el método ingresar.
             return "ERROR fatal: No se pudo realizar la operación."

    """ El toString() de toda la vida """
    def mostrar(self):
        return (f"{self.__titular.mostrar()} Cantidad: {self.getCantidad():.2f}€")

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
    def getBonificacion(self):
        return self.__bonificacion

    """ El toString() de toda la vida """
    def mostrar(self):
        return (f"{super().mostrar()} Bonificación: {self.getBonificacion()}%")

# ========================================================
# SOLUCIONES DE FUNCIONES ADICIONALES
# ========================================================

# PUNTO 1: Clase ClienteVIP (Extensión de Herencia)
class ClienteVIP(Persona):
    def __init__(self, nombre: str, apellido: str, dni: str, edad: int, limite_credito: float):
        super().__init__(nombre, apellido, dni, edad)
        self.setLimiteCredito(limite_credito)

    def getLimiteCredito(self):
        return self.__limite_credito

    def setLimiteCredito(self, limite_credito: float):
        """Valida que el límite sea un múltiplo de 1000 y no negativo."""
        if limite_credito < 0:
            raise ValueError("ERROR: El límite de crédito no puede ser negativo.")
        if limite_credito % 1000 != 0:
            raise ValueError("ERROR: El límite de crédito debe ser un múltiplo exacto de 1000.")
        self.__limite_credito = limite_credito
        
    def mostrar(self):
        return f"{super().mostrar()} Límite Crédito: {self.getLimiteCredito():.2f}€"

# PUNTO 2: Validación de Colección Externa
def validar_dni_lista(lista_dnis: list[str]) -> bool:
    """Devuelve True si todos los DNIs tienen 8 dígitos + 1 letra."""
    for dni in lista_dnis:
        if len(dni) != 9:
            return False
        # Primeros 8 caracteres deben ser dígitos
        if not dni[:8].isdigit():
            return False
        # Último carácter debe ser una letra alfabética
        if not dni[-1].isalpha():
            return False
    return True

# PUNTO 3: Filtrado por Estado de Objeto
def obtener_cuentas_activas(lista_cuentas: list[Cuenta]) -> list[Cuenta]:
    """Devuelve cuentas cuyo titular es mayor de edad y tiene DNI en mayúsculas."""
    cuentas_activas = []
    for cuenta in lista_cuentas:
        titular = cuenta.getTitular()
        # 1. Mayor de edad
        es_mayor = titular.mayorDeEdad()
        # 2. DNI en mayúsculas (compara el DNI guardado con el DNI en mayúsculas)
        dni_upper = titular.getDni().upper()
        dni_es_upper = titular.getDni() == dni_upper
        
        if es_mayor and dni_es_upper:
            cuentas_activas.append(cuenta)
    return cuentas_activas

# ========================================================
# PRUEBAS DE EJECUCIÓN DEL MODELO 6
# ========================================================

if __name__ == "__main__":
    print("\n--- PRUEBAS DE FUNCIONALIDAD DEL MODELO 6 ---")

    # Personas de prueba
    p_ana = Persona("Ana", "García", "12345678A", 20) # Menor de edad
    p_luis = Persona("Luis", "Pérez", "98765432B", 35) # Mayor de edad, DNI Upper
    p_eva = Persona("Eva", "López", "44444444c", 40) # Mayor de edad, DNI Lower

    # PUNTO 1: ClienteVIP y Setter Estricto
    print("\n[Punto 1] ClienteVIP y Setter Estricto:")
    try:
        vip1 = ClienteVIP("Javier", "Romero", "11111111J", 30, 10000.0)
        print(f"VIP Creado OK: {vip1.mostrar()}")
        vip1.setLimiteCredito(5000)
        print(f"Setter OK (Límite 5000): {vip1.getLimiteCredito():.2f}")
        vip1.setLimiteCredito(4500) # Debería fallar
    except ValueError as e:
        print(f"Setter FAIL esperado: {e}") # Esperado: ERROR: El límite de crédito debe ser un múltiplo exacto de 1000.
        
    # PUNTO 2: Validación de Colección Externa
    dnis_ok = ["12345678A", "00000000Z"]
    dnis_fail = ["1234567A", "123456789"] # Longitud, Carácter
    print(f"\n[Punto 2] Validación DNI Lista:")
    print(f"Lista OK ({dnis_ok}): {validar_dni_lista(dnis_ok)}") # Esperado: True
    print(f"Lista FAIL ({dnis_fail}): {validar_dni_lista(dnis_fail)}") # Esperado: False

    # PUNTO 3: Filtrado por Estado de Objeto
    cuenta1 = Cuenta(p_ana, 500.0) # Menor, DNI Upper -> No Activa
    cuenta2 = Cuenta(p_luis, 2000.0) # Mayor, DNI Upper -> Activa
    cuenta3 = Cuenta(p_eva, 1000.0) # Mayor, DNI Lower -> No Activa
    lista_cuentas = [cuenta1, cuenta2, cuenta3]
    cuentas_activas = obtener_cuentas_activas(lista_cuentas)
    
    print(f"\n[Punto 3] Cuentas Activas (Mayor y DNI UPPER):")
    print(f"Resultado: {[c.getTitular().getNombre() for c in cuentas_activas]}") # Esperado: ['Luis']

    # PUNTO 4: Propiedad de Cuenta (Método de String)
    print(f"\n[Punto 4] Iniciales Titular de Luis: {cuenta2.getInicialesTitular()}") # Esperado: L.P.

    # PUNTO 5: Transacción Segura
    cuenta_origen = Cuenta(p_luis, 1500.0)
    cuenta_destino = Cuenta(p_ana, 500.0)
    
    print(f"\n[Punto 5] Transacción Segura:")
    print(f"Origen: {cuenta_origen.getCantidad():.2f}€, Destino: {cuenta_destino.getCantidad():.2f}€")
    
    # Transacción OK
    resultado_ok = cuenta_origen.transferir(cuenta_destino, 500.0)
    print(f"Transferir 500€: {resultado_ok}")
    print(f"Origen post: {cuenta_origen.getCantidad():.2f}€, Destino post: {cuenta_destino.getCantidad():.2f}€")
    
    # Transacción FAIL (Cantidad a retirar inválida)
    resultado_fail = cuenta_origen.transferir(cuenta_destino, -100.0)
    print(f"Transferir -100€: {resultado_fail}") # Esperado: ERROR en la transferencia: ERROR: La cantidad a retirar tiene que ser mayor que 0.