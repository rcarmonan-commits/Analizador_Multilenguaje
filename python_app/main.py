import sys
import registros_structs
import objetos_clases
import analizador_archivos

def main():
    # Esta es la puerta de entrada a todo el proyecto. Decidí crear un menú interactivo usando 
    # un ciclo "while True" para que el profesor pueda saltar de un ejercicio a otro sin 
    # tener que salir a la consola y volver a ejecutar todo a mano.
    while True:
        print("\n---------------------------------------------------------")
        print(" Sistema de Análisis Multilenguaje - Desarrollado en Python ")
        print(" Estudiante: Rosary Carmona | Ingeniería de Software      ")
        print("---------------------------------------------------------")
        print("1. Demostrar el uso de Records y Structs (Punto 3)")
        print("2. Demostrar el uso de Clases y Objetos (Punto 4)")
        print("3. Ejecutar la Actividad Práctica Final (Analizador)")
        print("4. Cerrar el programa")
        print("---------------------------------------------------------")
        
        opcion = input("Por favor, ingrese el número de la opción que desea ejecutar: ")
        print("\n")
        
        # En Python, en versiones anteriores a la 3.10 no existe la estructura "switch-case" de Java o C#.
        # Por lo tanto, utilicé la clásica validación con if-elif para capturar lo que digita el usuario
        # y mandar a llamar al módulo correcto importado desde los otros archivos que programé.
        if opcion == "1":
            registros_structs.ejecutar_registros()
        elif opcion == "2":
            objetos_clases.ejecutar_clases()
        elif opcion == "3":
            analizador_archivos.ejecutar_analizador()
        elif opcion == "4":
            # Cuando eligen el 4, uso sys.exit() para apagar el programa de forma limpia y cerrar los procesos.
            print("El programa se ha cerrado correctamente. ¡Hasta luego!")
            sys.exit(0)
        else:
            # Esta validación evita que el programa falle si el profesor ingresa una letra o un número inválido.
            print("Opción inválida. Asegúrese de ingresar un número entre 1 y 4.")

if __name__ == "__main__":
    # Esta línea asegura que el código principal solo se corra si este archivo se ejecuta directamente,
    # y no si simplemente lo importamos desde otro script.
    main()
