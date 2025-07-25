import tkinter as tk
from tkinter import messagebox

# Precios
valor_perro_caliente, valor_pizza, valor_hamburguesa, valor_papa_frita, valor_gaseosa = 7000, 10000, 15000, 5000, 2000

# Inicializar cantidades
cantidades = {
    "Perro Caliente": 0,
    "Pizza": 0,
    "Hamburguesa": 0,
    "Papas Fritas": 0,
    "Gaseosa": 0
}

precios = {
    "Perro Caliente": valor_perro_caliente,
    "Pizza": valor_pizza,
    "Hamburguesa": valor_hamburguesa,
    "Papas Fritas": valor_papa_frita,
    "Gaseosa": valor_gaseosa
}

# Crear ventana
ventana = tk.Tk()
ventana.title("Restaurante Virtual")
ventana.geometry("400x500")
ventana.config(bg="#f0f0f0")

titulo = tk.Label(ventana, text="Menú del Restaurante", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
titulo.pack(pady=10)

# Diccionario para almacenar entradas de cantidad
entradas = {}

# Función para agregar cantidad ingresada
def agregar_producto(producto):
    try:
        cantidad = int(entradas[producto].get())
        if cantidad < 0:
            raise ValueError
        cantidades[producto] += cantidad
        messagebox.showinfo("Producto agregado", f"Se agregaron {cantidad} {producto}(s) al carrito.")
        entradas[producto].delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número entero positivo.")

# Mostrar productos con entradas y botones
for producto, precio in precios.items():
    frame = tk.Frame(ventana, bg="#f0f0f0")
    frame.pack(pady=5)
    
    etiqueta = tk.Label(frame, text=f"{producto} - ${precio}", font=("Helvetica", 12), bg="#f0f0f0")
    etiqueta.pack(side="left", padx=5)

    entrada = tk.Entry(frame, width=5)
    entrada.pack(side="left", padx=5)
    entradas[producto] = entrada

    boton_agregar = tk.Button(frame, text="Agregar", bg="#4CAF50", fg="white", command=lambda p=producto: agregar_producto(p))
    boton_agregar.pack(side="left", padx=5)

# Función para mostrar factura
def mostrar_factura():
    detalles = ""
    total = 0

    for producto, cantidad in cantidades.items():
        if cantidad > 0:
            subtotal = cantidad * precios[producto]
            total += subtotal
            detalles += f"{cantidad} {producto}(s) = ${subtotal}\n"

    if detalles == "":
        detalles = "No has agregado productos al carrito."
    else:
        detalles += f"\nTotal a pagar: ${total}"

    messagebox.showinfo("Factura", detalles)

# Botón confirmar
boton_confirmar = tk.Button(ventana, text="Confirmar Pedido", font=("Helvetica", 14), bg="#2196F3", fg="white", command=mostrar_factura)
boton_confirmar.pack(pady=20)

ventana.mainloop()
