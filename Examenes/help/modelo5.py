## SOLUCIÓN MODELO DE EXAMEN 5: INTEGRACIÓN Y VERIFICACIÓN

# ----------------------------------------------------------------------
# PUNTO 1: Herencia y Promedio Ponderado
# ----------------------------------------------------------------------

class Empleado:
    """Clase base con nombre y salario."""
    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base

class Gerente(Empleado):
    """Clase derivada que maneja proyectos y calcula bono."""
    def __init__(self, nombre: str, salario_base: float, proyectos: dict[str, int]):
        super().__init__(nombre, salario_base)
        self.proyectos = proyectos

    def calcular_bono(self, factor: float) -> float:
        """Calcula el bono basado en el promedio de impacto de proyectos."""
        if not self.proyectos:
            return 0.0
            
        # Calcular promedio
        puntuaciones = self.proyectos.values()
        promedio = sum(puntuaciones) / len(puntuaciones)
        
        # Aplicar lógica de bonificación
        if promedio >= 7.0:
            return promedio * factor
        else:
            return 0.0

# ----------------------------------------------------------------------
# PUNTO 2: Diccionario Inverso y Validación (Try-Except)
# ----------------------------------------------------------------------

def invertir_y_validar(diccionario: dict[str, int]) -> dict[int, str]:
    """Invierte claves y valores, devolviendo {} si hay valores duplicados."""
    try:
        diccionario_inverso = {v: k for k, v in diccionario.items()}
        
        # Comprobación de duplicidad (la longitud debe ser la misma)
        if len(diccionario_inverso) != len(diccionario):
             # Esto ocurre si dos claves originales tenían el mismo valor
             raise ValueError("Valores duplicados detectados.")

        return diccionario_inverso
        
    except (TypeError, ValueError) as e:
        # Captura el error si el valor original no es hasheable (ej. lista) o si detectamos duplicidad
        # En el caso de ValueError, es porque detectamos la duplicidad al comprobar la longitud.
        return {}

# ----------------------------------------------------------------------
# PUNTO 3: Análisis de Texto y Conteo
# ----------------------------------------------------------------------

def analizar_texto_vocales(texto: str) -> tuple[int, int]:
    """Devuelve (conteo_consonantes, longitud_palabra_más_larga)."""
    
    # Conjunto de vocales para chequeo rápido
    vocales = "aeiouáéíóú"
    conteo_consonantes = 0
    
    # Calcular longitud de palabra más larga
    palabras = texto.split()
    longitud_maxima = 0
    if palabras:
        longitud_maxima = max(len(p) for p in palabras)
        
    # Calcular conteo de consonantes
    for caracter in texto.lower():
        # Ignorar espacios y verificar si es alfabético
        if caracter.isalpha() and caracter not in vocales:
            conteo_consonantes += 1
            
    return (conteo_consonantes, longitud_maxima)

# ----------------------------------------------------------------------
# PUNTO 4: Búsqueda y Filtrado de Tuplas
# ----------------------------------------------------------------------

def filtrar_por_rango_precio(articulos: list[tuple[str, float, int]], precio_min: float, precio_max: float) -> list[str]:
    """Devuelve una lista de nombres de productos dentro del rango de precios [min, max]."""
    nombres_filtrados = []
    
    for nombre, precio, stock in articulos:
        # El precio está en el índice 1 de la tupla
        if precio_min <= precio <= precio_max:
            nombres_filtrados.append(nombre)
            
    return nombres_filtrados

# ----------------------------------------------------------------------
# PUNTO 5: Validación de Identificador
# ----------------------------------------------------------------------

def validar_identificador(id_codigo: str) -> bool:
    """Valida ID: longitud 6, 3 mayúsculas alfabéticas, 3 dígitos, y en lista permitida."""
    
    # Lista de prefijos permitidos (Punto 5.4)
    prefijos_permitidos = ['ADM', 'DEV', 'MKT']
    
    # 1. Longitud exacta de 6
    if len(id_codigo) != 6:
        return False
        
    # 2. Partición del código
    letras = id_codigo[:3]
    digitos = id_codigo[3:]
    
    # 3. Primeros 3: Alfabéticos, Mayúsculas Y en lista permitida
    if not (letras.isalpha() and letras.isupper() and letras in prefijos_permitidos):
        return False
        
    # 4. Últimos 3: Dígitos numéricos
    if not digitos.isdigit():
        return False
        
    return True # Todas las validaciones pasaron

# ----------------------------------------------------------------------
# PRUEBAS DE EJECUCIÓN DEL MODELO 5
# ----------------------------------------------------------------------

if __name__ == "__main__":
    print("\n--- PRUEBAS DE FUNCIONALIDAD DEL MODELO 5 ---")

    # PUNTO 1: Herencia y Promedio Ponderado
    proyectos_ok = {"A": 8, "B": 7, "C": 9} # Promedio = 8.0 (>= 7)
    proyectos_fail = {"D": 5, "E": 6} # Promedio = 5.5 (< 7)
    gerente_ok = Gerente("Eva", 50000.0, proyectos_ok)
    gerente_fail = Gerente("Juan", 40000.0, proyectos_fail)
    bono_ok = gerente_ok.calcular_bono(500.0)
    bono_fail = gerente_fail.calcular_bono(500.0)
    print(f"\n[Punto 1] Bono OK (Promedio 8.0 * 500): {bono_ok:.2f}") # Esperado: 4000.00
    print(f"[Punto 1] Bono FAIL (Promedio 5.5): {bono_fail:.2f}") # Esperado: 0.00

    # PUNTO 2: Diccionario Inverso y Validación
    dicc_ok = {"A": 10, "B": 20, "C": 30}
    dicc_fail = {"X": 10, "Y": 20, "Z": 10} # 'X' y 'Z' tienen el mismo valor (10)
    inverso_ok = invertir_y_validar(dicc_ok)
    inverso_fail = invertir_y_validar(dicc_fail)
    print(f"\n[Punto 2] Inverso OK: {inverso_ok}") # Esperado: {10: 'A', 20: 'B', 30: 'C'}
    print(f"[Punto 2] Inverso FAIL (Duplicidad): {inverso_fail}") # Esperado: {}

    # PUNTO 3: Análisis de Texto y Conteo
    texto_test = "El programador usa Python."
    conteo_res = analizar_texto_vocales(texto_test)
    # Consonantes: l, p, r, g, r, m, d, r, s, P, t, h, n (13)
    # Longitud Máxima: programador (11)
    print(f"\n[Punto 3] Análisis de '{texto_test}': (Consonantes, Long. Máxima) -> {conteo_res}") # Esperado: (13, 11)

    # PUNTO 4: Búsqueda y Filtrado de Tuplas
    lista_articulos = [
        ("Teclado", 15.99, 100), 
        ("Monitor", 125.00, 50), 
        ("Mouse", 8.50, 200),
        ("Portátil", 750.00, 20)
    ]
    filtrados_rango = filtrar_por_rango_precio(lista_articulos, 10.0, 150.0)
    print(f"\n[Punto 4] Filtrados en rango [10.0, 150.0]: {filtrados_rango}") # Esperado: ['Teclado', 'Monitor']

    # PUNTO 5: Validación de Identificador
    id_ok = validar_identificador("MKT007") # Válido
    id_fail_len = validar_identificador("DEV0070") # Inválido: Longitud
    id_fail_prefix = validar_identificador("XYZ123") # Inválido: Prefijo no permitido
    id_fail_char = validar_identificador("ADMAB3") # Inválido: Digitos (AB)
    print(f"\n[Punto 5] 'MKT007' (OK): {id_ok}") # Esperado: True
    print(f"[Punto 5] 'DEV0070' (FAIL - Len): {id_fail_len}") # Esperado: False
    print(f"[Punto 5] 'XYZ123' (FAIL - Prefijo): {id_fail_prefix}") # Esperado: False
    print(f"[Punto 5] 'ADMAB3' (FAIL - Dígitos): {id_fail_char}") # Esperado: False