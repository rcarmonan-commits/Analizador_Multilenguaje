# Protocolo Actividad de Aprendizaje Individual - Unidad 1
**Asignatura:** Estructuras de Datos  
**Programa:** Ingeniería de Software (4to Semestre)  
**Institución:** Universidad de Cartagena  
**Estudiante:** Rosary Carmona  
**Tutor:** John Carlos Arrieta Arrieta  

---

## Presentación
Hola, mi nombre es Rosary Carmona. Presento a continuación mi desarrollo para la primera actividad de aprendizaje de la asignatura. Como estudiante de cuarto semestre, considero que aún estoy en proceso de aprendizaje y me considero una principiante en varios de estos temas; sin embargo, he puesto todo mi esfuerzo en investigar, probar y codificar esta actividad paso a paso para apropiarme de los conceptos de memoria y estructuración de datos.

## Introducción
En el mundo del desarrollo de software, aprender a programar no se trata solo de hacer que la pantalla muestre un resultado, sino de saber cómo la computadora administra esos datos por detrás. En esta actividad, exploramos la diferencia fundamental entre estructuras sencillas (que solo guardan datos) y estructuras complejas orientadas a objetos (que guardan datos y también tienen comportamientos). Para hacer este reto más interesante y cumplir con la regla del tutor de "NO JAVA", decidí trabajar mi proyecto utilizando dos lenguajes muy populares: Python y JavaScript. Elegí JavaScript específicamente porque, a pesar de sus limitaciones técnicas, es el lenguaje de la web y me pareció un excelente reto intelectual emular conceptos de bajo nivel en él.

## Objetivos
- Entender en la práctica cómo funciona un Record o Struct frente a una Clase completa.
- Aprender a estructurar un proyecto interactivo para que no sea un código aburrido y estático.
- Demostrar el funcionamiento de arreglos de objetos leyendo información directamente desde un archivo de texto.
- Hacer uso correcto de Git, creando diferentes ramas para cada parte del código y uniéndolas al final.

## Justificación
Realizar este tipo de laboratorios prácticos es vital para mi formación como futura ingeniera. Muchas veces usamos variables sin pensar si ocupan mucha o poca memoria. Al investigar sobre el Stack (memoria estática y rápida donde suelen vivir los Structs) y el Heap (memoria dinámica donde viven los Objetos), comprendí que elegir la herramienta correcta hace que nuestros programas sean mucho más eficientes.

---

## Justificación de Lenguajes Seleccionados
Para esta actividad, la rúbrica solicitaba explícitamente no utilizar Java y elegir dos lenguajes de una lista permitida. Mi elección final fue **Python** y **JavaScript**. 

- **¿Por qué Python?** Es un lenguaje excelente para demostrar la Programación Orientada a Objetos gracias a su sintaxis limpia y a su decorador `@dataclass`, que permite simular estructuras de datos ligeras rápidamente.
- **¿Por qué JavaScript?** Inicialmente consideré buscar un lenguaje derivado de C (como C# o C++), pero me incliné por **JavaScript** al darme cuenta del gran reto que representa. Soy plenamente consciente de que JavaScript **no posee** una estructura `struct` de manera nativa en su gestión de memoria. Sin embargo, para demostrar que entiendo las bases teóricas más allá de la sintaxis, decidí simular el comportamiento de una estructura puramente orientada a datos (Struct) utilizando *Objetos Literales (JSON)* en memoria rápida, y posteriormente demostrar el encapsulamiento utilizando la sintaxis de *Clases de ES6* en el Heap. Entender y exponer las limitaciones tecnológicas de un lenguaje me pareció la mejor forma de demostrar mis conocimientos.

---

## Desarrollo de la Actividad

Para que la revisión de mi trabajo sea lo más clara y amigable posible, no quise entregar un montón de códigos sueltos. En su lugar, decidí diseñar un sistema interactivo completo. A continuación, explico detalladamente cómo desarrollé cada punto:

### 1. El Menú Principal e Interactividad
Lo primero que hice fue crear un archivo llamado `main.py`. Mi objetivo era construir un menú principal (similar al que hicimos en la actividad del Simulador de Cajero Automático hace un tiempo). Este menú le muestra al usuario 4 opciones claras para navegar por todo el proyecto. Al digitar un número, el programa llama internamente a los otros archivos que programé. Además, le agregué interactividad a todos los ejercicios: el programa no solo carga datos de prueba por defecto, sino que ahora le pregunta al profesor por consola si desea ingresar nuevos estudiantes escribiendo su nombre, edad y promedio, haciendo la experiencia mucho más dinámica.

### 2. Resolviendo el Punto 3 (Structs y Records)
Para este punto, investigué cómo crear una estructura que fuera únicamente una "caja de datos", sin métodos complejos. 
- En el lado de **Python**, descubrí que existe algo llamado `dataclass`. Lo utilicé para crear un registro de estudiante muy ligero. En mi código, inicio el programa guardando a tres estudiantes en un arreglo, y luego le permito al usuario agregar más. Finalmente, accedo directamente al promedio de uno de ellos (Luis Gomez) y lo modifico para demostrar cómo se alteran los datos en un Struct puro.
- En el lado de **JavaScript**, dado que el lenguaje no tiene Structs reales, investigué y decidí usar Objetos Literales en formato JSON. Esta es la forma más directa que tiene JavaScript para empaquetar datos puros sin tener que usar pesados constructores de clase ni métodos, emulando la teoría de un Record.

### 3. Resolviendo el Punto 4 (Clases y Objetos)
Aquí el reto era diferente, ya que debía usar el paradigma de Programación Orientada a Objetos real, es decir, juntar las variables con sus funciones.
- Para **Python**, programé una clase tradicional `Estudiante` con su respectivo método constructor. Pero la gran diferencia con el punto anterior es que aquí le programé una función interna llamada `mostrar_info()`. Es decir, ahora es el mismo objeto el que sabe cómo imprimir sus datos, yo no tengo que hacerlo desde afuera. También le agregué un método para actualizar la nota, protegiendo así los datos (encapsulamiento).
- Para **JavaScript**, usé la sintaxis de clases modernas (`class` de ES6). A diferencia de los simples JSON anteriores, aquí utilicé la palabra clave `new`, lo que le indica al motor de JavaScript que reserve un espacio dinámico en la memoria Heap para cada estudiante, encapsulando sus propios métodos. Y como pediste interactividad, le programé un escáner por consola para que puedas instanciar todos los objetos que quieras en tiempo real.

### 4. Cuadro Comparativo (Punto 5)
A partir de lo que investigué y programé, concluyo las siguientes diferencias clave:
- **Propósito:** Un Struct solo sirve para almacenar variables juntas. Una Clase sirve para almacenar variables junto con sus funciones lógicas.
- **Memoria:** Los Structs generalmente se procesan más rápido porque viven en una memoria de corto plazo (Stack). Las Clases, al ser más complejas, viven en una memoria dinámica (Heap).
- **Protección:** En un Struct, cualquiera puede entrar y cambiar un dato. En una Clase, los datos están encapsulados y ocultos, y solo se deben modificar a través de métodos permitidos.

### 5. Tip de Evaluación Final (Proyecto Integrador)
Para obtener la mejor calificación posible, modifiqué el ejercicio "Analizador de Archivos". **Cumplí con el reto de implementarlo en los DOS lenguajes (Python y JavaScript)** para comparar diferencias de sintaxis. Además, diseñé la solución para que integrara absolutamente todos los requerimientos de la actividad en un solo código:
- **Struct/Record**: En Python usé `@dataclass` (Estadisticas) y en JS usé un Objeto Literal puro, ambos exclusivamente para agrupar los datos estadísticos (minimo, maximo, promedio).
- **Matriz interna**: Creé una clase `ArchivoAnalizado` que en su interior tiene un atributo `matriz_datos`. Esta matriz (un arreglo de arreglos Nx2) almacena los números extraídos del archivo y un booleano indicando si son pares o impares. 
- **Arreglo de Objetos**: La clase principal `AnalizadorArchivos` instancia los objetos `ArchivoAnalizado` (que por dentro tienen la matriz y el struct) y los va apilando todos en un arreglo global llamado `arreglo_objetos`.
Con esta estructura anidada *(Arreglo General -> Objetos -> Matriz y Structs internos)* dejo en evidencia mi dominio de cómo combinar estructuras simples para construir entidades complejas y empaquetadas orientadas a objetos.

---

## Enlaces de Entrega

Para la entrega, me aseguré de llevar un control estricto de versiones usando Git. Creé ramas separadas (`rama-python`, `rama-javascript`, `rama-analizador`) para cada punto de la actividad y luego fui fusionando todo hacia la rama principal con mucho cuidado.

- **Enlace del repositorio público de GitHub:** [Repositorio Analizador Multilenguaje](https://github.com/rcarmonan-commits/Analizador_Multilenguaje)
- **Enlace del video de sustentación:** [AÑADIR ENLACE DEL VIDEO AQUÍ]
