"""Verificar si un número es múltiplo de 5.
Solicita un número y verifica si es múltiplo de 5. Muestra el resultado."""

while True:
    try:
        number = int(input("Ingrese un número: "))
        residue = (number % 5)
        if (residue == 0):
            print(f"El número ingresado es múltiplo de 5, porque {number} divido por 5 da como residuo 0")
            print(number / 5)
        else:
            print(f"El número {number} no es múltuplo de 5")
        break
    except ValueError:
        print("Valor no permitido")
