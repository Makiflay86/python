## Solución Modelo de Examen 1: Estructuras y Manipulación de Datos

# Ejercicio 1: Gestión de Productos (Clases, Lista, Función)
class Producto:
    """Clase para representar un producto con nombre y precio."""
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

def mostrar_inventario(inventario: list[Producto]):
    """Imprime los detalles de cada producto en la lista de inventario."""
    print("\n--- INVENTARIO DE PRODUCTOS ---")
    for producto in inventario:
        print(f"Nombre: {producto.nombre:<15} - Precio: {producto.precio:.2f}€")
    print("-------------------------------\n")

# Ejercicio 2: Análisis de Texto (Función, String, Diccionario)
def contar_vocales(texto: str) -> dict:
    """Cuenta la aparición de vocales (incluidas las acentuadas) en un texto."""
    vocales_a_contar = 'aeiouáéíóú'
    conteo = {vocal: 0 for vocal in vocales_a_contar}
    
    # Convertir el texto a minúsculas para un conteo uniforme
    texto_lower = texto.lower()
    
    for caracter in texto_lower:
        if caracter in conteo:
            conteo[caracter] += 1
            
    return conteo

# --- Código Principal del Examen ---

# Ejercicio 1: Creación de instancias y lista
producto1 = Producto("Monitor 27", 199.99)
producto2 = Producto("Teclado Mecánico", 75.50)
producto3 = Producto("Ratón Ergonómico", 35.00)

inventario_principal = [producto1, producto2, producto3]

# Ejercicio 1: Llamada a la función
mostrar_inventario(inventario_principal)

# Ejercicio 2: Prueba de la función contar_vocales
frase_ejemplo = "La tecnología AvAnza rÁpidamente."
conteo_resultado = contar_vocales(frase_ejemplo)

print("--- ANÁLISIS DE VOCALES ---")
print(f"Frase Original: '{frase_ejemplo}'")
print(f"Conteo de Vocales: {conteo_resultado}")
print("---------------------------\n")