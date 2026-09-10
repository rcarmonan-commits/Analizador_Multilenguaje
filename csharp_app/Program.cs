using System;

namespace CSharpApp
{
    class Program
    {
        // =========================================================================
        // FUNCIÓN AUXILIAR: Pregunta si el usuario desea regresar al menú o salir
        // =========================================================================
        /// <summary>
        /// Después de ejecutar un módulo, pregunta al usuario si desea regresar
        /// al menú principal o salir. Valida la respuesta en bucle.
        /// Retorna true si desea regresar al menú, false si desea salir.
        /// </summary>
        static bool PreguntarContinuar()
        {
            while (true)
            {
                Console.WriteLine("\n---------------------------------------------------------");
                Console.Write(" ¿Desea regresar al menú principal o salir? (M = Menú / S = Salir): ");
                string respuesta = (Console.ReadLine() ?? "").Trim().ToUpper();

                if (respuesta == "M") return true;
                if (respuesta == "S") return false;

                Console.WriteLine(" Opción inválida. Ingrese M para volver al menú o S para salir.");
            }
        }

        static void Main(string[] args)
        {
            bool continuar = true;

            while (continuar)
            {
                // -------------------------------------------------------------------------
                // MENÚ PRINCIPAL
                // -------------------------------------------------------------------------
                Console.WriteLine("\n=========================================================");
                Console.WriteLine("  Sistema de Análisis Multilenguaje - Desarrollado en C#");
                Console.WriteLine("  Estudiante: Rosary Carmona | Protocolo Individual");
                Console.WriteLine("=========================================================");
                Console.WriteLine("  1. Demostrar el uso de Records y Structs (Punto 3)");
                Console.WriteLine("  2. Demostrar el uso de Clases y Objetos (Punto 4)");
                Console.WriteLine("  3. Ejecutar la Actividad Práctica Final (Analizador)");
                Console.WriteLine("  4. Salir del programa");
                Console.WriteLine("=========================================================");
                Console.Write("  Ingrese el número de la opción que desea ejecutar: ");

                string opcion = (Console.ReadLine() ?? "").Trim();
                Console.WriteLine();

                // En C# usamos if-else en lugar de switch para mayor claridad y compatibilidad
                // con el estilo del proyecto. Cada opción llama al módulo correspondiente
                // y luego pregunta si desea regresar al menú o salir.
                if (opcion == "1")
                {
                    RegistrosStructs.ProbarStructs();
                    continuar = PreguntarContinuar();
                }
                else if (opcion == "2")
                {
                    ObjetosClases.ProbarObjetos();
                    continuar = PreguntarContinuar();
                }
                else if (opcion == "3")
                {
                    AnalizadorArchivos.EjecutarAnalizador();
                    continuar = PreguntarContinuar();
                }
                else if (opcion == "4")
                {
                    // Salida directa desde el menú sin preguntar
                    continuar = false;
                }
                else
                {
                    // Esta validación evita que el programa falle si se ingresa un valor inválido.
                    Console.WriteLine("  ⚠ Opción inválida. Asegúrese de ingresar un número entre 1 y 4.");
                }
            }

            // Cuando eligen salir (opción 4 o S), cerramos el programa de forma limpia.
            Console.WriteLine("\n  El programa se ha cerrado correctamente. ¡Hasta luego!\n");
        }
    }
}
