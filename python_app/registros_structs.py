from dataclasses import dataclass

# Para resolver el punto de los Structs (o Records) en Python, descubrí que la mejor 
# manera de hacerlo es usando una herramienta del lenguaje llamada "dataclass". 
# Lo que hace esto es crear una estructura muy sencilla que solamente sirve para guardar 
# datos, sin tener funciones complejas por dentro. Es exactamente el concepto de "Struct" 
# que vimos en la teoría.
@dataclass
class EstudianteRecord:
    nombre: str
    edad: int
    promedio: float

def solicitar_datos_estudiante():
    # Esta función la agregué para que el programa no sea estático. 
    # Aquí le pedimos al usuario por consola que ingrese los datos de un estudiante nuevo.
    nombre = input("Ingrese el nombre del estudiante: ")
    try:
        # Es importante convertir el texto que ingresa el usuario a números (int para la edad y float para el promedio)
        edad = int(input(f"Ingrese la edad de {nombre}: "))
        promedio = float(input(f"Ingrese el promedio de {nombre} (ej: 4.5): "))
        
        # Una vez tenemos los datos limpios, creamos el "Record" y lo devolvemos
        return EstudianteRecord(nombre, edad, promedio)
    except ValueError:
        # Si el usuario escribe una letra en lugar de un número, capturamos el error para que el programa no se caiga
        print("Error: Los datos numéricos ingresados no son válidos. Intente nuevamente.")
        return None

def ejecutar_registros():
    print("\n--- Demostración del Punto 3: Records (Structs) en Python ---")
    
    # Siguiendo las instrucciones de la actividad, primero creo 3 estudiantes con datos ficticios.
    # Como usamos un Record, estos datos se guardan directamente.
    estudiante1 = EstudianteRecord(nombre="Ana Perez", edad=20, promedio=4.2)
    estudiante2 = EstudianteRecord(nombre="Luis Gomez", edad=22, promedio=3.5)
    estudiante3 = EstudianteRecord(nombre="Maria Lopez", edad=19, promedio=4.8)

    # Luego, agrupo a estos estudiantes en una lista (que en Python funciona como un arreglo).
    arreglo_estudiantes = [estudiante1, estudiante2, estudiante3]
    
    # Aquí incorporo la lógica interactiva. Le pregunto al usuario si desea agregar más personas
    # al arreglo que acabamos de crear.
    print("El sistema ha cargado 3 estudiantes por defecto.")
    while True:
        respuesta = input("¿Desea agregar un nuevo estudiante? (s/n): ").strip().lower()
        if respuesta == 's':
            # Llamamos a la función que pide los datos y si todo sale bien, lo agregamos a la lista
            nuevo_estudiante = solicitar_datos_estudiante()
            if nuevo_estudiante:
                arreglo_estudiantes.append(nuevo_estudiante)
                print(f"Estudiante '{nuevo_estudiante.nombre}' agregado con éxito.")
        elif respuesta == 'n':
            # Si el usuario dice que no, rompemos el ciclo para continuar con el programa
            break
        else:
            print("Opción no válida. Ingrese 's' para sí, o 'n' para no.")

    # Para comprobar que los datos están guardados, recorro toda la lista usando un ciclo for
    # y muestro la información en la pantalla.
    print("\nEstado inicial de los registros en el sistema:")
    for est in arreglo_estudiantes:
        print(f"Estudiante: {est.nombre}, Edad: {est.edad}, Promedio Actual: {est.promedio}")

    # Ahora demuestro cómo se modifica un dato dentro de un Record.
    # En este caso, accedo directamente a la variable "promedio" y le cambio el valor.
    print("\nActualizando la calificación del estudiante por defecto 'Luis Gomez' a 4.0...")
    
    # Para evitar errores, primero verifico que la lista tenga suficientes elementos y que sea el estudiante correcto
    if len(arreglo_estudiantes) > 1 and arreglo_estudiantes[1].nombre == "Luis Gomez":
        arreglo_estudiantes[1].promedio = 4.0

    # Finalmente, vuelvo a imprimir la lista completa para evidenciar que el cambio de promedio se aplicó correctamente.
    print("\nEstado actualizado tras la modificación:")
    for est in arreglo_estudiantes:
        print(f"Estudiante: {est.nombre}, Edad: {est.edad}, Promedio Actual: {est.promedio}")
    print("--------------------------------------------------------------\n")

if __name__ == "__main__":
    ejecutar_registros()
