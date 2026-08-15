# =========================================================================
# PUNTO 4 DE LA RUBRICA: Objetos (Clases e instancias)
# =========================================================================

# -------------------------------------------------------------------------
# ACTIVIDAD: Declaración
# -------------------------------------------------------------------------
# Definir una clase Estudiante con: nombre, edad, promedio y un método mostrarInfo.
class Estudiante:
    def __init__(self, nombre, edad, promedio):
        # En una Clase aplicamos ENCAPSULAMIENTO usando doble guion bajo (atributos privados)
        self.__nombre = nombre
        self.__edad = edad
        self.__promedio = promedio
        
        # 💡 TIP EVALUACION FINAL: 
        # Usar un arreglo de objetos que contenga un campo que sea a su vez una matriz.
        self.__calificaciones_matriz = [
            [self.__promedio, round(self.__promedio - 0.2, 2), round(self.__promedio + 0.1, 2)],
            [round(self.__promedio + 0.1, 2), self.__promedio, round(self.__promedio - 0.1, 2)]
        ]

    # Setter encapsulado para modificar el promedio de forma segura
    def set_promedio(self, nuevo_promedio):
        self.__promedio = nuevo_promedio

    def get_promedio(self):
        return self.__promedio

    # -------------------------------------------------------------------------
    # ACTIVIDAD: Recorrido (Método propio)
    # -------------------------------------------------------------------------
    # Método MostrarInfo exigido por la rubrica
    def mostrar_info(self):
        print(f"Objeto Clase -> Nombre: {self.__nombre}, Edad: {self.__edad}, Promedio: {self.__promedio}")
        print(f"  Matriz Encapsulada: {self.__calificaciones_matriz}")

def probar_objetos():
    print("\n=======================================================")
    print(" EJECUTANDO PUNTO 4 DE LA RUBRICA: Objetos (Clases)")
    print("=======================================================")

    # -------------------------------------------------------------------------
    # ACTIVIDAD: Inicialización y Recorrido
    # -------------------------------------------------------------------------
    print("\n>>> Actividad: Inicialización y Recorrido usando mostrarInfo()...")
    # Crear 3 instancias y almacenarlas en un arreglo/lista.
    arreglo_estudiantes = []
    arreglo_estudiantes.append(Estudiante("Luis", 21, 3.8))
    arreglo_estudiantes.append(Estudiante("Ana", 23, 4.5))
    arreglo_estudiantes.append(Estudiante("Pedro", 18, 2.9))

    # Llamar al metodo mostrarInfo para cada objeto.
    for est in arreglo_estudiantes:
        est.mostrar_info()

    # -------------------------------------------------------------------------
    # ACTIVIDAD: Modificación
    # -------------------------------------------------------------------------
    # Cambiar el promedio de un estudiante usando métodos Setters.
    print("\n>>> Actividad: Modificación del promedio de Luis usando Setter Encapsulado...")
    arreglo_estudiantes[0].set_promedio(4.5)
    print(f"Nuevo promedio de Luis (Leido por Getter): {arreglo_estudiantes[0].get_promedio()}\n")

    # -------------------------------------------------------------------------
    # ACTIVIDAD: Comparativa
    # -------------------------------------------------------------------------
    print("\n>>> Actividad: Comparativa")
    print("    -> (Las Clases definen estado y comportamiento, operan por")
    print("        referencia en el Heap, a diferencia del Struct que es")
    print("        un tipo por valor en el Stack).\n")
