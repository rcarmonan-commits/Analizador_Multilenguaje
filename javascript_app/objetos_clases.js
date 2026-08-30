const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// A diferencia del archivo anterior donde usé objetos JSON estáticos (structs simulados),
// aquí utilizo la sintaxis de Programación Orientada a Objetos introducida en ES6 (ECMAScript 6).
// Ahora tenemos un constructor real, métodos internos y encapsulamiento. Esto vive en la memoria Heap.
class EstudianteObjeto {
    constructor(nombre, edad, promedio) {
        this.nombre = nombre;
        this.edad = edad;
        this.promedio = promedio;
    }

    // Este es un comportamiento propio del objeto. Él mismo sabe cómo imprimirse, no necesito 
    // sacar las variables desde afuera para imprimirlas como lo hice con el struct.
    mostrarInfo() {
        console.log(`[Datos del Objeto] Estudiante: ${this.nombre} | Edad: ${this.edad} | Promedio: ${this.promedio}`);
    }

    // Método setter para encapsular la actualización de la nota
    setPromedio(nuevoPromedio) {
        this.promedio = nuevoPromedio;
        console.log(`Evento: El promedio de ${this.nombre} ha sido actualizado a ${this.promedio}`);
    }
}

function solicitarDatosObjeto(callback) {
    rl.question("Ingrese el nombre del estudiante: ", (nombre) => {
        rl.question(`Ingrese la edad de ${nombre}: `, (edadStr) => {
            rl.question(`Ingrese el promedio de ${nombre} (ej: 4.5): `, (promedioStr) => {
                const edad = parseInt(edadStr);
                const promedio = parseFloat(promedioStr);

                if (isNaN(edad) || isNaN(promedio)) {
                    console.log("Error: Los datos numéricos no son válidos.");
                    callback(null);
                } else {
                    // Utilizo la palabra 'new' para reservar espacio dinámico en la memoria Heap
                    const nuevoObjeto = new EstudianteObjeto(nombre, edad, promedio);
                    callback(nuevoObjeto);
                }
            });
        });
    });
}

function iniciarPrograma() {
    console.log("\n--- Demostración del Punto 4: Clases y Objetos reales en JS ---");

    // Instancio 3 objetos con la palabra clave 'new'
    const est1 = new EstudianteObjeto("Carlos Ruiz", 21, 3.8);
    const est2 = new EstudianteObjeto("Diana Vargas", 23, 4.5);
    const est3 = new EstudianteObjeto("Roberto Carlos", 20, 3.2);

    const arregloObjetos = [est1, est2, est3];
    console.log("Se han instanciado 3 objetos Estudiante por defecto.");

    function preguntar() {
        rl.question("¿Desea instanciar un nuevo estudiante? (s/n): ", (respuesta) => {
            respuesta = respuesta.trim().toLowerCase();
            if (respuesta === 's') {
                solicitarDatosObjeto((nuevo) => {
                    if (nuevo) {
                        arregloObjetos.push(nuevo);
                        console.log(`Objeto '${nuevo.nombre}' agregado con éxito.`);
                    }
                    preguntar();
                });
            } else if (respuesta === 'n') {
                mostrarResultados();
            } else {
                console.log("Opción no válida. Ingrese 's' o 'n'.");
                preguntar();
            }
        });
    }

    function mostrarResultados() {
        console.log("\nInvocando el comportamiento interno (método) de cada objeto en el arreglo:");
        arregloObjetos.forEach(estudiante => {
            // Ya no hago un print feo, sino que le pido al objeto que ejecute su propio código
            estudiante.mostrarInfo();
        });

        console.log("\nAplicando una actualización del estado utilizando un método del objeto...");
        if (arregloObjetos.length > 2 && arregloObjetos[2].nombre === "Roberto Carlos") {
            // Accedo al setter en lugar de acceder a la variable de forma insegura
            arregloObjetos[2].setPromedio(4.0);
        }

        console.log("\nComprobación del estado final del objeto modificado:");
        if (arregloObjetos.length > 2 && arregloObjetos[2].nombre === "Roberto Carlos") {
            arregloObjetos[2].mostrarInfo();
        }
        console.log("----------------------------------------------------------------------\n");
        rl.close();
    }

    preguntar();
}

iniciarPrograma();
