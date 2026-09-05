using System;
using System.IO;
using System.Linq;

namespace CSharpApp
{
    // =========================================================================
    // ACTIVIDAD PRÁCTICA: ANALIZADOR DE ARCHIVOS 
    // =========================================================================
    // RUBRICA: "Modificar el ejercicio asignado en la actividad Protocolo Individual 
    // Unidad 1 y aplicar los conceptos de Objetos, Struct y Récord como elementos 
    // guardados en los arreglos o matrices."
    // 
    // EXPLICACION: Para no alterar la naturaleza original del Ejercicio 6 (analizar numeros), 
    // y mantener el codigo TOTALMENTE SEPARADO de los estudiantes, hemos creado un  
    // Objeto llamado 'RegistroNumerico'. Así aplicamos la POO exactamente como dice 
    // el profesor sin arruinar la logica de los numeros.

    // -------------------------------------------------------------------------
    // 1. APLICANDO CONCEPTOS DE OBJETOS: Creación de la clase para el arreglo
    // -------------------------------------------------------------------------
    public class RegistroNumerico
    {
        public double Valor { get; set; }

        public RegistroNumerico(double valor)
        {
            Valor = valor;
        }
    }

    public class AnalizadorArchivos
    {
        public static void EjecutarAnalizador()
        {
            Console.WriteLine("\n=======================================================");
            Console.WriteLine(" EJECUTANDO ACTIVIDAD PRÁCTICA: Analizador de Archivos (C#)");
            Console.WriteLine("=======================================================");
            Console.WriteLine("\n>>> Actividad: Modificar el Ejercicio 6 leyendo Objetos en un Arreglo...");
            
            string archivoEntrada = "numeros_entrada.txt";
            string archivoSalida = "resultados_csharp.txt";

            if (!File.Exists(archivoEntrada))
            {
                File.WriteAllLines(archivoEntrada, new string[] { "32", "45", "18", "50", "29" });
            }

            Console.WriteLine($"Leyendo el archivo de disco: {archivoEntrada}");

            // =========================================================================
            // 2. MODIFICACION DEL EJERCICIO ORIGINAL: LEER Y GUARDAR COMO OBJETOS
            // =========================================================================
            // El codigo original de Java leia ints/doubles primitivos. 
            // Aquí instanciamos un Objeto por cada numero leido y lo guardamos 
            // en un arreglo de Objetos, cumpliendo la exigencia principal.
            string[] lineas = File.ReadAllLines(archivoEntrada);
            RegistroNumerico[] arregloObjetos = new RegistroNumerico[lineas.Length];

            for (int i = 0; i < lineas.Length; i++)
            {
                double numero = Convert.ToDouble(lineas[i]);
                arregloObjetos[i] = new RegistroNumerico(numero);
            }

            // =========================================================================
            // 3. CALCULAR ESTADISTICAS (Iterando sobre el arreglo de Objetos)
            // =========================================================================
            double suma = 0;
            double maximo = arregloObjetos[0].Valor;
            double minimo = arregloObjetos[0].Valor;

            foreach (var obj in arregloObjetos)
            {
                double val = obj.Valor;
                suma += val;
                if (val > maximo) maximo = val;
                if (val < minimo) minimo = val;
            }

            double promedio = Math.Round(suma / arregloObjetos.Length, 2);

            // =========================================================================
            // 4. ORDENAR ARREGLO DE OBJETOS Y GUARDAR RESULTADOS
            // =========================================================================
            arregloObjetos = arregloObjetos.OrderBy(o => o.Valor).ToArray();

            using (StreamWriter fw = new StreamWriter(archivoSalida))
            {
                fw.WriteLine("=== REPORTE ESTADISTICO ===");
                fw.WriteLine($"Archivo origen: {archivoEntrada}");
                fw.WriteLine($"Cantidad de datos: {arregloObjetos.Length}\n");
                
                fw.WriteLine($"Minimo: {minimo}");
                fw.WriteLine($"Maximo: {maximo}");
                fw.WriteLine($"Promedio: {promedio}\n");

                fw.WriteLine("=== DATOS ORDENADOS ===");
                foreach (var obj in arregloObjetos)
                {
                    fw.WriteLine($"{obj.Valor}");
                }
            }

            Console.WriteLine($"-> Analisis exitoso. Reporte guardado en '{archivoSalida}'.\n");
        }
    }
}
