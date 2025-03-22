numero = 1
while (numero != 100):
    if (numero >= 1 and numero <= 100):
        numero = int(input("Por favor ingrese un número del 1 al 100: "))
        print(numero)
    else:
        print("***¡Por favor ingrese un número entre el rango permitido!***")
        numero = 1
print("Usted ingresó el número 100. Acaba de cerrar el cliclo While")
