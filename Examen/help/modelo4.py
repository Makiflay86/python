## SOLUCIÓN MODELO DE EXAMEN 4: ROBUSTEZ Y APLICACIÓN DE ESTRUCTURAS

# ----------------------------------------------------------------------
# PUNTO 1: Gestión de Personal (Clases, Herencia, Lista)
# ----------------------------------------------------------------------

class Personal:
    """Clase base para el personal."""
    def __init__(self, nombre: str, id_empleado: str):
        self.nombre = nombre
        self.id_empleado = id_empleado

class Programador(Personal):
    """Clase derivada que añade lenguajes de programación."""
    def __init__(self, nombre: str, id_empleado: str, lenguajes: list[str]):
        super().__init__(nombre, id_empleado)
        # Convertir a minúsculas los lenguajes para búsqueda robusta
        self.lenguajes = [lang.lower() for lang in lenguajes]

def filtrar_por_lenguaje(lista_programadores: list[Programador], lenguaje: str) -> list[Programador]:
    """Devuelve una lista de programadores que manejan el lenguaje dado."""
    lenguaje_lower = lenguaje.lower()
    programadores_filtrados = []
    
    for programador in lista_programadores:
        if lenguaje_lower in programador.lenguajes:
            programadores_filtrados.append(programador)
            
    return programadores_filtrados

# ----------------------------------------------------------------------
# PUNTO 2: Conteo de Caracteres Únicos (Función, String, Diccionario)
# ----------------------------------------------------------------------

def contar_unicos(texto: str) -> dict[str, int]:
    """
    Cuenta caracteres únicos (sin espacios ni distinción de mayúsculas) 
    y devuelve su código ASCII.
    """
    diccionario_unicos = {}
    
    # Manejar caso de cadena vacía
    if not texto:
        return {} 
        
    for caracter in texto.lower():
        # Ignorar espacios
        if caracter == ' ':
            continue
            
        # Almacenar solo si es la primera vez que se ve (carácter único)
        if caracter not in diccionario_unicos:
            diccionario_unicos[caracter] = ord(caracter)
            
    return diccionario_unicos

# ----------------------------------------------------------------------
# PUNTO 3: Análisis de Secuencias Numéricas (Función, Lista, Tupla)
# ----------------------------------------------------------------------

def analizar_numeros(lista_numeros: list) -> tuple[int, int, int]:
    """
    Analiza una lista de números y devuelve (mínimo, máximo, suma).
    Maneja listas vacías o no numéricas con try-except.
    """
    try:
        # Verificar que la lista no esté vacía
        if not lista_numeros:
            return (0, 0, 0)
            
        # Intentar calcular los valores (sum, min y max fallarían si hay no-numéricos)
        suma_total = sum(lista_numeros)
        min_valor = min(lista_numeros)
        max_valor = max(lista_numeros)
        
        return (min_valor, max_valor, suma_total)
        
    except (TypeError, ValueError):
        # Captura errores si hay tipos de datos incompatibles (ej. int + str)
        return (0, 0, 0)

# ----------------------------------------------------------------------
# PUNTO 4: Búsqueda de Coincidencias (Diccionario, Listas)
# ----------------------------------------------------------------------

def obtener_faltantes(inventario: dict[str, tuple[str, int]], umbral: int) -> list[str]:
    """
    Recibe un inventario y un umbral, devuelve una lista de códigos 
    de producto con stock <= umbral.
    """
    codigos_faltantes = []
    
    # Iterar sobre claves (código) y valores (tupla) del diccionario
    # Desempaquetamos la tupla en (nombre, stock)
    for codigo, (nombre, stock) in inventario.items():
        if stock <= umbral:
            codigos_faltantes.append(codigo)
            
    return codigos_faltantes

# ----------------------------------------------------------------------
# PUNTO 5: Validación de Password (String, Control de Flujo)
# ----------------------------------------------------------------------

def validar_password(password: str) -> bool:
    """
    Valida la contraseña según 3 criterios: longitud >= 10, al menos 1 mayúscula y al menos 1 dígito.
    Ignora espacios al inicio/fin.
    """
    # 1. Limpiar espacios al inicio/fin
    password_limpia = password.strip()
    
    # Criterio 1: Longitud mínima
    if len(password_limpia) < 10:
        return False
        
    # Inicializar banderas de validación
    tiene_mayuscula = False
    tiene_digito = False
    
    # Criterios 2 y 3: Búsqueda de mayúscula y dígito
    for char in password_limpia:
        if char.isupper():
            tiene_mayuscula = True
        if char.isdigit():
            tiene_digito = True
            
        # Optimización: Si ya encontramos ambos, salimos del bucle
        if tiene_mayuscula and tiene_digito:
            break
            
    # La contraseña es válida si ambos criterios se cumplen
    return tiene_mayuscula and tiene_digito

# ----------------------------------------------------------------------
# PRUEBAS DE EJECUCIÓN DEL MODELO 4
# ----------------------------------------------------------------------

if __name__ == "__main__":
    print("\n--- PRUEBAS DE FUNCIONALIDAD DEL MODELO 4 ---")

    # PUNTO 1: Gestión de Personal
    prog1 = Programador("Ana Lopez", "P001", ["Python", "Java"])
    prog2 = Programador("Beto Ruiz", "P002", ["java", "C++", "SQL"])
    prog3 = Programador("Carlos Sanz", "P003", ["JavaScript", "Python"])
    lista_pers = [prog1, prog2, prog3]
    filtrados_python = filtrar_por_lenguaje(lista_pers, "PYTHON")
    print("\n[Punto 1] Programadores que manejan 'Python':")
    print(f"Resultado: {[p.nombre for p in filtrados_python]}") # Esperado: ['Ana Lopez', 'Carlos Sanz']
    
    # PUNTO 2: Conteo de Caracteres Únicos
    cadena_test_1 = "Hola Mundo 123"
    conteo_1 = contar_unicos(cadena_test_1)
    conteo_2 = contar_unicos("")
    print(f"\n[Punto 2] Caracteres únicos en '{cadena_test_1}' (sin espacios/mayús):")
    print(f"Resultado (parcial - claves): {list(conteo_1.keys())}") 
    print(f"[Punto 2] Cadena vacía: {conteo_2}") # Esperado: {}
    
    # PUNTO 3: Análisis de Secuencias Numéricas
    secuencia_1 = [10, 5, 20, 2]
    secuencia_2 = [10, 'a', 20] # Caso de error (elemento no numérico)
    analisis_1 = analizar_numeros(secuencia_1)
    analisis_2 = analizar_numeros(secuencia_2)
    analisis_3 = analizar_numeros([])
    print(f"\n[Punto 3] Análisis de {secuencia_1}: {analisis_1}") # Esperado: (2, 20, 37)
    print(f"[Punto 3] Caso con error ('a'): {analisis_2}") # Esperado: (0, 0, 0)
    print(f"[Punto 3] Caso vacío: {analisis_3}") # Esperado: (0, 0, 0)
    
    # PUNTO 4: Búsqueda de Coincidencias
    inventario_test = {
        "A101": ("Tornillo M4", 150),
        "B205": ("Arandela 10mm", 45),
        "C300": ("Tuerca M8", 10),
        "D404": ("Clavo 2cm", 250)
    }
    faltantes = obtener_faltantes(inventario_test, 50)
    print(f"\n[Punto 4] Códigos faltantes (umbral 50): {faltantes}") # Esperado: ['B205', 'C300']
    
    # PUNTO 5: Validación de Password
    valida_ok = validar_password("   MiClave100   ") # Válido: Limpieza + Longitud + Mayús + Dígito
    valida_fail_len = validar_password("Corta1") # Inválido: Longitud < 10
    valida_fail_mayus = validar_password("miclave100") # Inválido: No Mayúscula
    valida_fail_digit = validar_password("MiClaveSegura") # Inválido: No Dígito
    print(f"\n[Punto 5] '   MiClave100   ' (OK): {valida_ok}") # Esperado: True
    print(f"[Punto 5] 'Corta1' (FAIL - Len): {valida_fail_len}") # Esperado: False
    print(f"[Punto 5] 'miclave100' (FAIL - Mayús): {valida_fail_mayus}") # Esperado: False
    print(f"[Punto 5] 'MiClaveSegura' (FAIL - Dígito): {valida_fail_digit}") # Esperado: False
    print("\n----------------------------------------------------")