"""Validar si un número tiene dos cifras.
Pide un número entero. Si está entre 10 y 99 (inclusive), muestra “Tiene dos cifras”. Si no, muestra “No tiene dos cifras”."""
while True:
    try:
        number = int(input("Ingrese un número entero: "))
        break
    except ValueError:
        print("El valor ingresado es incorrecto")

if (number > 9 and number < 100):
    print("El número tiene dos cifras")
else:
    print("El número no tiene dos cifras")