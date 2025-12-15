## SOLUCIÓN MODELO DE EXAMEN 7: GESTIÓN DE AGENDA AVANZADA

# ========================================================
# CLASE BASE AJUSTADA
# ========================================================

class Persona:
    def __init__(self, nombre, direccion, telefono, provincia, email=""):
        self.nombre = nombre
        self.direccion = direccion
        
        # Validación estricta del teléfono
        if len(telefono) == 9 and telefono.isdigit():
            self.telefono = telefono
        else:
            raise ValueError("ERROR: El teléfono debe ser un string de 9 dígitos.")
            
        self.provincia = provincia
        self.email = email # Nuevo atributo para el Punto 2

    def toString(self):
        # Corregido: usa return para que pueda ser llamado externamente
        return (f"Nombre: {self.nombre} | Dirección: {self.direccion} | Teléfono: {self.telefono} | Provincia: {self.provincia} | Email: {self.email}")

    # PUNTO 1: Propiedad de Nombre Corto
    def getNombreCorto(self):
        """Devuelve el primer nombre (la primera palabra) en mayúsculas."""
        if self.nombre:
            return self.nombre.split()[0].upper()
        return "N/A"

# ========================================================
# DICCIONARIO GLOBAL (para simulación)
# ========================================================

contactos = {}
contactos["FRANCISCO"] = Persona("FRANCISCO JAVIER", "oefjw32 32 r2oij", "632341223", "Jaén", "fran@email.com")
contactos["AITOR"] = Persona("AITOR", "jaen linaejioej 3rr", "236225454", "Jaén", "aitor@email.com")
contactos["MARIO"] = Persona("MARIO", "santani3or20r dwefw", "523453423", "Málaga", "mario@email.com")
contactos["LAURA"] = Persona("LAURA", "calle falsa 123", "600123456", "Sevilla", "laura@email.com")

# ========================================================
# FUNCIONES DE EXAMEN (PUNTOS 2, 3, 5)
# ========================================================

# PUNTO 2: Búsqueda y Validación de Email
def es_email_valido(email: str) -> bool:
    """Verifica sintaxis básica y unicidad en los contactos."""
    # 1. Validación de sintaxis básica
    if email.count('@') != 1 or email.count('.') == 0:
        return False
        
    # 2. Validación de unicidad
    for persona in contactos.values():
        if persona.email.lower() == email.lower():
            print(f"ERROR: El email '{email}' ya está registrado.")
            return False
            
    return True

# PUNTO 3: Conteo por Categoría
def contar_contactos_por_provincia() -> dict[str, int]:
    """Cuenta el número de contactos por provincia."""
    conteo_provincias = {}
    for persona in contactos.values():
        provincia = persona.provincia.strip().capitalize() # Limpieza de datos
        
        if provincia in conteo_provincias:
            conteo_provincias[provincia] += 1
        else:
            conteo_provincias[provincia] = 1
            
    return conteo_provincias

# PUNTO 4: Modificación Robusta con Validaciones (Refactorización de modContacto)
def validar_nuevo_telefono(telefono_str: str) -> bool:
    """Función auxiliar que comprueba que el teléfono es de 9 dígitos."""
    return len(telefono_str) == 9 and telefono_str.isdigit()

def modContacto(contactos_dict: dict):
    """Permite modificar contacto validando el nuevo teléfono."""
    print("\n=== Modificar un contacto (Punto 4 Refactorizado) ===")
    try:
        contacto = input("¿Qué contacto quieres modificar? ").strip().upper()
        if not contacto in contactos_dict:
            print("ERROR: No existe ningún contacto.")
            return False
        
        print(f"Modificando contacto: {contactos_dict[contacto].nombre}")
        
        opcionMod = input("¿Qué quieres modificar? (1: Dirección, 2: Teléfono) ").strip()

        if opcionMod == '1':
            direccion = input("Introduce la nueva dirección: ").strip()
            contactos_dict[contacto].direccion = direccion
            print("Dirección modificada correctamente.")
        elif opcionMod == '2':
            telefono = input("Introduce el nuevo teléfono: ").strip()
            if validar_nuevo_telefono(telefono): # Uso de la función de validación
                contactos_dict[contacto].telefono = telefono
                print("Teléfono modificado correctamente.")
            else:
                print("WARNING: Teléfono no válido (debe ser 9 dígitos). No se realizaron cambios.")
        else:
            print("WARNING: Opción no válida.")

    except Exception as e:
        print(f"ERROR: Ha ocurrido un error inesperado: {e}")
    finally:
        print("")
        input("Pulsa [ENTER] para continuar...")
        return False

# PUNTO 5: Eliminar Múltiples Contactos
def eliminar_multiples(nombres_a_eliminar: list[str]) -> str:
    """Elimina múltiples contactos del diccionario, gestionando errores con try-except."""
    eliminados = []
    no_encontrados = []
    
    for nombre in nombres_a_eliminar:
        nombre_upper = nombre.strip().upper()
        try:
            # Intentar eliminar la clave del diccionario
            del contactos[nombre_upper]
            eliminados.append(nombre_upper)
        except KeyError:
            # Capturar si la clave (nombre) no existe
            no_encontrados.append(nombre_upper)
        
    res_str = f"Eliminados OK: {', '.join(eliminados) if eliminados else 'Ninguno'}."
    if no_encontrados:
        res_str += f" No encontrados: {', '.join(no_encontrados)}."
        
    return res_str

# ========================================================
# PRUEBAS DE EJECUCIÓN DEL MODELO 7
# ========================================================

if __name__ == "__main__":
    print("\n--- PRUEBAS DE FUNCIONALIDAD DEL MODELO 7 ---")
    
    # PUNTO 1: Propiedad de Nombre Corto
    print(f"\n[Punto 1] Nombre Completo de Francisco: {contactos['FRANCISCO'].nombre}")
    print(f"[Punto 1] Nombre Corto (Expected: FRANCISCO): {contactos['FRANCISCO'].getNombreCorto()}")
    
    # PUNTO 2: Búsqueda y Validación de Email
    print(f"\n[Punto 2] Validación de Email:")
    print(f"Email 'test@valido.com' (OK): {es_email_valido('test@valido.com')}") # Esperado: True
    print(f"Email 'aitor@email.com' (Duplicado): {es_email_valido('aitor@email.com')}") # Esperado: False
    print(f"Email 'mal_formato.com' (FAIL): {es_email_valido('mal_formato.com')}") # Esperado: False

    # PUNTO 3: Conteo por Categoría
    conteo_provincias = contar_contactos_por_provincia()
    print(f"\n[Punto 3] Conteo por Provincia:")
    print(f"Resultado: {conteo_provincias}") # Esperado: {'Jaén': 2, 'Málaga': 1, 'Sevilla': 1}

    # PUNTO 4: Modificación Robusta (Simulación de Modificar Teléfono)
    print("\n[Punto 4] Simulación de Modificar Contacto (Teléfono):")
    nombre_mod = "MARIO"
    telefono_original = contactos[nombre_mod].telefono
    
    # Simulación de entrada: Opción 2 y Teléfono válido
    print("--- Prueba 1: Teléfono válido (999888777) ---")
    nuevo_telf_ok = "999888777"
    if validar_nuevo_telefono(nuevo_telf_ok):
        contactos[nombre_mod].telefono = nuevo_telf_ok
    print(f"Teléfono de Mario: {contactos[nombre_mod].telefono}") # Esperado: 999888777
    
    # Simulación de entrada: Opción 2 y Teléfono NO válido
    print("--- Prueba 2: Teléfono NO válido (123) ---")
    nuevo_telf_fail = "123"
    if not validar_nuevo_telefono(nuevo_telf_fail):
        print(f"WARNING: Teléfono no válido. El teléfono de Mario sigue siendo: {contactos[nombre_mod].telefono}") # Esperado: 999888777

    # PUNTO 5: Eliminar Múltiples Contactos
    nombres_a_borrar = ["AITOR", "MARIA", "LAURA"] # AITOR y LAURA existen, MARIA no
    print(f"\n[Punto 5] Eliminación Múltiple ({nombres_a_borrar}):")
    resultado_del = eliminar_multiples(nombres_a_borrar)
    print(resultado_del) # Esperado: Eliminados OK: AITOR, LAURA. No encontrados: MARIA.
    print(f"Contactos restantes (claves): {list(contactos.keys())}") # Esperado: ['FRANCISCO', 'MARIO']