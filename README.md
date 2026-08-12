# Actividad Unidad 1 - Protocolo Actividad de Aprendizaje Individual

**Asignatura:** Estructuras de datos
**Programa:** Ingeniería del software
**IES:** Universidad de Cartagena
**Estudiante:** Rosary Carmona
**Tutor:** John Carlos Arrieta Arrieta

---

## Presentación

Hola, mi nombre es Rosary Carmona. Presento a continuación mi desarrollo para el Protocolo Individual correspondiente a la Unidad 1. He aplicado los conceptos de programación orientada a objetos y estructuras de datos utilizando **Python** y **C#**, integrando los desarrollos en ramas independientes con Git, absteniéndome estrictamente de usar Java tal como lo indica la rúbrica.

---

## Introducción

El presente proyecto documenta el aprendizaje fundamental y práctico sobre la evolución del almacenamiento de datos en memoria. A través de la resolución de problemas en dos lenguajes distintos (C# como lenguaje estático y Python como lenguaje dinámico), analizaremos las agrupaciones de datos pasivas (Structs y Records), hasta llegar al encapsulamiento y comportamiento activo de los Objetos (Clases). Todo el desarrollo se maneja utilizando el sistema de control de versiones Git.

---

## Objetivos

**Objetivo General:**
Comprender y aplicar la evolución de las estructuras de datos, desde agrupaciones estáticas (Arreglos) hacia agrupaciones complejas y encapsuladas (Structs y Objetos) utilizando Python y C# bajo un sistema de control de versiones.

**Objetivos Específicos:**
- Emular e implementar `Records/Structs` puros enfocados únicamente en el almacenamiento de datos.
- Declarar y construir Objetos y Clases modernas encapsulando atributos y métodos propios.
- Desarrollar un "Analizador de Archivos" leyendo desde un archivo de texto e iterando un arreglo de objetos para procesar sus atributos numéricamente.
- Controlar las modificaciones de código bajo el sistema Git, aislando el trabajo en ramas (branches) independientes y fusionándolas de forma segura.

---

## Justificación

Entender cómo la programación pasó de usar simples arreglos a crear "moldes" personalizados (Structs y Clases) es vital para el desarrollo de software moderno. Las estructuras primitivas no escalan bien cuando necesitamos almacenar mucha información de una sola entidad (por ejemplo, nombre, edad y promedio de un estudiante). Al usar Objetos y Records, organizamos la memoria lógicamente. Aplicar esto en lenguajes como C# (fuertemente tipado) y Python (dinámico) demuestra versatilidad profesional y una comprensión profunda del manejo de memoria (Stack vs Heap).

---

## Fundamentos Teóricos

### 1. Records o Structs
- **Definición:** Son estructuras de datos pasivas que aglutinan múltiples valores (atributos) relacionados bajo un solo nombre. A diferencia de las clases, no suelen contener lógica compleja o métodos.
- **Tipado y acceso a campos:** En lenguajes estáticos como C#, los campos tienen un tipo fuertemente definido y se accede a ellos con la notación de punto (`estudiante.nombre`).
- **Mutabilidad:** En lenguajes como C#, los structs son por defecto inmutables o mutables solo reasignando toda la copia de la estructura.
- **Uso en memoria:** Residen en la pila (**Stack**), lo que los hace extremadamente rápidos de crear y destruir, ya que no requieren recolección de basura.

### 2. Objetos (Clases)
- **Definición:** Son entidades activas que combinan datos (estado/atributos) y comportamiento (métodos). Proveen mecanismos avanzados como el encapsulamiento.
- **Mutabilidad:** Son dinámicamente mutables; se puede alterar su estado en tiempo de ejecución a través de sus métodos públicos (Getters/Setters).
- **Uso en memoria:** Se instancian en el montículo (**Heap**), por lo que se pasan por referencia y su limpieza depende del Recolector de Basura (Garbage Collector).

---

## Desarrollo

A continuación presento mi proceso lógico y de desarrollo detallado para dar respuesta a los requerimientos:

### Paso 1: Implementación de Records / Structs (Punto 3)

Desarrollé la lógica en `registros_structs.py` (Python) y `RegistrosStructs.cs` (C#), cumpliendo con los siguientes ítems de la rúbrica:

1. **Declaración:** Definí un struct `EstudianteStruct` con nombre, edad, promedio y un arreglo bidimensional (2x3) de calificaciones para cumplir con el Tip de evaluación.
2. **Inicialización:** Creé 3 instancias de estudiantes con sus respectivos datos.
3. **Recorrido:** Almacené las instancias en un arreglo y las recorrí para mostrar sus datos.
4. **Modificación:** Accedí directamente al atributo público para cambiar el promedio de un estudiante específico.
5. **Comparativa:** Demostré cómo los structs son colecciones simples de datos sin métodos internos.

```text
--- PUNTO 3: RECORDS Y STRUCTS (PYTHON) ---
>>> Actividad: Inicializacion y Recorrido
Estudiante: Juan Perez, Edad: 20, Promedio: 4.5, Notas: [[4.0, 4.5, 4.2], [4.6, 4.8, 5.0]]
Estudiante: Maria Gomez, Edad: 22, Promedio: 4.8, Notas: [[4.8, 4.9, 4.7], [5.0, 5.0, 4.9]]
Estudiante: Carlos Lopez, Edad: 21, Promedio: 3.9, Notas: [[3.5, 3.8, 4.0], [4.1, 3.9, 4.2]]

>>> Actividad: Modificacion
Cambiando el promedio de Juan Perez directamente...
Nuevo promedio de Juan Perez: 4.7

>>> Actividad: Comparativa
A diferencia de una clase, este Record es puramente de almacenamiento de datos y no tiene metodos encapsulados.
```

### Paso 2: Implementación de Objetos y Clases (Punto 4)

Desarrollé la lógica en `objetos_clases.py` y `ObjetosClases.cs` aplicando POO:

1. **Declaración:** Definí la clase `EstudianteClase` encapsulando los atributos y añadiendo el método `mostrarInfo()`.
2. **Inicialización:** Instancié 3 objetos Estudiante.
3. **Recorrido:** Iteré sobre el arreglo de objetos invocando su método `mostrarInfo()`.
4. **Modificación:** Cambié el promedio utilizando el método Setter encapsulado `set_promedio()`.
5. **Comparativa:** Expliqué en comentarios la diferencia de encapsulamiento respecto a un Struct.

```text
--- PUNTO 4: OBJETOS Y CLASES (PYTHON) ---
>>> Actividad: Inicializacion y Recorrido
[Info] Estudiante: Ana Torres, Edad: 23, Promedio: 4.2, Notas: [[4.0, 4.2, 4.1], [4.5, 4.3, 4.4]]
[Info] Luis Fernandez, Edad: 19, Promedio: 3.5, Notas: [[3.0, 3.5, 3.2], [3.8, 3.6, 3.9]]
[Info] Sofia Ramirez, Edad: 20, Promedio: 4.6, Notas: [[4.5, 4.6, 4.4], [4.8, 4.7, 4.9]]

>>> Actividad: Modificacion
Cambiando el promedio de Ana Torres usando un metodo setter...
Nuevo promedio de Ana Torres modificado de forma segura.

>>> Actividad: Comparativa
A diferencia de un Struct, la Clase protege sus atributos (encapsulamiento) y expone metodos como set_promedio().
```

### Paso 3: Analizador Integrador (Actividad Práctica - Ejercicio 6)

Se replicó el "Analizador de Archivos Numéricos" utilizando arreglos de Objetos:

1. En lugar de usar arreglos primitivos, el sistema lee `numeros.txt` y por cada número crea un objeto `RegistroNumerico`.
2. Estos objetos se almacenan en un arreglo.
3. Se itera el arreglo de objetos para extraer el valor interno y calcular Mínimo, Máximo y Promedio.
4. Los resultados se guardan en un nuevo archivo de texto, demostrando el uso avanzado de POO en procesamiento de archivos.

```text
--- ACTIVIDAD PRACTICA: ANALIZADOR DE ARCHIVOS CON OBJETOS ---
Leyendo el archivo 'numeros.txt'...
Creando objetos RegistroNumerico...
Calculando estadisticas a partir del arreglo de objetos...

Estadisticas generadas:
- Minimo: 3.0
- Maximo: 98.0
- Promedio: 45.2
-> Resultados guardados exitosamente en 'resultados_python.txt'
```

### Paso 4: Implementación de Control de Versiones con Git

Para cumplir con las exigencias metodológicas de la actividad, el código en Python y C# se desarrolló en ramas separadas y se versionó bajo Git.

A continuación, se evidencian los comandos exactos ejecutados:

**1. Para el desarrollo en Python (Structs, Clases y Analizador):**
```bash
git switch main
git pull
git switch -c rama-python
git status
git add .
git commit -m "feat(python): implementacion de records y structs mediante diccionarios y namedtuples"
git commit -m "feat(python): creacion de clases, objetos y analizador integrador"
git push origin rama-python
git switch main
git pull
git merge rama-python
git push origin main
```

**2. Para el desarrollo en C# (Structs, Clases y Analizador):**
```bash
git switch main
git pull
git switch -c rama-csharp
git status
git add .
git commit -m "feat(csharp): implementacion de records puros con structs tipo valor"
git commit -m "feat(csharp): desarrollo de clases con encapsulamiento real y analizador integrador"
git push origin rama-csharp
git switch main
git pull
git merge rama-csharp
git push origin main
```

---

## Diferencias entre Struct/Record y Objetos (Tabla Comparativa)

| Característica | Struct / Record (C#) - Estático | Objeto (Python) - Dinámico |
| --- | --- | --- |
| **Definición** | Colección de datos pasiva. | Entidad activa con estado y métodos. |
| **Mutabilidad** | Inmutables por defecto o reasignando copia. | Mutables dinámicamente en tiempo de ejecución. |
| **Tipado** | Estático y fuertemente tipado en declaración. | Dinámico ("Duck Typing"). |
| **Uso en memoria**| Pila (**Stack**), rápido y sin recolector. | Montículo (**Heap**), con Garbage Collection. |
| **Ejemplo** | `public struct EstudianteStruct {...}` | `class Estudiante: def __init__(self): ...` |

---

## Enlace del repositorio público de GitHub

https://github.com/rcarmonan-commits/Analizador_Multilenguaje

### 🌳 Árbol de commits (git log --oneline --graph)

```text
*   0432b75 Merge branch 'rama-csharp'
|\  
| * 0c57ade feat(csharp): desarrollo de clases con encapsulamiento real y analizador integrador
| * 86cc727 feat(csharp): implementacion de records puros con structs tipo valor
|/  
*   e4232bf Merge branch 'rama-python'
|\  
| * 0ebd426 feat(python): creacion de clases, objetos y analizador integrador
| * f0e2f5f feat(python): implementacion de records y structs mediante diccionarios y namedtuples
|/  
* aee9ca8 feat: iniciando proyecto individual multilenguaje (Estructuras de datos)
```

---

## Enlace del video de sustentación

[ Inserte aquí el enlace de YouTube / Google Drive con el video explicando el código, probando la ejecución y mostrando el rostro y voz del alumno ]
