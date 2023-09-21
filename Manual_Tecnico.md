# Manual Técnico: Aplicación de Análisis Léxico y Operaciones Matemáticas

## Descripción del Proyecto
Este proyecto consiste en una aplicación que realiza análisis léxico de un lenguaje de programación personalizado y ejecuta operaciones matemáticas. La aplicación fue desarrollada por María Patricia Serrano Ramírez como parte del curso "Lenguajes Formales y de Programación" en la Universidad San Carlos de Guatemala durante el segundo semestre de 2023.

## Componentes del Proyecto

### 1. Analizador Léxico
El analizador léxico es la parte principal de la aplicación y se encarga de procesar una secuencia de caracteres en formato de lenguaje personalizado. A continuación, se describen sus características clave:

- **Clases de Expresiones**: El analizador léxico utiliza clases de expresiones para representar las diferentes estructuras del lenguaje, como operaciones matemáticas y palabras reservadas.

- **Operaciones Matemáticas**: La aplicación puede realizar operaciones matemáticas como suma, resta, multiplicación, división, potenciación, raíz cuadrada y módulo.

- **Función de Análisis**: La función `funcionToken()` en las clases de expresiones se utiliza para realizar análisis léxico y ejecutar las operaciones matemáticas.

### 2. Clase Producto
La clase Producto representa un artículo del inventario y contiene los siguientes atributos:

- `nombre`: Nombre del producto.
- `cantidad`: Cantidad disponible del producto.
- `precio_unitario`: Precio unitario del producto.
- `ubicacion`: Ubicación física del producto en el inventario.

### 3. Funcionalidades Principales

#### Cargar Inventario Inicial
La función `cargar_inventario(archivo)` se encarga de cargar el inventario inicial desde un archivo de formato .inv. Los productos se almacenan en una lista y se instancia un objeto Producto para cada uno.

#### Cargar Instrucciones de Movimientos
La función `cargar_movimientos(inventario, archivo)` procesa las instrucciones de movimientos desde un archivo de formato .mov. Se pueden agregar stock a un producto existente o vender productos, ajustando las cantidades disponibles en consecuencia.

#### Crear Informe de Inventario
La función `informe(inventario, archivo)` genera un informe de inventario en formato tabular y lo guarda en un archivo de texto .txt. El informe incluye detalles como nombre del producto, cantidad disponible, precio unitario, valor total y ubicación. La información se formatea utilizando la librería tabulate.

#### Menú de Interacción
La función `menu()` muestra un menú interactivo para el usuario, que permite cargar el inventario inicial, cargar movimientos e imprimir informes de inventario y salir del programa.

### 4. Manejo de Archivos
- **Formato de Inventario (.inv)**: Cada línea del archivo contiene los datos de un producto en el formato "crear_producto nombre;cantidad;precio_unitario;ubicacion".

- **Formato de Movimientos (.mov)**: Cada línea del archivo contiene una instrucción de movimiento en el formato "agregar_stock nombre;cantidad;ubicacion" o "vender_producto nombre;cantidad;ubicacion".

- **Formato de Informe (.txt)**: El informe de inventario se guarda en un archivo de texto en formato tabular. La librería tabulate se utiliza para formatear la tabla.

### 5. Ejemplo de Uso
Ejecutando el programa, se mostrará un menú desde el cual se pueden realizar las diferentes operaciones del sistema de inventario, como cargar el inventario inicial, cargar movimientos e imprimir informes.

### 6. Recursos Adicionales
Además del código proporcionado, se recomienda utilizar recursos como:

- **Markdown** para formatear y documentar textos.
- **Librería tabulate** para formatear tablas.

## Conclusiones
Este proyecto es un ejemplo de una aplicación que combina análisis léxico y operaciones matemáticas para gestionar un sistema de inventario. El uso de clases de expresiones facilita el análisis de las estructuras del lenguaje personalizado y la ejecución de operaciones matemáticas. Además, la aplicación proporciona una interfaz de usuario interactiva a través de un menú. Este manual técnico proporciona una descripción detallada de las funcionalidades y componentes clave de la aplicación.
