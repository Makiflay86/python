## Solución Modelo de Examen 3: Control de Flujo y Validación

# Ejercicio 1: Clasificación de Vehículos (Clases, Herencia, Lista, Función)
class Vehiculo:
    """Clase base con un método de descripción genérico."""
    def describir(self):
        print("Este es un vehículo genérico.")

class Coche(Vehiculo):
    """Clase derivada que maneja accesorios."""
    def __init__(self):
        self.accesorios = []
    
    def describir(self):
        print(f"Este es un Coche con accesorios: {', '.join(self.accesorios) if self.accesorios else 'Ninguno'}.")

    def agregar_accesorio(self, accesorio: str):
        """Añade un accesorio a la lista."""
        self.accesorios.append(accesorio)

class Moto(Vehiculo):
    """Clase derivada simple."""
    def describir(self):
        print("Esta es una Moto.")

def filtrar_coches(lista_vehiculos: list[Vehiculo]) -> list[Coche]:
    """Filtra y devuelve solo los objetos que son instancias de la clase Coche."""
    coches_filtrados = []
    for vehiculo in lista_vehiculos:
        if isinstance(vehiculo, Coche):
            coches_filtrados.append(vehiculo)
    return coches_filtrados

# Ejercicio 2: Validación de Credenciales (Función, Diccionario, String)
def validar_usuarios(credenciales: dict[str, str]) -> dict[str, str]:
    """Valida contraseñas (longitud >= 8 y al menos un dígito) y devuelve usuarios válidos."""
    usuarios_validos = {}
    for usuario, contrasena in credenciales.items():
        # Regla 1: Longitud de al menos 8 caracteres
        longitud_valida = len(contrasena) >= 8
        
        # Regla 2: Contener al menos un dígito numérico
        contiene_digito = any(char.isdigit() for char in contrasena)
        
        if longitud_valida and contiene_digito:
            usuarios_validos[usuario] = contrasena
            
    return usuarios_validos

# --- Código Principal del Examen ---

# Ejercicio 1: Creación de objetos y prueba de filtro
mi_coche = Coche()
mi_coche.agregar_accesorio("GPS")
mi_coche.agregar_accesorio("Techo Solar")
mi_moto = Moto()
lista_mixta = [mi_coche, mi_moto, Coche(), Vehiculo()]
coches_solo = filtrar_coches(lista_mixta)

print("--- CLASIFICACIÓN DE VEHÍCULOS ---")
print(f"Lista Mixta de Vehículos: {len(lista_mixta)} elementos.")
print(f"Coches Filtrados (cantidad): {len(coches_solo)}")
for c in coches_solo:
    c.describir()
print("----------------------------------\n")

# Ejercicio 2: Prueba de validación de credenciales
datos_credenciales = {
    "admin": "Secure123",  # Válido: >=8 y tiene dígito
    "user1": "password",   # Inválido: No tiene dígito
    "user2": "Corto1",     # Inválido: <8 caracteres
    "superu": "ClaveSecreta99" # Válido: >=8 y tiene dígito
}
usuarios_aprobados = validar_usuarios(datos_credenciales)

print("--- VALIDACIÓN DE CREDENCIALES ---")
print(f"Credenciales de Entrada: {datos_credenciales}")
print(f"Usuarios Válidos: {usuarios_aprobados}")
print("----------------------------------\n")