import os
from dataclasses import dataclass

# 1. Concepto de Récord/Struct puro (Solo datos, sin métodos)
# Lo utilizo para agrupar las estadísticas calculadas.
@dataclass
class Estadisticas:
    minimo: int
    maximo: int
    promedio: float

# 2. Concepto de Clase y Objeto (Atributos + Métodos)
# Cumpliendo con el requerimiento de tener "un arreglo de objetos que contengan 
# un campo que sea a su vez una matriz".
class ArchivoAnalizado:
    def __init__(self, nombre_archivo: str, matriz_datos: list, estadisticas: Estadisticas):
        self.nombre_archivo = nombre_archivo
        
        # ¡Aquí está el campo exigido en la rúbrica que es a su vez una matriz!
        # Guardaremos los datos en formato de matriz Nx2: [[valor, es_par], [valor, es_par], ...]
        self.matriz_datos = matriz_datos 
        
        # Guardo el struct de estadísticas dentro del objeto
        self.estadisticas = estadisticas
        
    def mostrar_resumen(self):
        # Método de la clase para mostrar sus propios datos (Encapsulamiento)
        print(f"\n--- Resumen del Objeto: {self.nombre_archivo} ---")
        print(f"Estadísticas -> Mínimo: {self.estadisticas.minimo}, Máximo: {self.estadisticas.maximo}, Promedio: {self.estadisticas.promedio:.2f}")
        print("Muestra de la matriz interna de datos (Valor, Es_Par):")
        # Imprimo solo los primeros 5 elementos de la matriz para no saturar la pantalla
        for fila in self.matriz_datos[:5]:
            print(f"  {fila}")
        if len(self.matriz_datos) > 5:
            print("  ...")

class AnalizadorArchivos:
    def __init__(self):
        # Este es el arreglo de objetos principal que pide la rúbrica.
        # Aquí guardaré objetos de tipo "ArchivoAnalizado".
        self.arreglo_objetos = []

    def procesar(self, archivo_entrada: str):
        print(f"Analizando el archivo '{archivo_entrada}'...")
        
        if not os.path.exists(archivo_entrada):
            print(f"Error: No existe el archivo '{archivo_entrada}'.")
            return

        try:
            matriz_interna = []
            valores = []
            
            with open(archivo_entrada, 'r') as f:
                for linea in f:
                    linea = linea.strip()
                    if linea.isdigit() or (linea.startswith('-') and linea[1:].isdigit()):
                        numero = int(linea)
                        valores.append(numero)
                        
                        # Construyo una fila de la matriz: [numero, booleano]
                        fila = [numero, numero % 2 == 0]
                        matriz_interna.append(fila)
            
            if not valores:
                print("El archivo está vacío o sin números válidos.")
                return

            # Construyo el Struct de estadísticas
            stats = Estadisticas(
                minimo=min(valores),
                maximo=max(valores),
                promedio=sum(valores) / len(valores)
            )
            
            # Instancio el Objeto final (que contiene la matriz y el struct)
            objeto_archivo = ArchivoAnalizado(
                nombre_archivo=archivo_entrada,
                matriz_datos=matriz_interna,
                estadisticas=stats
            )
            
            # Guardo el objeto en mi arreglo general
            self.arreglo_objetos.append(objeto_archivo)
            
            # Muestro los datos usando el método del objeto
            objeto_archivo.mostrar_resumen()

        except Exception as e:
            print(f"Error procesando archivo: {e}")

def ejecutar_analizador():
    # Creo un archivo de prueba para sustentar el programa
    ruta_prueba = "numeros_matriz.txt"
    if not os.path.exists(ruta_prueba):
        with open(ruta_prueba, 'w') as f:
            f.write("45\n12\n-5\n89\n100\n73\n2\n24\n99\n1\n")
            
    analizador = AnalizadorArchivos()
    analizador.procesar(ruta_prueba)

if __name__ == "__main__":
    ejecutar_analizador()
