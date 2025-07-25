"""Descuento por cantidad.
Pide cuántos productos compró. Si son 10 o más, aplica 20% de descuento. Si no, 5%. Muestra total con descuento."""

products = int(input("¿Cuántos productos compraste? "))
if (products >= 10):
    buy = int(input("¿Cuál fue el valor de tu compra? "))
    print("Tienes el 20% de descuento")
    discount = (buy * 20) / 100
    total_value = buy - discount
    print(f"El valor inicial de tu compra es de {buy} menos el 20% que es igual a {discount}.\nEl valor final de tu compra es de {total_value}")
else:
    print("No tienes descuento en tu compra")