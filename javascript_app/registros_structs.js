const readline = require('readline');

// Para leer datos por consola en JS uso esta interfaz que es la estándar de Node.
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// ¡Hola! Al programar este punto, me di cuenta de que JavaScript no tiene la palabra 'struct' nativa.
// Pero para cumplir con el requerimiento de una "agrupación de datos puros sin comportamiento", 
// utilicé Objetos Literales en formato JSON. Esta es la forma más ligera en JS de simular un Record en memoria.
function solicitarDatosEstudiante(callback) {
    rl.question("Ingrese el nombre del estudiante: ", (nombre) => {
        rl.question(`Ingrese la edad de ${nombre}: `, (edadStr) => {
            rl.question(`Ingrese el promedio de ${nombre} (ej: 4.5): `, (promedioStr) => {
                const edad = parseInt(edadStr);
                const promedio = parseFloat(promedioStr);

                if (isNaN(edad) || isNaN(promedio)) {
                    console.log("Error: Los datos numéricos no son válidos.");
                    callback(null);
                } else {
                    // Aquí construyo mi "Struct" simulado. Solo tiene variables, nada de lógica.
                    const nuevoStruct = { nombre: nombre, edad: edad, promedio: promedio };
                    callback(nuevoStruct);
                }
            });
        });
    });
}

function iniciarPrograma() {
    console.log("\n--- Demostración del Punto 3: Simulación de Records (Structs) en JS ---");

    // Instancio 3 estudiantes base en mis structs simulados, tal como pide la rúbrica.
    const estudiante1 = { nombre: "Ana Perez", edad: 20, promedio: 4.2 };
    const estudiante2 = { nombre: "Luis Gomez", edad: 22, promedio: 3.5 };
    const estudiante3 = { nombre: "Maria Lopez", edad: 19, promedio: 4.8 };

    // Guardo los structs en un arreglo
    const arregloEstudiantes = [estudiante1, estudiante2, estudiante3];
    console.log("El sistema ha cargado 3 registros por defecto.");

    // Función recursiva para poder preguntar al profesor si desea añadir varios estudiantes
    function preguntar() {
        rl.question("¿Desea agregar un nuevo estudiante? (s/n): ", (respuesta) => {
            respuesta = respuesta.trim().toLowerCase();
            if (respuesta === 's') {
                solicitarDatosEstudiante((nuevo) => {
                    if (nuevo) {
                        arregloEstudiantes.push(nuevo);
                        console.log(`Estudiante '${nuevo.nombre}' agregado con éxito.`);
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
        console.log("\nEstado inicial de los registros en JavaScript:");
        arregloEstudiantes.forEach(est => {
            console.log(`Nombre: ${est.nombre} | Edad: ${est.edad} | Promedio Actual: ${est.promedio}`);
        });

        // Demuestro que esto actúa como un struct al acceder y alterar la variable directamente
        console.log("\nEjecutando la actualización del promedio para 'Luis Gomez' a 4.0...");
        if (arregloEstudiantes.length > 1 && arregloEstudiantes[1].nombre === "Luis Gomez") {
            arregloEstudiantes[1].promedio = 4.0;
        }

        console.log("\nRevisión del estado después de la actualización:");
        arregloEstudiantes.forEach(est => {
            console.log(`Nombre: ${est.nombre} | Edad: ${est.edad} | Promedio Actual: ${est.promedio}`);
        });
        console.log("--------------------------------------------------------------------\n");
        rl.close();
    }

    preguntar();
}

iniciarPrograma();
