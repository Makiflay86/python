## Solución Modelo de Examen 2: Herencia y Colecciones Complejas

# Ejercicio 1: Sistema de Calificaciones (Clases, Herencia, Diccionario)
class Persona:
    """Clase base con atributos nombre y edad."""
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):
    """Clase derivada que añade notas (diccionario) y método de promedio."""
    def __init__(self, nombre: str, edad: int, notas: dict[str, float]):
        super().__init__(nombre, edad)
        self.notas = notas

    def calcular_promedio(self) -> float:
        """Calcula el promedio de las notas del estudiante."""
        if not self.notas:
            return 0.0
        return sum(self.notas.values()) / len(self.notas)

# Ejercicio 2: Búsqueda en Secuencias (Función, Lista, Tupla)
def encontrar_mas_caro(articulos: list[tuple[str, float]]) -> tuple[str, float]:
    """Recorre una lista de tuplas (nombre, precio) y devuelve el artículo más caro."""
    if not articulos:
        return ("", 0.0) # Devuelve una tupla vacía o con valores por defecto si la lista está vacía

    mas_caro = articulos[0] # Inicializa con el primer artículo
    precio_maximo = articulos[0][1] # Inicializa con el precio del primer artículo

    for nombre, precio in articulos[1:]: # Itera desde el segundo elemento
        if precio > precio_maximo:
            precio_maximo = precio
            mas_caro = (nombre, precio)
            
    return mas_caro

# --- Código Principal del Examen ---

# Ejercicio 1: Creación de instancia y prueba
notas_luis = {"Programación": 8.5, "Bases de Datos": 7.0, "Sistemas": 9.0}
estudiante_luis = Estudiante("Luis García", 20, notas_luis)
promedio = estudiante_luis.calcular_promedio()

print("--- SISTEMA DE CALIFICACIONES ---")
print(f"Estudiante: {estudiante_luis.nombre}, Edad: {estudiante_luis.edad}")
print(f"Notas: {estudiante_luis.notas}")
print(f"Promedio de Notas: {promedio:.2f}")
print("---------------------------------\n")

# Ejercicio 2: Creación de lista de tuplas y prueba
lista_articulos = [("Laptop", 1200.00), ("Monitor", 350.50), ("Teclado", 150.99), ("Mouse", 75.00)]
articulo_caro = encontrar_mas_caro(lista_articulos)

print("--- BÚSQUEDA DE ARTÍCULO MÁS CARO ---")
print(f"Lista de Artículos: {lista_articulos}")
print(f"Artículo más caro encontrado: Nombre: {articulo_caro[0]}, Precio: {articulo_caro[1]:.2f}€")
print("-------------------------------------\n")