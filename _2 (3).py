import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import datetime
from tkinter.font import Font
import os

class MercadoInteligenteGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mercado Inteligente - Sistema de Carrito de Compras")
        self.root.geometry("900x600")
        self.root.configure(bg="#f0f0f0")
        
        # Variables de la aplicación
        self.carrito = []
        self.presupuesto_limite = 1000.0
        self.umbral_descuento = 5
        
        # Configuración de estilos
        self.configurar_estilos()
        
        # Crear interfaz principal
        self.crear_interfaz()
        
    def configurar_estilos(self):
        """Configura los estilos visuales de la aplicación"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Estilos para botones
        self.style.configure('TButton', font=('Arial', 10), background='#4CAF50', foreground='black')
        self.style.map('TButton', background=[('active', '#45a049')])
        
        # Estilos para etiquetas
        self.style.configure('TLabel', font=('Arial', 11), background='#f0f0f0')
        self.style.configure('Header.TLabel', font=('Arial', 14, 'bold'), background='#f0f0f0')
        
        # Estilos para tablas
        self.style.configure('Treeview', 
                            background='#f9f9f9', 
                            foreground='black', 
                            fieldbackground='#f9f9f9')
        self.style.map('Treeview', background=[('selected', '#4CAF50')])
        self.style.configure('Treeview.Heading', font=('Arial', 10, 'bold'))
        
    def crear_interfaz(self):
        """Crea los componentes principales de la interfaz"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título de la aplicación
        header_label = ttk.Label(main_frame, text="MERCADO INTELIGENTE", style='Header.TLabel')
        header_label.pack(pady=(0, 20))
        
        # Frame para botones de acción
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        # Botones de acción
        add_btn = ttk.Button(button_frame, text="Agregar Producto", command=self.agregar_producto)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        remove_btn = ttk.Button(button_frame, text="Eliminar Producto", command=self.eliminar_producto)
        remove_btn.pack(side=tk.LEFT, padx=5)
        
        edit_btn = ttk.Button(button_frame, text="Modificar Producto", command=self.modificar_producto)
        edit_btn.pack(side=tk.LEFT, padx=5)
        
        checkout_btn = ttk.Button(button_frame, text="Finalizar Compra", command=self.finalizar_compra)
        checkout_btn.pack(side=tk.RIGHT, padx=5)
        
        # Tabla de productos en el carrito
        self.crear_tabla_carrito(main_frame)
        
        # Frame para información de totales
        totals_frame = ttk.Frame(main_frame, padding="5")
        totals_frame.pack(fill=tk.X, pady=10)
        
        # Etiquetas para mostrar totales
        self.label_subtotal = ttk.Label(totals_frame, text="Subtotal: $0.00")
        self.label_subtotal.pack(side=tk.LEFT, padx=10)
        
        self.label_descuento = ttk.Label(totals_frame, text="Descuento: $0.00")
        self.label_descuento.pack(side=tk.LEFT, padx=10)
        
        self.label_total = ttk.Label(totals_frame, text="Total: $0.00", font=('Arial', 12, 'bold'))
        self.label_total.pack(side=tk.RIGHT, padx=10)
    
    def crear_tabla_carrito(self, parent):
        """Crea la tabla que muestra los productos en el carrito"""
        # Frame para la tabla
        table_frame = ttk.Frame(parent)
        table_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Scrollbar para la tabla
        scrollbar = ttk.Scrollbar(table_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Crear tabla (Treeview)
        columns = ('id', 'nombre', 'cantidad', 'precio', 'subtotal', 'descuento', 'total')
        self.tabla_carrito = ttk.Treeview(table_frame, columns=columns, show='headings', yscrollcommand=scrollbar.set)
        
        # Configurar columnas
        self.tabla_carrito.heading('id', text='#')
        self.tabla_carrito.heading('nombre', text='Producto')
        self.tabla_carrito.heading('cantidad', text='Cantidad')
        self.tabla_carrito.heading('precio', text='Precio Unit.')
        self.tabla_carrito.heading('subtotal', text='Subtotal')
        self.tabla_carrito.heading('descuento', text='Descuento')
        self.tabla_carrito.heading('total', text='Total')
        
        # Ajustar ancho de columnas
        self.tabla_carrito.column('id', width=40, anchor=tk.CENTER)
        self.tabla_carrito.column('nombre', width=200)
        self.tabla_carrito.column('cantidad', width=80, anchor=tk.CENTER)
        self.tabla_carrito.column('precio', width=100, anchor=tk.E)
        self.tabla_carrito.column('subtotal', width=100, anchor=tk.E)
        self.tabla_carrito.column('descuento', width=100, anchor=tk.E)
        self.tabla_carrito.column('total', width=100, anchor=tk.E)
        
        # Empaquetar tabla
        self.tabla_carrito.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Configurar scrollbar
        scrollbar.config(command=self.tabla_carrito.yview)
    
    def agregar_producto(self):
        """Abre una ventana para agregar un nuevo producto al carrito"""
        # Crear ventana de diálogo
        dialog = tk.Toplevel(self.root)
        dialog.title("Agregar Producto")
        dialog.geometry("400x300")
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.configure(bg="#f0f0f0")
        
        # Frame para formulario
        form_frame = ttk.Frame(dialog, padding=20)
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        # Campos de entrada
        ttk.Label(form_frame, text="Nombre del Producto:").grid(row=0, column=0, sticky=tk.W, pady=5)
        nombre_entry = ttk.Entry(form_frame, width=30)
        nombre_entry.grid(row=0, column=1, pady=5)
        nombre_entry.focus()
        
        ttk.Label(form_frame, text="Cantidad:").grid(row=1, column=0, sticky=tk.W, pady=5)
        cantidad_entry = ttk.Entry(form_frame, width=30)
        cantidad_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(form_frame, text="Precio Unitario ($):").grid(row=2, column=0, sticky=tk.W, pady=5)
        precio_entry = ttk.Entry(form_frame, width=30)
        precio_entry.grid(row=2, column=1, pady=5)
        
        # Mensaje de descuentos
        mensaje_descuento = ttk.Label(form_frame, 
                                     text=f"* Descuentos: 5% (≥{self.umbral_descuento} und.), 10% (≥10 und.), 15% (≥20 und.)",
                                     font=("Arial", 9))
        mensaje_descuento.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=(20, 5))
        
        # Botones
        btn_frame = ttk.Frame(form_frame)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=20)
        
        ttk.Button(btn_frame, text="Cancelar", 
                  command=dialog.destroy).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(btn_frame, text="Agregar al Carrito", 
                  command=lambda: self.procesar_nuevo_producto(
                      nombre_entry.get(),
                      cantidad_entry.get(),
                      precio_entry.get(),
                      dialog)).pack(side=tk.LEFT, padx=5)
    
    def procesar_nuevo_producto(self, nombre, cantidad_str, precio_str, dialog):
        """Procesa y valida los datos de un nuevo producto"""
        # Validar nombre
        if not nombre.strip():
            messagebox.showerror("Error", "El nombre del producto no puede estar vacío")
            return
        
        # Validar cantidad
        try:
            cantidad = int(cantidad_str)
            if cantidad <= 0:
                messagebox.showerror("Error", "La cantidad debe ser un número positivo")
                return
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero válido")
            return
        
        # Validar precio
        try:
            precio = float(precio_str)
            if precio <= 0:
                messagebox.showerror("Error", "El precio debe ser un número positivo")
                return
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número válido")
            return
        
        # Calcular valores
        subtotal = cantidad * precio
        descuento = self.calcular_descuento(cantidad, precio)
        total = subtotal - descuento
        
        # Agregar al carrito
        producto = {
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio,
            'subtotal': subtotal,
            'descuento': descuento,
            'total': total
        }
        self.carrito.append(producto)
        
        # Actualizar tabla
        self.actualizar_tabla_carrito()
        
        # Cerrar diálogo
        dialog.destroy()
        
        # Verificar presupuesto
        self.verificar_presupuesto()
        
    def calcular_descuento(self, cantidad, precio_unitario):
        """Calcula el descuento basado en la cantidad de productos"""
        subtotal = cantidad * precio_unitario
        
        # Aplicación de descuentos por volumen
        if cantidad >= self.umbral_descuento and cantidad < 10:
            return subtotal * 0.05  # 5% de descuento
        elif cantidad >= 10 and cantidad < 20:
            return subtotal * 0.10  # 10% de descuento
        elif cantidad >= 20:
            return subtotal * 0.15  # 15% de descuento
        return 0.0
    
    def actualizar_tabla_carrito(self):
        """Actualiza la tabla con los productos actuales en el carrito"""
        # Limpiar tabla
        for item in self.tabla_carrito.get_children():
            self.tabla_carrito.delete(item)
        
        # Agregar productos
        for i, producto in enumerate(self.carrito, 1):
            self.tabla_carrito.insert('', 'end', values=(
                i,
                producto['nombre'],
                producto['cantidad'],
                f"${producto['precio']:.2f}",
                f"${producto['subtotal']:.2f}",
                f"${producto['descuento']:.2f}",
                f"${producto['total']:.2f}"
            ))
        
        # Actualizar totales
        self.actualizar_totales()
    
    def actualizar_totales(self):
        """Actualiza las etiquetas de totales"""
        total_subtotal = sum(item['subtotal'] for item in self.carrito)
        total_descuento = sum(item['descuento'] for item in self.carrito)
        total_pagar = sum(item['total'] for item in self.carrito)
        
        self.label_subtotal.config(text=f"Subtotal: ${total_subtotal:.2f}")
        self.label_descuento.config(text=f"Descuento: ${total_descuento:.2f}")
        self.label_total.config(text=f"Total: ${total_pagar:.2f}")
    
    def verificar_presupuesto(self):
        """Verifica si el total supera el presupuesto límite"""
        total_pagar = sum(item['total'] for item in self.carrito)
        
        if total_pagar > self.presupuesto_limite:
            messagebox.showwarning(
                "Alerta de Presupuesto",
                f"El total de su compra (${total_pagar:.2f}) supera el presupuesto límite de ${self.presupuesto_limite:.2f}"
            )
    
    def eliminar_producto(self):
        """Elimina el producto seleccionado del carrito"""
        seleccion = self.tabla_carrito.selection()
        if not seleccion:
            messagebox.showinfo("Información", "Seleccione un producto para eliminar")
            return
        
        # Obtener índice del producto seleccionado
        indice = int(self.tabla_carrito.item(seleccion[0])['values'][0]) - 1
        
        # Confirmar eliminación
        producto = self.carrito[indice]
        confirmar = messagebox.askyesno(
            "Confirmar Eliminación",
            f"¿Está seguro de eliminar '{producto['nombre']}' del carrito?"
        )
        
        if confirmar:
            # Eliminar del carrito
            self.carrito.pop(indice)
            # Actualizar tabla
            self.actualizar_tabla_carrito()
            
    
    def modificar_producto(self):
        """Modifica el producto seleccionado"""
        seleccion = self.tabla_carrito.selection()
        if not seleccion:
            messagebox.showinfo("Información", "Seleccione un producto para modificar")
            return
        
        # Obtener índice del producto seleccionado
        indice = int(self.tabla_carrito.item(seleccion[0])['values'][0]) - 1
        producto = self.carrito[indice]
        
        # Crear ventana de diálogo
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Modificar Producto: {producto['nombre']}")
        dialog.geometry("400x200")
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.configure(bg="#f0f0f0")
        
        # Frame para formulario
        form_frame = ttk.Frame(dialog, padding=20)
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        # Campos de entrada
        ttk.Label(form_frame, text="Cantidad:").grid(row=0, column=0, sticky=tk.W, pady=5)
        cantidad_entry = ttk.Entry(form_frame, width=30)
        cantidad_entry.insert(0, str(producto['cantidad']))
        cantidad_entry.grid(row=0, column=1, pady=5)
        cantidad_entry.select_range(0, tk.END)
        cantidad_entry.focus()
        
        ttk.Label(form_frame, text="Precio Unitario ($):").grid(row=1, column=0, sticky=tk.W, pady=5)
        precio_entry = ttk.Entry(form_frame, width=30)
        precio_entry.insert(0, str(producto['precio']))
        precio_entry.grid(row=1, column=1, pady=5)
        
        # Botones
        btn_frame = ttk.Frame(form_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        ttk.Button(btn_frame, text="Cancelar", 
                  command=dialog.destroy).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(btn_frame, text="Guardar Cambios", 
                  command=lambda: self.guardar_modificacion(
                      indice,
                      cantidad_entry.get(),
                      precio_entry.get(),
                      dialog)).pack(side=tk.LEFT, padx=5)
    
    def guardar_modificacion(self, indice, cantidad_str, precio_str, dialog):
        """Guarda los cambios de un producto modificado"""
        producto = self.carrito[indice]
        
        # Validar cantidad
        try:
            cantidad = int(cantidad_str)
            if cantidad <= 0:
                messagebox.showerror("Error", "La cantidad debe ser un número positivo")
                return
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero válido")
            return
        
        # Validar precio
        try:
            precio = float(precio_str)
            if precio <= 0:
                messagebox.showerror("Error", "El precio debe ser un número positivo")
                return
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número válido")
            return
        
        # Actualizar producto
        producto['cantidad'] = cantidad
        producto['precio'] = precio
        producto['subtotal'] = cantidad * precio
        producto['descuento'] = self.calcular_descuento(cantidad, precio)
        producto['total'] = producto['subtotal'] - producto['descuento']
        
        # Actualizar tabla
        self.actualizar_tabla_carrito()
        
        # Cerrar diálogo
        dialog.destroy()
        
        # Verificar presupuesto
        self.verificar_presupuesto()
        
    
    def finalizar_compra(self):
        """Finaliza la compra y muestra el ticket"""
        if not self.carrito:
            messagebox.showinfo("Información", "El carrito está vacío")
            return
        
        # Crear ventana para el ticket
        ticket_window = tk.Toplevel(self.root)
        ticket_window.title("Ticket de Compra")
        ticket_window.geometry("500x600")
        ticket_window.configure(bg="white")
        
        # Frame para el ticket
        ticket_frame = tk.Frame(ticket_window, bg="white", padx=20, pady=20)
        ticket_frame.pack(fill=tk.BOTH, expand=True)
        
        # Fecha y título
        fecha_actual = datetime.datetime.now()
        
        tk.Label(ticket_frame, text="MERCADO INTELIGENTE", 
                font=("Arial", 16, "bold"), bg="white").pack(pady=(0, 5))
        
        tk.Label(ticket_frame, text="TICKET DE COMPRA", 
                font=("Arial", 14), bg="white").pack(pady=(0, 10))
        
        tk.Label(ticket_frame, 
                text=f"Fecha: {fecha_actual.strftime('%d/%m/%Y')} - Hora: {fecha_actual.strftime('%H:%M:%S')}", 
                font=("Arial", 10), bg="white").pack(pady=(0, 20))
        
        # Canvas para detalles
        canvas_frame = tk.Frame(ticket_frame, bg="white")
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        canvas = tk.Canvas(canvas_frame, bg="white")
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Encabezados
        header_frame = tk.Frame(scrollable_frame, bg="white")
        header_frame.pack(fill=tk.X, pady=(0, 5))
        
        tk.Label(header_frame, text="Cant.", width=6, anchor="w", 
                font=("Arial", 10, "bold"), bg="white").pack(side=tk.LEFT)
        tk.Label(header_frame, text="Producto", width=20, anchor="w", 
                font=("Arial", 10, "bold"), bg="white").pack(side=tk.LEFT)
        tk.Label(header_frame, text="Precio", width=10, anchor="e", 
                font=("Arial", 10, "bold"), bg="white").pack(side=tk.LEFT)
        tk.Label(header_frame, text="Subtotal", width=10, anchor="e", 
                font=("Arial", 10, "bold"), bg="white").pack(side=tk.LEFT)
        
        # Línea divisoria
        tk.Frame(scrollable_frame, height=1, bg="black").pack(fill=tk.X, pady=(0, 5))
        
        # Productos
        for producto in self.carrito:
            item_frame = tk.Frame(scrollable_frame, bg="white")
            item_frame.pack(fill=tk.X, pady=2)
            
            tk.Label(item_frame, text=str(producto['cantidad']), width=6, anchor="w", 
                    font=("Arial", 10), bg="white").pack(side=tk.LEFT)
            tk.Label(item_frame, text=producto['nombre'], width=20, anchor="w", 
                    font=("Arial", 10), bg="white").pack(side=tk.LEFT)
            tk.Label(item_frame, text=f"${producto['precio']:.2f}", width=10, anchor="e", 
                    font=("Arial", 10), bg="white").pack(side=tk.LEFT)
            tk.Label(item_frame, text=f"${producto['subtotal']:.2f}", width=10, anchor="e", 
                    font=("Arial", 10), bg="white").pack(side=tk.LEFT)
        
        # Línea divisoria
        tk.Frame(scrollable_frame, height=1, bg="black").pack(fill=tk.X, pady=10)
        
        # Totales
        total_productos = sum(item['cantidad'] for item in self.carrito)
        total_subtotal = sum(item['subtotal'] for item in self.carrito)
        total_descuento = sum(item['descuento'] for item in self.carrito)
        total_pagar = sum(item['total'] for item in self.carrito)
        
        totals_frame = tk.Frame(scrollable_frame, bg="white")
        totals_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(totals_frame, text=f"Subtotal ({total_productos} productos):", 
                anchor="e", font=("Arial", 10), bg="white").pack(side=tk.LEFT, expand=True, fill=tk.X)
        tk.Label(totals_frame, text=f"${total_subtotal:.2f}", width=10, 
                anchor="e", font=("Arial", 10), bg="white").pack(side=tk.RIGHT)
        
        discount_frame = tk.Frame(scrollable_frame, bg="white")
        discount_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(discount_frame, text="Descuento aplicado:", 
                anchor="e", font=("Arial", 10), bg="white").pack(side=tk.LEFT, expand=True, fill=tk.X)
        tk.Label(discount_frame, text=f"${total_descuento:.2f}", width=10, 
                anchor="e", font=("Arial", 10), bg="white").pack(side=tk.RIGHT)
        
        final_frame = tk.Frame(scrollable_frame, bg="white")
        final_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(final_frame, text="TOTAL A PAGAR:", 
                anchor="e", font=("Arial", 12, "bold"), bg="white").pack(side=tk.LEFT, expand=True, fill=tk.X)
        tk.Label(final_frame, text=f"${total_pagar:.2f}", width=10, 
                anchor="e", font=("Arial", 12, "bold"), bg="white").pack(side=tk.RIGHT)
        
        # Mensaje final
        tk.Frame(scrollable_frame, height=1, bg="black").pack(fill=tk.X, pady=10)
        tk.Label(scrollable_frame, text="¡Gracias por su compra!", 
                font=("Arial", 12, "bold"), bg="white").pack(pady=10)
        
        # Botones finales
        button_frame = tk.Frame(ticket_window, bg="white", pady=10)
        button_frame.pack(fill=tk.X)
        
        ttk.Button(button_frame, text="Imprimir", 
                  command=lambda: messagebox.showinfo("Imprimir", "Enviando a impresora...")).pack(side=tk.LEFT, padx=10)
        
        ttk.Button(button_frame, text="Guardar Ticket", 
                  command=lambda: self.guardar_ticket(ticket_window)).pack(side=tk.LEFT, padx=10)
        
        ttk.Button(button_frame, text="Finalizar", 
                  command=lambda: self.finalizar_proceso_compra(ticket_window)).pack(side=tk.RIGHT, padx=10)
    
    def guardar_ticket(self, ticket_window):
        """Guarda el ticket en un archivo de texto"""
        # Crear el contenido del ticket
        contenido = "MERCADO INTELIGENTE\n"
        contenido += "TICKET DE COMPRA\n\n"
        contenido += f"Fecha: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
        contenido += "Cant.  Producto              Precio    Subtotal\n"
        contenido += "------------------------------------------------\n"
        
        for producto in self.carrito:
            contenido += f"{producto['cantidad']:<6} {producto['nombre']:<20} ${producto['precio']:>7.2f} ${producto['subtotal']:>8.2f}\n"
        
        contenido += "\n"
        
        # Calcular totales
        total_productos = sum(item['cantidad'] for item in self.carrito)
        total_subtotal = sum(item['subtotal'] for item in self.carrito)
        total_descuento = sum(item['descuento'] for item in self.carrito)
        total_pagar = sum(item['total'] for item in self.carrito)
        
        # Agregar totales al contenido
        contenido += f"Subtotal ({total_productos} productos): ${total_subtotal:.2f}\n"
        contenido += f"Descuento aplicado: ${total_descuento:.2f}\n"
        contenido += f"TOTAL A PAGAR: ${total_pagar:.2f}\n\n"
        contenido += "¡Gracias por su compra!"
        
        # Guardar el contenido en un archivo
        try:
            with open("ticket.txt", "w", encoding="utf-8") as file:
                file.write(contenido)
            messagebox.showinfo("Ticket Guardado", "El ticket se ha guardado correctamente en 'ticket.txt'")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el ticket: {e}")
    
    def finalizar_proceso_compra(self, ticket_window):
        """Finaliza el proceso de compra y limpia el carrito"""
        # Cerrar ventana del ticket
        ticket_window.destroy()
        
        # Limpiar carrito
        self.carrito = []
        self.actualizar_tabla_carrito()
        
        # Mostrar mensaje de éxito
        messagebox.showinfo("Compra Finalizada", "¡Gracias por su compra! Vuelva pronto.")


def iniciar_aplicacion():
    root = tk.Tk()
    app = MercadoInteligenteGUI(root)
    
    def on_closing():
        root.destroy()
        
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()