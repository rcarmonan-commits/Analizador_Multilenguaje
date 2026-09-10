"""
=============================================================
  Suite de Tests - Analizador Multilenguaje (Python)
  Autor: rcarmonan-commits
  Descripcion: Tests unitarios y de integración para los módulos
               registros_structs, objetos_clases y analizador_archivos
=============================================================
"""
import unittest
import os
import sys

# Aseguramos que el directorio actual esté en el path para importar los módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dataclasses import dataclass
import registros_structs
import objetos_clases
import analizador_archivos


# ============================================================
# TESTS PARA: registros_structs.py (Punto 3 - Struct/Record)
# ============================================================
class TestEstudianteStruct(unittest.TestCase):

    def setUp(self):
        """Crea instancias de prueba antes de cada test."""
        self.e1 = registros_structs.EstudianteStruct("Carlos", 20, 3.5)
        self.e2 = registros_structs.EstudianteStruct("Maria", 22, 4.8)
        self.e3 = registros_structs.EstudianteStruct("Juan", 19, 2.1)

    def test_creacion_nombre(self):
        """Verifica que el nombre se asigna correctamente."""
        self.assertEqual(self.e1.nombre, "Carlos")

    def test_creacion_edad(self):
        """Verifica que la edad se asigna correctamente."""
        self.assertEqual(self.e1.edad, 20)

    def test_creacion_promedio(self):
        """Verifica que el promedio se asigna correctamente."""
        self.assertAlmostEqual(self.e1.promedio, 3.5)

    def test_matriz_tiene_dos_filas(self):
        """La matriz encapsulada debe tener 2 filas."""
        self.assertEqual(len(self.e1.calificaciones_matriz), 2)

    def test_matriz_tiene_tres_columnas(self):
        """Cada fila de la matriz debe tener 3 columnas."""
        for fila in self.e1.calificaciones_matriz:
            self.assertEqual(len(fila), 3)

    def test_primer_elemento_matriz_igual_a_promedio(self):
        """El primer elemento de la fila 0 debe ser igual al promedio."""
        self.assertAlmostEqual(self.e1.calificaciones_matriz[0][0], self.e1.promedio)

    def test_modificacion_promedio_directo(self):
        """En un Struct/Dataclass el atributo es modificable directamente."""
        self.e1.promedio = 4.0
        self.assertAlmostEqual(self.e1.promedio, 4.0)

    def test_arreglo_de_tres_structs(self):
        """Verifica que se pueden guardar 3 instancias en una lista."""
        arreglo = [self.e1, self.e2, self.e3]
        self.assertEqual(len(arreglo), 3)
        self.assertEqual(arreglo[1].nombre, "Maria")

    def test_promedio_maria(self):
        """Verifica el promedio de María específicamente."""
        self.assertAlmostEqual(self.e2.promedio, 4.8)

    def test_edad_juan(self):
        """Verifica la edad de Juan."""
        self.assertEqual(self.e3.edad, 19)

    def test_probar_structs_no_lanza_excepcion(self):
        """La función probar_structs() debe ejecutarse sin lanzar errores."""
        try:
            registros_structs.probar_structs()
        except Exception as e:
            self.fail(f"probar_structs() lanzó una excepción: {e}")


# ============================================================
# TESTS PARA: objetos_clases.py (Punto 4 - Clases/Objetos)
# ============================================================
class TestEstudianteClase(unittest.TestCase):

    def setUp(self):
        """Crea instancias de prueba antes de cada test."""
        self.luis  = objetos_clases.Estudiante("Luis", 21, 3.8)
        self.ana   = objetos_clases.Estudiante("Ana", 23, 4.5)
        self.pedro = objetos_clases.Estudiante("Pedro", 18, 2.9)

    def test_getter_promedio_luis(self):
        """El getter debe retornar el promedio correcto de Luis."""
        self.assertAlmostEqual(self.luis.get_promedio(), 3.8)

    def test_setter_modifica_promedio(self):
        """El setter debe modificar el promedio correctamente."""
        self.luis.set_promedio(4.5)
        self.assertAlmostEqual(self.luis.get_promedio(), 4.5)

    def test_setter_no_altera_otros_objetos(self):
        """Modificar a Luis no debe alterar el promedio de Ana."""
        self.luis.set_promedio(1.0)
        self.assertAlmostEqual(self.ana.get_promedio(), 4.5)

    def test_encapsulamiento_atributo_privado(self):
        """Los atributos privados (doble guion bajo) no deben ser accesibles directamente."""
        with self.assertRaises(AttributeError):
            _ = self.luis.__nombre   # Debe fallar por name mangling de Python

    def test_arreglo_de_tres_objetos(self):
        """Verifica que se pueden almacenar 3 objetos Estudiante en una lista."""
        arreglo = [self.luis, self.ana, self.pedro]
        self.assertEqual(len(arreglo), 3)

    def test_mostrar_info_no_lanza_excepcion(self):
        """mostrar_info() debe ejecutarse sin excepciones."""
        try:
            self.luis.mostrar_info()
        except Exception as e:
            self.fail(f"mostrar_info() lanzó una excepción: {e}")

    def test_promedio_pedro(self):
        """Verifica el promedio de Pedro."""
        self.assertAlmostEqual(self.pedro.get_promedio(), 2.9)

    def test_setter_con_valor_maximo(self):
        """El setter debe aceptar el valor máximo de calificación (5.0)."""
        self.ana.set_promedio(5.0)
        self.assertAlmostEqual(self.ana.get_promedio(), 5.0)

    def test_setter_con_valor_cero(self):
        """El setter debe aceptar el valor cero."""
        self.pedro.set_promedio(0.0)
        self.assertAlmostEqual(self.pedro.get_promedio(), 0.0)

    def test_probar_objetos_no_lanza_excepcion(self):
        """La función probar_objetos() debe ejecutarse sin lanzar errores."""
        try:
            objetos_clases.probar_objetos()
        except Exception as e:
            self.fail(f"probar_objetos() lanzó una excepción: {e}")


# ============================================================
# TESTS PARA: analizador_archivos.py (Actividad Práctica Final)
# ============================================================
class TestAnalizadorArchivos(unittest.TestCase):

    def setUp(self):
        """Prepara archivos de prueba temporales antes de cada test."""
        self.archivo_entrada = "test_numeros_entrada.txt"
        self.archivo_salida  = "test_resultados.txt"
        # Escribimos datos conocidos para poder verificar los cálculos
        with open(self.archivo_entrada, "w") as f:
            for n in [10, 20, 30, 40, 50]:
                f.write(f"{n}\n")

    def tearDown(self):
        """Limpia los archivos temporales después de cada test."""
        for archivo in [self.archivo_entrada, self.archivo_salida,
                        "numeros_entrada.txt", "resultados_python.txt"]:
            if os.path.exists(archivo):
                os.remove(archivo)

    def test_registro_numerico_crea_correctamente(self):
        """RegistroNumerico debe guardar el valor asignado."""
        reg = analizador_archivos.RegistroNumerico(42.0)
        self.assertAlmostEqual(reg.valor, 42.0)

    def test_suma_correcta(self):
        """Verifica que la suma de [10,20,30,40,50] = 150."""
        valores = [10.0, 20.0, 30.0, 40.0, 50.0]
        objetos = [analizador_archivos.RegistroNumerico(v) for v in valores]
        suma = sum(o.valor for o in objetos)
        self.assertAlmostEqual(suma, 150.0)

    def test_promedio_correcto(self):
        """Verifica que el promedio de [10,20,30,40,50] = 30.0."""
        valores = [10.0, 20.0, 30.0, 40.0, 50.0]
        objetos = [analizador_archivos.RegistroNumerico(v) for v in valores]
        promedio = sum(o.valor for o in objetos) / len(objetos)
        self.assertAlmostEqual(promedio, 30.0)

    def test_maximo_correcto(self):
        """Verifica que el máximo de [10,20,30,40,50] = 50."""
        valores = [10.0, 20.0, 30.0, 40.0, 50.0]
        objetos = [analizador_archivos.RegistroNumerico(v) for v in valores]
        maximo = max(o.valor for o in objetos)
        self.assertAlmostEqual(maximo, 50.0)

    def test_minimo_correcto(self):
        """Verifica que el mínimo de [10,20,30,40,50] = 10."""
        valores = [10.0, 20.0, 30.0, 40.0, 50.0]
        objetos = [analizador_archivos.RegistroNumerico(v) for v in valores]
        minimo = min(o.valor for o in objetos)
        self.assertAlmostEqual(minimo, 10.0)

    def test_ordenamiento_correcto(self):
        """Verifica que el ordenamiento funciona con lista desordenada."""
        valores = [30.0, 10.0, 50.0, 20.0, 40.0]
        objetos = [analizador_archivos.RegistroNumerico(v) for v in valores]
        objetos.sort(key=lambda x: x.valor)
        ordenados = [o.valor for o in objetos]
        self.assertEqual(ordenados, [10.0, 20.0, 30.0, 40.0, 50.0])

    def test_ejecutar_analizador_genera_archivo_salida(self):
        """ejecutar_analizador() debe generar el archivo 'resultados_python.txt'."""
        analizador_archivos.ejecutar_analizador()
        self.assertTrue(os.path.exists("resultados_python.txt"),
                        "No se generó el archivo resultados_python.txt")

    def test_archivo_salida_contiene_reporte(self):
        """El archivo de salida debe contener 'REPORTE ESTADISTICO'."""
        analizador_archivos.ejecutar_analizador()
        with open("resultados_python.txt", "r") as f:
            contenido = f.read()
        self.assertIn("REPORTE ESTADISTICO", contenido)

    def test_archivo_salida_contiene_minimo(self):
        """El archivo de salida debe contener la línea 'Minimo:'."""
        analizador_archivos.ejecutar_analizador()
        with open("resultados_python.txt", "r") as f:
            contenido = f.read()
        self.assertIn("Minimo:", contenido)

    def test_archivo_salida_contiene_maximo(self):
        """El archivo de salida debe contener la línea 'Maximo:'."""
        analizador_archivos.ejecutar_analizador()
        with open("resultados_python.txt", "r") as f:
            contenido = f.read()
        self.assertIn("Maximo:", contenido)

    def test_archivo_salida_contiene_promedio(self):
        """El archivo de salida debe contener la línea 'Promedio:'."""
        analizador_archivos.ejecutar_analizador()
        with open("resultados_python.txt", "r") as f:
            contenido = f.read()
        self.assertIn("Promedio:", contenido)

    def test_archivo_salida_contiene_datos_ordenados(self):
        """El archivo de salida debe contener la sección 'DATOS ORDENADOS'."""
        analizador_archivos.ejecutar_analizador()
        with open("resultados_python.txt", "r") as f:
            contenido = f.read()
        self.assertIn("DATOS ORDENADOS", contenido)

    def test_ejecutar_analizador_no_lanza_excepcion(self):
        """ejecutar_analizador() no debe lanzar ninguna excepción."""
        try:
            analizador_archivos.ejecutar_analizador()
        except Exception as e:
            self.fail(f"ejecutar_analizador() lanzó una excepción: {e}")


# ============================================================
# PUNTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    print("\n" + "="*60)
    print("  EJECUTANDO SUITE DE TESTS - Analizador Multilenguaje")
    print("="*60 + "\n")
    unittest.main(verbosity=2)
