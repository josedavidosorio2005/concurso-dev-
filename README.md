Documentación para el Proyecto "Mercado Inteligente"
Descripción del Proyecto
El proyecto "Mercado Inteligente" es una aplicación de escritorio desarrollada en Python utilizando la biblioteca Tkinter. El objetivo de la aplicación es gestionar un sistema de carrito de compras que permita a los usuarios agregar, eliminar y modificar productos, así como calcular totales y aplicar descuentos.

Tabla de Contenidos
Requisitos
Estructura del Proyecto
Características Principales
Uso de la Aplicación
Funciones Clave
Conclusión
Requisitos
Python 3.x
Biblioteca Tkinter (incluida en la instalación estándar de Python)
Conocimientos básicos de programación en Python
Estructura del Proyecto
El archivo principal de la aplicación es _2.py. Este archivo contiene la clase MercadoInteligenteGUI, que gestiona la interfaz gráfica y la lógica del carrito de compras.

Estructura de Clases
MercadoInteligenteGUI: Clase principal que maneja la interfaz y la lógica del carrito.
Métodos:
__init__()
configurar_estilos()
crear_interfaz()
agregar_producto()
eliminar_producto()
modificar_producto()
finalizar_compra()
calcular_descuento()
actualizar_tabla_carrito()
verificar_presupuesto()
guardar_datos()
finalizar_proceso_compra()
Características Principales
Agregar Productos: Permite al usuario añadir productos al carrito con nombre, cantidad y precio.
Eliminar Productos: Opción para eliminar productos seleccionados del carrito.
Modificar Productos: Permite actualizar la cantidad y el precio de un producto en el carrito.
Cálculo de Totales: Calcula automáticamente el subtotal, descuento y total a pagar.
Visualización de Ticket: Genera un ticket de compra al finalizar la compra, mostrando todos los detalles.
Uso de la Aplicación
Iniciar la Aplicación: Ejecutar el archivo _2.py en un entorno Python.
Agregar Productos: Hacer clic en "Agregar Producto" y llenar el formulario.
Modificar Productos: Seleccionar un producto en la tabla y hacer clic en "Modificar Producto".
Eliminar Productos: Seleccionar un producto y hacer clic en "Eliminar Producto".
Finalizar Compra: Hacer clic en "Finalizar Compra" para ver el ticket.
Funciones Clave
agregar_producto()
Abre un diálogo para ingresar los detalles del producto y lo añade al carrito tras validación.

eliminar_producto()
Elimina el producto seleccionado del carrito y actualiza la tabla.

modificar_producto()
Permite modificar la cantidad y el precio de un producto ya existente en el carrito.

calcular_descuento(cantidad, precio_unitario)
Calcula el descuento basado en la cantidad de productos comprados.

actualizar_tabla_carrito()
Actualiza la visualización de la tabla con los productos actuales en el carrito.

verificar_presupuesto()
Verifica si el total de la compra supera el presupuesto límite definido.

Conclusión
El proyecto "Mercado Inteligente" es una aplicación robusta y fácil de usar que permite a los usuarios gestionar su carrito de compras de manera eficiente. Su interfaz gráfica intuitiva y las funcionalidades implementadas hacen que la experiencia de compra sea agradable y organizada.
