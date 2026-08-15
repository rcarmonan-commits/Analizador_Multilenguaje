from dataclasses import dataclass, field

# =========================================================================
# PUNTO 3 DE LA RUBRICA: Record o Struct
# =========================================================================
# FUNDAMENTOS TEORICOS:
# - Concepto y utilidad: Un Record/Struct agrupa datos relacionados.
# - Diferencias con objeto: En Python no existen Structs puros como en C#,
#   pero emulamos su comportamiento con @dataclass o NamedTuples, creando 
#   objetos ligeros que no tienen comportamiento (métodos), solo datos pasivos.
# - Tipado y acceso a campos: Aunque Python es de tipado dinamico, usamos Type 
#   Hints (str, int, float) para emular la rigidez de un struct de C#.

# -------------------------------------------------------------------------
# ACTIVIDAD: Declaración
# -------------------------------------------------------------------------
# Definir un struct o record que contenga: nombre, edad, promedio.
@dataclass
class EstudianteStruct:
    nombre: str
    edad: int
    promedio: float
    
    # 💡 TIP EVALUACION FINAL: 
    # Usar un arreglo de objetos/structs que contenga un campo que sea a su vez una matriz.
    # En Python implementamos la matriz usando una lista de listas (arreglo 2D)
    calificaciones_matriz: list = field(init=False)

    def __post_init__(self):
        # Llenamos la matriz con datos de ejemplo usando el promedio
        self.calificaciones_matriz = [
            [self.promedio, round(self.promedio - 0.2, 2), round(self.promedio + 0.1, 2)],
            [round(self.promedio + 0.1, 2), self.promedio, round(self.promedio - 0.1, 2)]
        ]

def probar_structs():
    print("\n=======================================================")
    print(" EJECUTANDO PUNTO 3 DE LA RUBRICA: Record o Struct (PYTHON)")
    print("=======================================================")

    # -------------------------------------------------------------------------
    # ACTIVIDAD: Inicialización y Recorrido
    # -------------------------------------------------------------------------
    print("\n>>> Actividad: Inicialización y Recorrido de 3 instancias...")
    # Crear 3 instancias con datos ficticios y guardarlas en un arreglo.
    estudiantes = []
    estudiantes.append(EstudianteStruct("Carlos", 20, 3.5))
    estudiantes.append(EstudianteStruct("Maria", 22, 4.8))
    estudiantes.append(EstudianteStruct("Juan", 19, 2.1))

    # Recorrer el arreglo mostrando los datos (incluyendo la matriz del Tip)
    for est in estudiantes:
        print(f"Struct -> Nombre: {est.nombre}, Edad: {est.edad}, Promedio: {est.promedio}")
        print(f"  Matriz: {est.calificaciones_matriz}")

    # -------------------------------------------------------------------------
    # ACTIVIDAD: Modificación
    # -------------------------------------------------------------------------
    # Cambiar el promedio de un estudiante especifico (Carlos).
    print("\n>>> Actividad: Modificación del promedio de Carlos de forma directa...")
    estudiantes[0].promedio = 4.0
    print(f"Nuevo promedio de Carlos: {estudiantes[0].promedio}\n")
    
    # -------------------------------------------------------------------------
    # ACTIVIDAD: Comparativa
    # -------------------------------------------------------------------------
    print("\n>>> Actividad: Comparativa")
    print("    -> (En Python no existen Structs puros como en C#, por lo que")
    print("        emulamos el comportamiento con Dataclasses). Las diferencias")
    print("        completas se documentan en el README y el PDF.\n")
