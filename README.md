# Inventory Manager in Python

Este proyecto es un gestor de inventario simple desarrollado en Python. Ideal para negocios pequeños o como práctica de programación, permite agregar, consultar, actualizar, eliminar productos y calcular el valor total del inventario. Los productos se identifican mediante un ID único que se reasigna automáticamente si un producto es eliminado.

## Funcionalidades

- Añadir productos con nombre, precio y cantidad.
- Consultar productos por nombre.
- Actualizar el precio de un producto.
- Eliminar productos y reorganizar los IDs.
- Calcular el valor total del inventario usando funciones lambda.
- Mostrar todos los productos disponibles.
- Validación de datos para evitar errores de ingreso.

## Tecnologías usadas

- Python 3
- Diccionarios
- Funciones
- Funciones lambda
- Manejo de errores (try-except)
- Entrada de datos en consola

## Estructura del código

- `inventario`: diccionario donde se almacenan los productos.
- `id_actual`: contador que asigna un ID único a cada nuevo producto.
- Funciones para cada operación (añadir, consultar, eliminar, actualizar).
- Menú interactivo para navegar por el sistema.

## Vista en consola

------ MENÚ DE INVENTARIO ------

1. Añadir producto

2. Consultar producto

3. Actualizar precio

4. Eliminar producto

5. Calcular valor total

6. Mostrar todos los productos

7. Salir

## Cómo usarlo

1. Ejecuta el archivo `.py` en una terminal con Python 3 instalado.
2. Sigue el menú y escribe las opciones según lo que desees hacer.
3. Los datos se almacenan en memoria mientras el programa está corriendo.

## Autor

Dylan Andrés Marín Campo  
Desarrollador en formación, con interés en automatización y desarrollo de soluciones tecnológicas.
