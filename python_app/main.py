import sys
import registros_structs
import objetos_clases
import analizador_archivos

# =========================================================================
# FUNCIÓN AUXILIAR: Pregunta si el usuario desea regresar al menú o salir
# =========================================================================
def preguntar_continuar():
    """
    Después de ejecutar un módulo, pregunta al usuario si desea regresar
    al menú principal o salir del programa. Valida la respuesta en bucle.
    Retorna True si desea regresar al menú, False si desea salir.
    """
    while True:
        print("\n---------------------------------------------------------")
        respuesta = input(" ¿Desea regresar al menú principal o salir? (M = Menú / S = Salir): ").strip().upper()
        if respuesta == "M":
            return True
        elif respuesta == "S":
            return False
        else:
            print(" Opción inválida. Ingrese M para volver al menú o S para salir.")


def main():
    # Esta es la puerta de entrada a todo el proyecto. Decidí crear un menú interactivo usando
    # un ciclo "while True" para que el profesor pueda saltar de un ejercicio a otro sin
    # tener que salir a la consola y volver a ejecutar todo a mano.
    while True:
        print("\n=========================================================")
        print("  Sistema de Análisis Multilenguaje - Desarrollado en Python")
        print("  Estudiante: Rosary Carmona | Protocolo Individual")
        print("=========================================================")
        print("  1. Demostrar el uso de Records y Structs (Punto 3)")
        print("  2. Demostrar el uso de Clases y Objetos (Punto 4)")
        print("  3. Ejecutar la Actividad Práctica Final (Analizador)")
        print("  4. Salir del programa")
        print("=========================================================")

        opcion = input("  Ingrese el número de la opción que desea ejecutar: ").strip()
        print()

        # En Python, en versiones anteriores a la 3.10 no existe la estructura "switch-case" de Java o C#.
        # Por lo tanto, utilicé la clásica validación con if-elif para capturar lo que digita el usuario
        # y mandar a llamar al módulo correcto importado desde los otros archivos que programé.
        if opcion == "1":
            registros_structs.probar_structs()
            if not preguntar_continuar():
                break

        elif opcion == "2":
            objetos_clases.probar_objetos()
            if not preguntar_continuar():
                break

        elif opcion == "3":
            analizador_archivos.ejecutar_analizador()
            if not preguntar_continuar():
                break

        elif opcion == "4":
            # Salida directa desde el menú sin preguntar
            break

        else:
            # Esta validación evita que el programa falle si el profesor ingresa una letra o un número inválido.
            print("  ⚠ Opción inválida. Asegúrese de ingresar un número entre 1 y 4.")

    # Cuando eligen salir (opción 4 o S), cerramos el programa de forma limpia.
    print("\n  El programa se ha cerrado correctamente. ¡Hasta luego!\n")
    sys.exit(0)


if __name__ == "__main__":
    # Esta línea asegura que el código principal solo se corra si este archivo se ejecuta directamente,
    # y no si simplemente lo importamos desde otro script.
    main()
