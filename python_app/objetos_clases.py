# Para este cuarto punto, el objetivo era implementar el concepto de Clases y Objetos.
# A diferencia del archivo anterior donde solo usábamos la estructura para guardar datos estáticos,
# una Clase me permite tener tanto las variables (el estado) como las funciones (el comportamiento) 
# unidos en un solo bloque lógico.
class Estudiante:
    # Este es el constructor de la clase. Cada vez que quiero crear un nuevo estudiante en la memoria (Heap),
    # Python ejecuta esta función para darle los valores iniciales.
    def __init__(self, nombre: str, edad: int, promedio: float):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    # En lugar de imprimir los datos sueltos desde fuera, creé este método dentro de la clase.
    # Así, es el propio estudiante el que tiene la capacidad de mostrar su propia información.
    def mostrar_info(self):
        print(f"[{self.nombre}] - Edad: {self.edad} años, Calificación: {self.promedio}")

    # Este es un método modificador (conocido en la teoría como "setter").
    # La mejor práctica en programación orientada a objetos es no cambiar las variables directamente desde afuera,
    # sino pedirle a la clase que lo haga a través de un método. Esto asegura el encapsulamiento de la información.
    def set_promedio(self, nuevo_promedio: float):
        self.promedio = nuevo_promedio
        print(f"Notificación: El registro académico de {self.nombre} fue actualizado a {self.promedio}")

def solicitar_datos_estudiante():
    # Creamos esta función extra para que la revisión de la tarea sea más interactiva y el profesor pueda
    # escribir los datos a través de la terminal, en vez de ver solo información fija.
    nombre = input("Ingrese el nombre del estudiante: ")
    try:
        edad = int(input(f"Ingrese la edad de {nombre}: "))
        promedio = float(input(f"Ingrese el promedio de {nombre} (ej: 4.5): "))
        
        # Una vez capturados todos los campos, usamos la clase Estudiante para generar un nuevo objeto 
        # y lo devolvemos para guardarlo.
        return Estudiante(nombre, edad, promedio)
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para edad y promedio.")
        return None

def ejecutar_clases():
    print("\n--- Demostración del Punto 4: Objetos y Clases en Python ---")
    
    # Para cumplir con la rúbrica, instanciamos tres objetos base con datos de prueba.
    # Es importante notar que usamos la palabra "Estudiante" llamando a la clase, lo cual aloja esto en memoria dinámica.
    est1 = Estudiante("Carlos Ruiz", 21, 3.8)
    est2 = Estudiante("Diana Vargas", 23, 4.5)
    est3 = Estudiante("Roberto Carlos", 20, 3.2)

    # Todos esos objetos individuales los metemos dentro de una lista para poder procesarlos en conjunto.
    arreglo_objetos = [est1, est2, est3]
    
    # Le damos la opción al usuario de agregar sus propios objetos de forma interactiva usando un ciclo while.
    print("Se han instanciado 3 objetos Estudiante por defecto.")
    while True:
        respuesta = input("¿Desea instanciar un nuevo estudiante? (s/n): ").strip().lower()
        if respuesta == 's':
            nuevo_obj = solicitar_datos_estudiante()
            if nuevo_obj:
                # El nuevo objeto ingresado por teclado se añade al final de nuestra lista.
                arreglo_objetos.append(nuevo_obj)
                print(f"Objeto de '{nuevo_obj.nombre}' instanciado y agregado con éxito.")
        elif respuesta == 'n':
            # Cuando el usuario termina de ingresar datos, salimos del ciclo para continuar la demostración.
            break
        else:
            print("Opción no válida. Ingrese 's' para sí, o 'n' para no.")

    # A continuación recorro toda la lista, pero fíjense que ya no hago un "print" manual.
    # Le estoy diciendo a cada estudiante que se encargue él mismo de imprimir sus datos usando su propio método.
    print("\nDesplegando la información de cada objeto desde su propio método:")
    for estudiante in arreglo_objetos:
        estudiante.mostrar_info()

    # Ahora comprobamos que el método "setter" funciona. Modifico el promedio del tercer estudiante base,
    # y en vez de usar un igual (=), llamo a la función que programé arriba.
    print("\nAplicando actualización de calificaciones mediante el método de la clase...")
    
    # Valido que el tercer elemento de la lista efectivamente sea Roberto para evitar errores si el usuario ingresó más datos
    if len(arreglo_objetos) > 2 and arreglo_objetos[2].nombre == "Roberto Carlos":
        arreglo_objetos[2].set_promedio(4.0)

    # Por último, pido al objeto que vuelva a mostrar sus datos para certificar que el promedio efectivamente cambió en memoria.
    print("\nValidando el cambio en el estudiante modificado:")
    if len(arreglo_objetos) > 2 and arreglo_objetos[2].nombre == "Roberto Carlos":
        arreglo_objetos[2].mostrar_info()
        
    print("----------------------------------------------------------\n")

if __name__ == "__main__":
    ejecutar_clases()
