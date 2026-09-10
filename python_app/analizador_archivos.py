import os

# =========================================================================
# ACTIVIDAD PRÁCTICA: ANALIZADOR DE ARCHIVOS 
# =========================================================================
# RUBRICA: "Modificar el ejercicio asignado en la actividad Protocolo Individual 
# Unidad 1 y aplicar los conceptos de Objetos, Struct y Récord como elementos 
# guardados en los arreglos o matrices."
# 
# EXPLICACION: Para no alterar la naturaleza original del Ejercicio 6 (analizar numeros), 
# y mantener el codigo TOTALMENTE SEPARADO de los estudiantes, hemos creado un  
# Objeto llamado 'RegistroNumerico'. Así aplicamos la POO exactamente como dice 
# el profesor sin arruinar la logica de los numeros.

# -------------------------------------------------------------------------
# 1. APLICANDO CONCEPTOS DE OBJETOS: Creación de la clase para el arreglo
# -------------------------------------------------------------------------
class RegistroNumerico:
    def __init__(self, valor):
        self.valor = valor

def ejecutar_analizador():
    print("\n=======================================================")
    print(" EJECUTANDO ACTIVIDAD PRÁCTICA: Analizador de Archivos (PYTHON)")
    print("=======================================================")
    print("\n>>> Actividad: Modificar el Ejercicio 6 leyendo Objetos en un Arreglo...")

    # -------------------------------------------------------------------------
    # SOLICITAR Y VALIDAR el archivo de entrada ingresado por el usuario
    # -------------------------------------------------------------------------
    archivo_entrada = input("\nIngrese el nombre (o ruta) del archivo de entrada: ").strip()
    archivo_salida = "resultados_python.txt"

    if not archivo_entrada:
        print("ERROR: No ingresó ningún nombre de archivo. Operación cancelada.")
        return

    if not os.path.exists(archivo_entrada):
        print(f"ERROR: El archivo '{archivo_entrada}' no existe o la ruta es incorrecta.")
        print("Verifique el nombre del archivo e intente de nuevo.")
        return

    print(f"Archivo encontrado. Leyendo: {archivo_entrada}")
    
    # =========================================================================
    # 2. MODIFICACION DEL EJERCICIO ORIGINAL: LEER Y GUARDAR COMO OBJETOS
    # =========================================================================
    # El codigo original de Java leia ints/float primitivos. 
    # Aquí instanciamos un Objeto por cada numero leido y lo guardamos 
    # en un arreglo de Objetos, cumpliendo la exigencia principal.
    arreglo_objetos = []
    
    with open(archivo_entrada, "r") as f:
        lineas = f.readlines()
        for linea in lineas:
            numero = float(linea.strip())
            arreglo_objetos.append(RegistroNumerico(numero))
            
    # =========================================================================
    # 3. CALCULAR ESTADISTICAS (Iterando sobre el arreglo de Objetos)
    # =========================================================================
    suma = 0
    maximo = arreglo_objetos[0].valor
    minimo = arreglo_objetos[0].valor
    
    for obj in arreglo_objetos:
        val = obj.valor
        suma += val
        if val > maximo:
            maximo = val
        if val < minimo:
            minimo = val
            
    promedio = suma / len(arreglo_objetos)
    
    # =========================================================================
    # 4. ORDENAR ARREGLO DE OBJETOS Y GUARDAR RESULTADOS
    # =========================================================================
    arreglo_objetos.sort(key=lambda x: x.valor)
    
    with open(archivo_salida, "w") as f:
        f.write("=== REPORTE ESTADISTICO ===\n")
        f.write(f"Archivo origen: {archivo_entrada}\n")
        f.write(f"Cantidad de datos: {len(arreglo_objetos)}\n\n")
        f.write(f"Minimo: {minimo}\n")
        f.write(f"Maximo: {maximo}\n")
        f.write(f"Promedio: {promedio:.2f}\n\n")
        
        f.write("=== DATOS ORDENADOS ===\n")
        for obj in arreglo_objetos:
            f.write(f"{obj.valor}\n")
            
    print(f"-> Analisis exitoso. Reporte guardado en '{archivo_salida}'.\n")

if __name__ == "__main__":
    ejecutar_analizador()
