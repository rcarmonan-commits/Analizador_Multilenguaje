using System;

namespace CSharpApp
{
    // =========================================================================
    // PUNTO 3 DE LA RUBRICA: Record o Struct
    // =========================================================================
    // FUNDAMENTOS TEORICOS:
    // - Concepto y utilidad: Los Structs en C# (o Records en otros lenguajes) sirven 
    //   para almacenar datos relacionados como un solo bloque. Son estructuras ligeras.
    // - Diferencias con objeto: Un Struct es un "Tipo de Valor" que se aloja en el Stack. 
    //   Se pasa por copia y no tiene herencia, a diferencia de las clases (Objetos) que 
    //   son "Tipos de Referencia", se alojan en el Heap y pueden heredar.
    // - Tipado y acceso a campos: Típicamente los campos de un Struct son publicos para
    //   permitir el acceso rapido (sin getters/setters), demostrando tipado fuerte.

    // -------------------------------------------------------------------------
    // ACTIVIDAD: Declaración
    // -------------------------------------------------------------------------
    // Definir un struct o record que contenga: nombre, edad, promedio.
    public struct EstudianteStruct
    {
        public string Nombre;
        public int Edad;
        public double Promedio;
        
        // 💡 TIP EVALUACION FINAL: 
        // Usar un arreglo de objetos/structs que contenga un campo que sea a su vez una matriz.
        public double[,] CalificacionesMatriz;

        public EstudianteStruct(string nombre, int edad, double promedio)
        {
            Nombre = nombre;
            Edad = edad;
            Promedio = promedio;
            
            // Llenamos la matriz con datos de ejemplo usando el promedio
            CalificacionesMatriz = new double[2, 3] {
                { promedio, Math.Round(promedio - 0.2, 2), Math.Round(promedio + 0.1, 2) },
                { Math.Round(promedio + 0.1, 2), promedio, Math.Round(promedio - 0.1, 2) }
            };
        }
    }

    public class RegistrosStructs
    {
        public static void ProbarStructs()
        {
            Console.WriteLine("\n=======================================================");
            Console.WriteLine(" EJECUTANDO PUNTO 3 DE LA RUBRICA: Record o Struct (C#)");
            Console.WriteLine("=======================================================");

            // -------------------------------------------------------------------------
            // ACTIVIDAD: Inicialización y Recorrido
            // -------------------------------------------------------------------------
            Console.WriteLine("\n>>> Actividad: Inicialización y Recorrido de 3 instancias...");
            // Crear 3 instancias con datos ficticios y guardarlas en un arreglo.
            EstudianteStruct[] estudiantes = new EstudianteStruct[3];
            estudiantes[0] = new EstudianteStruct("Carlos", 20, 3.5);
            estudiantes[1] = new EstudianteStruct("Maria", 22, 4.8);
            estudiantes[2] = new EstudianteStruct("Juan", 19, 2.1);

            // Recorrer el arreglo mostrando los datos (incluyendo la matriz del Tip)
            for (int i = 0; i < estudiantes.Length; i++)
            {
                Console.WriteLine($"Struct -> Nombre: {estudiantes[i].Nombre}, Edad: {estudiantes[i].Edad}, Promedio: {estudiantes[i].Promedio}");
                Console.WriteLine($"  Matriz: [{estudiantes[i].CalificacionesMatriz[0,0]}, {estudiantes[i].CalificacionesMatriz[0,1]}, ...]");
            }

            // -------------------------------------------------------------------------
            // ACTIVIDAD: Modificación
            // -------------------------------------------------------------------------
            // Cambiar el promedio de un estudiante específico (Carlos).
            Console.WriteLine("\n>>> Actividad: Modificación del promedio de Carlos de forma directa...");
            estudiantes[0].Promedio = 4.0;
            Console.WriteLine($"Nuevo promedio de Carlos: {estudiantes[0].Promedio}\n");
            
            // -------------------------------------------------------------------------
            // ACTIVIDAD: Comparativa
            // -------------------------------------------------------------------------
            Console.WriteLine("\n>>> Actividad: Comparativa");
            Console.WriteLine("    -> (En C# los Structs son Value Types pasados por copia,");
            Console.WriteLine("        en Python emulamos esto con Dataclasses). Las diferencias");
            Console.WriteLine("        completas se documentan en el README y el PDF.\n");
        }
    }
}
