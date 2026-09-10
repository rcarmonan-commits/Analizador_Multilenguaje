using System;

namespace CSharpApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Iniciando Módulos del Protocolo Individual...\n");

            // Ejecuta demostración de Structs
            RegistrosStructs.ProbarStructs();

            // Ejecuta demostración de Clases
            ObjetosClases.ProbarObjetos();

            // Ejecuta analizador integrador
            AnalizadorArchivos.EjecutarAnalizador();
        }
    }
}
