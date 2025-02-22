Documentación del Sistema de Carrito de Compras - Mercado Inteligente
Introducción
El proyecto Mercado Inteligente es un sistema de carrito de compras desarrollado en Python utilizando la biblioteca Tkinter para la interfaz gráfica de usuario. Este sistema permite a los usuarios gestionar productos en un carrito, aplicar descuentos, y generar tickets de compra en formato PDF.

Requisitos
Python 3.x
Bibliotecas:
tkinter
ttk
messagebox
datetime
os
glob
fpdf
Estructura del Código
El código se organiza en una clase principal llamada MercadoInteligenteGUI, que contiene todos los métodos y atributos necesarios para la funcionalidad de la aplicación. A continuación, se describen los componentes principales.

Clase MercadoInteligenteGUI
Atributos
root: Ventana principal de la aplicación.
carrito: Lista que almacena los productos añadidos al carrito.
presupuesto_limite: Presupuesto máximo permitido (por defecto, $1000.00).
umbral_descuento: Cantidad mínima de productos para aplicar descuentos (por defecto, 5).
Métodos
__init__(self, root)

Inicializa la ventana y configura la interfaz gráfica.
configurar_estilos(self)

Configura los estilos visuales de la aplicación utilizando ttk.Style.
crear_interfaz(self)

Crea los componentes principales de la interfaz, incluyendo botones y tablas.
crear_tabla_carrito(self, parent)

Crea una tabla que muestra los productos en el carrito.
agregar_producto(self)

Abre un diálogo para agregar un nuevo producto al carrito.
procesar_nuevo_producto(self, nombre, cantidad_str, precio_str, dialog)

Valida y procesa los datos de un nuevo producto.
calcular_descuento(self, cantidad, precio_unitario)

Calcula el descuento basado en la cantidad de productos.
actualizar_tabla_carrito(self)

Actualiza la tabla con los productos actuales en el carrito.
actualizar_totales(self)

Actualiza las etiquetas de totales mostrando subtotal, descuento y total a pagar.
verificar_presupuesto(self)

Verifica si el total supera el presupuesto límite.
eliminar_producto(self)

Elimina el producto seleccionado del carrito.
modificar_producto(self)

Modifica el producto seleccionado.
finalizar_compra(self)

Finaliza la compra y muestra el ticket.
guardar_ticket(self, ticket_window)

Guarda el ticket en un archivo PDF.
mostrar_historial(self)

Muestra una ventana con el historial de facturas.
finalizar_proceso_compra(self, ticket_window)

Finaliza el proceso de compra y limpia el carrito.
Función Principal
Copiar
def iniciar_aplicacion():
    root = tk.Tk()
    app = MercadoInteligenteGUI(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
Conclusión
El sistema Mercado Inteligente proporciona una interfaz amigable para gestionar compras, aplicar descuentos y generar tickets. Este proyecto puede ampliarse con más funcionalidades, como la integración de bases de datos o la implementación de un sistema de autenticación para los usuarios.
