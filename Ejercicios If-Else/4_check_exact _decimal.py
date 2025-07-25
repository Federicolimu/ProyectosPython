"""Comprobar si un número es decimal exacto.
Pide un número decimal. Si tiene parte decimal distinta de 0, muestra “Es decimal”. Si no, muestra “Es entero”."""

while True:
    try:
        number = float(input("Ingrese un número decimal: "))
        if (number % 1 == 0):
            print("En un entero")
        else:
            print("Es decimal")
        break
    except ValueError:
        print("Numero inválido")
