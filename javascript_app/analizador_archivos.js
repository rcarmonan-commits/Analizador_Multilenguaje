const fs = require('fs');

// 1. Concepto de Récord/Struct puro (Solo datos, sin métodos) en JavaScript (Objeto Literal JSON)
// Función que simula la creación del Struct de estadísticas.
function crearEstadisticas(minimo, maximo, promedio) {
    return {
        minimo: minimo,
        maximo: maximo,
        promedio: promedio
    };
}

// 2. Concepto de Clase y Objeto (Atributos + Métodos)
// Cumpliendo con el requerimiento de tener "un arreglo de objetos que contengan 
// un campo que sea a su vez una matriz".
class ArchivoAnalizado {
    constructor(nombreArchivo, matrizDatos, estadisticas) {
        this.nombreArchivo = nombreArchivo;
        
        // ¡Aquí está el campo exigido en la rúbrica que es a su vez una matriz!
        // Guardaremos los datos en formato de matriz Nx2: [[valor, esPar], [valor, esPar], ...]
        this.matrizDatos = matrizDatos;
        
        // Guardo el struct (json) de estadísticas dentro del objeto
        this.estadisticas = estadisticas;
    }
    
    // Método de la clase para mostrar sus propios datos (Encapsulamiento)
    mostrarResumen() {
        console.log(`\n--- Resumen del Objeto: ${this.nombreArchivo} ---`);
        console.log(`Estadísticas -> Mínimo: ${this.estadisticas.minimo}, Máximo: ${this.estadisticas.maximo}, Promedio: ${this.estadisticas.promedio.toFixed(2)}`);
        console.log("Muestra de la matriz interna de datos (Valor, Es_Par):");
        
        // Imprimo solo los primeros 5 elementos de la matriz para no saturar la pantalla
        for (let i = 0; i < Math.min(5, this.matrizDatos.length); i++) {
            console.log(`  [${this.matrizDatos[i][0]}, ${this.matrizDatos[i][1]}]`);
        }
        if (this.matrizDatos.length > 5) {
            console.log("  ...");
        }
    }
}

class AnalizadorArchivos {
    constructor() {
        // Este es el arreglo de objetos principal que pide la rúbrica.
        // Aquí guardaré objetos de tipo "ArchivoAnalizado".
        this.arregloObjetos = [];
    }

    procesar(archivoEntrada) {
        console.log(`Analizando el archivo '${archivoEntrada}'...`);
        
        if (!fs.existsSync(archivoEntrada)) {
            console.log(`Error: No existe el archivo '${archivoEntrada}'.`);
            return;
        }

        try {
            const contenido = fs.readFileSync(archivoEntrada, 'utf8');
            const lineas = contenido.split('\n');
            
            const matrizInterna = [];
            const valores = [];
            
            for (let linea of lineas) {
                linea = linea.trim();
                // Verificamos si es un número válido (incluso negativo)
                if (linea && !isNaN(linea)) {
                    const numero = parseInt(linea, 10);
                    valores.push(numero);
                    
                    // Construyo una fila de la matriz: [numero, booleano]
                    const fila = [numero, numero % 2 === 0];
                    matrizInterna.push(fila);
                }
            }
            
            if (valores.length === 0) {
                console.log("El archivo está vacío o sin números válidos.");
                return;
            }

            // Construyo el Struct (JSON) de estadísticas
            const minimo = Math.min(...valores);
            const maximo = Math.max(...valores);
            const promedio = valores.reduce((a, b) => a + b, 0) / valores.length;
            
            const stats = crearEstadisticas(minimo, maximo, promedio);
            
            // Instancio el Objeto final (que contiene la matriz y el struct)
            const objetoArchivo = new ArchivoAnalizado(
                archivoEntrada,
                matrizInterna,
                stats
            );
            
            // Guardo el objeto en mi arreglo general
            this.arregloObjetos.push(objetoArchivo);
            
            // Muestro los datos usando el método del objeto
            objetoArchivo.mostrarResumen();

        } catch (error) {
            console.log(`Error procesando archivo: ${error.message}`);
        }
    }
}

function ejecutarAnalizador() {
    // Creo un archivo de prueba para sustentar el programa
    const rutaPrueba = "numeros_matriz_js.txt";
    if (!fs.existsSync(rutaPrueba)) {
        fs.writeFileSync(rutaPrueba, "45\n12\n-5\n89\n100\n73\n2\n24\n99\n1\n");
    }
            
    const analizador = new AnalizadorArchivos();
    analizador.procesar(rutaPrueba);
}

// Exportamos la función para poder usarla desde un menú principal si es necesario
module.exports = { ejecutarAnalizador };

// Si ejecutamos directamente el script, llamamos a la función
if (require.main === module) {
    ejecutarAnalizador();
}
