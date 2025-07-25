"""Promoción doble en tienda.
Pide si el usuario tiene tarjeta y si su compra es mayor a 100.000. Si ambas condiciones se cumplen, aplica promoción."""

card = input("¿Tienes tarjeta de la tienda?\nEscribe si ó no: ")
buy = float(input("Ingresa el valor de la compra: "))

if (card == "si" and buy > 100.000):
    print("Aplicas a la promición")
else:
    print("No aplicas a la promición")