using System;

namespace CSharpApp
{
    // =========================================================================
    // PUNTO 4 DE LA RUBRICA: Objetos (Clases e instancias)
    // =========================================================================
    
    // -------------------------------------------------------------------------
    // ACTIVIDAD: Declaración
    // -------------------------------------------------------------------------
    // Definir una clase Estudiante con: nombre, edad, promedio y un método mostrarInfo.
    public class Estudiante
    {
        // En una Clase verdadera aplicamos ENCAPSULAMIENTO (atributos privados)
        private string nombre;
        private int edad;
        private double promedio;
        
        // 💡 TIP EVALUACION FINAL: 
        // Usar un arreglo de objetos que contenga un campo que sea a su vez una matriz.
        private double[,] calificacionesMatriz;

        public Estudiante(string nombre, int edad, double promedio)
        {
            this.nombre = nombre;
            this.edad = edad;
            this.promedio = promedio;
            
            // Se crea una matriz 2x3 interna como pide el TIP de evaluacion
            this.calificacionesMatriz = new double[2, 3] {
                { promedio, Math.Round(promedio - 0.2, 2), Math.Round(promedio + 0.1, 2) },
                { Math.Round(promedio + 0.1, 2), promedio, Math.Round(promedio - 0.1, 2) }
            };
        }

        // Setter encapsulado para modificar el promedio de forma segura
        public void SetPromedio(double nuevoPromedio)
        {
            this.promedio = nuevoPromedio;
        }

        public double GetPromedio()
        {
            return this.promedio;
        }

        // -------------------------------------------------------------------------
        // ACTIVIDAD: Recorrido (Método propio)
        // -------------------------------------------------------------------------
        // Método MostrarInfo exigido por la rubrica
        public void MostrarInfo()
        {
            Console.WriteLine($"Objeto Clase -> Nombre: {nombre}, Edad: {edad}, Promedio: {promedio}");
            Console.WriteLine($"  Matriz Encapsulada: [{calificacionesMatriz[0,0]}, {calificacionesMatriz[0,1]}, ...]");
        }
    }

    public class ObjetosClases
    {
        public static void ProbarObjetos()
        {
            Console.WriteLine("\n=======================================================");
            Console.WriteLine(" EJECUTANDO PUNTO 4 DE LA RUBRICA: Objetos (Clases) (C#)");
            Console.WriteLine("=======================================================");

            // -------------------------------------------------------------------------
            // ACTIVIDAD: Inicialización y Recorrido
            // -------------------------------------------------------------------------
            Console.WriteLine("\n>>> Actividad: Inicialización y Recorrido usando MostrarInfo()...");
            // Crear 3 instancias y almacenarlas en un arreglo/lista.
            Estudiante[] arregloEstudiantes = new Estudiante[3];
            arregloEstudiantes[0] = new Estudiante("Luis", 21, 3.8);
            arregloEstudiantes[1] = new Estudiante("Ana", 23, 4.5);
            arregloEstudiantes[2] = new Estudiante("Pedro", 18, 2.9);

            // Llamar al metodo mostrarInfo para cada objeto.
            foreach (Estudiante est in arregloEstudiantes)
            {
                est.MostrarInfo();
            }

            // -------------------------------------------------------------------------
            // ACTIVIDAD: Modificación
            // -------------------------------------------------------------------------
            // Cambiar el promedio de un estudiante usando métodos Setters.
            Console.WriteLine("\n>>> Actividad: Modificación del promedio de Luis usando Setter Encapsulado...");
            arregloEstudiantes[0].SetPromedio(4.5);
            Console.WriteLine($"Nuevo promedio de Luis (Leido por Getter): {arregloEstudiantes[0].GetPromedio()}\n");

            // -------------------------------------------------------------------------
            // ACTIVIDAD: Comparativa
            // -------------------------------------------------------------------------
            Console.WriteLine("\n>>> Actividad: Comparativa");
            Console.WriteLine("    -> (Las Clases definen estado y comportamiento, operan por");
            Console.WriteLine("        referencia en el Heap, a diferencia del Struct que es");
            Console.WriteLine("        un tipo por valor en el Stack).\n");
        }
    }
}
