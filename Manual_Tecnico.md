# Manual Técnico: Aplicación de Análisis Léxico y Operaciones Matemáticas

### Universidad San Carlos de Guatemala
Escuela de Ciencias y Sistemas 

Segundo Semestre 2023

Lenguajes Formales y de Programación

## Descripción del Proyecto
Este proyecto consiste en una aplicación que realiza análisis léxico de un lenguaje de programación personalizado y ejecuta operaciones matemáticas. 


## Objetivos
* Objetivo General
    * Desarrollar un sistema de análisis léxico para reconocer un lenguaje dado, gestionar archivos y generar informes de análisis léxico.

* Objetivos Específicos
    * Analizador Léxico: Implementar un analizador léxico basado en estados para reconocer tokens y palabras reservadas en el código fuente.
    * Gestión de Archivos: Crear funciones para abrir, guardar y guardar como archivos con formato JSON.
    * Generación de Informes: Generar informes de análisis léxico que incluyan detalles sobre tokens y errores, y guardarlos en un archivo JSON.
    * Interfaz Gráfica: Diseñar una interfaz gráfica de usuario utilizando la biblioteca Tkinter para cargar y analizar código fuente.
    * Graficación de Árboles: Utilizar la biblioteca Graphviz para generar y mostrar diagramas de árbol de las operaciones analizadas.
   


---
## Implementación

### Clase Expression
- Clase abstracta que sirve como base para las clases Palabra, Operaciones y Operaciones_un_valor.
- Define una función abstracta `funcionToken()` que debe implementarse en las clases derivadas.

### Clase Palabra
- Representa una palabra o token en el código fuente.
- Almacena la palabra, la fila y la columna donde se encuentra.

### Clase Operaciones
- Representa una operación que involucra dos valores (valor1 y valor2) y un tipo de operación (suma, resta, etc.).
- Implementa la función `funcionToken()` para realizar la operación correspondiente.

### Clase Operaciones_un_valor
- Representa una operación que involucra un solo valor (valor1) y un tipo de operación (seno, coseno, etc.).
- Implementa la función `funcionToken()` para realizar la operación correspondiente.

### Función analizador()
- Analiza el código fuente proporcionado y extrae las palabras y operaciones relevantes.
- Identifica errores léxicos y los almacena en la lista `lista_errores`.

### Función crear_palabra()
- Utilizada en el análisis léxico para crear palabras a partir de caracteres en el código fuente.

### Función crear_numero()
- Utilizada para crear números a partir de caracteres en el código fuente.

### Función operar()
- Implementa un analizador sintáctico para reconocer y realizar operaciones de acuerdo con la jerarquía de operaciones.
- Crea objetos Operaciones o Operaciones_un_valor y los almacena en la lista `operaciones_resultantes`.

### Función funcionan()
- Llama a `operar()` repetidamente hasta que se hayan procesado todas las operaciones.
- Muestra los resultados en el widget `textae`.

### Función graficar_operaciones()
- Utiliza la biblioteca Graphviz para generar un diagrama de árbol de las operaciones analizadas y lo guarda en un archivo.

## Funciones relacionadas con la interfaz gráfica

### boton_analiza()
- Llama a `analizador()` y `funcionan()` para analizar el código fuente y mostrar los resultados.

### boton_error()
- Crea un archivo JSON que contiene los errores léxicos detectados y los muestra en el widget `textae`.

### boton_report()
- Llama a `graficar_operaciones()` para generar y mostrar el diagrama de árbol de las operaciones.

## Funciones relacionadas con la gestión de archivos y la interfaz de usuario

### Manejo de Archivos
- El formato del archivo de código fuente es JSON.
- El formato del archivo de errores es JSON.
- Se utilizan funciones para abrir, guardar y guardar como archivos con extensiones .json.

## Ejemplo de Uso
- Al ejecutar la aplicacion se mostrara una vista amigable que funciona por medio de botones hay 7 botones de los cuales su funcion se explica arriba, la aplicacion mostrara el archivo abierto en el text de arriba y en el de abajo mostrara los resultados del analisis como el archivo de errores.

## AFD 
- A continuacion una imagen del AFD Y la Gramatica
  ![Automata](https://github.com/Serrano18/LFP_S2_2023_Proyecto1_202201989/blob/main/Automata.jpeg)
---
