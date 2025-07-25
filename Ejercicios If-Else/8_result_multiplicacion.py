"""Multiplicación y verificación.
Pide dos números. Si su producto es mayor que 100, muestra “Resultado alto”. Si no, “Resultado bajo”."""
while True:
    try:
        number_1 = int(input("Ingresa un número: "))
        while True:
            try:
                number_2 = int(input("Ingresa otro número: "))
                result = (number_1 * number_2)
                print(f"{number_1} * {number_2} = {result}")
                if (result > 100):
                    print("Resultado alto")
                    break
                else:
                    print("Resultado bajo")
                    break
            except ValueError:
                print("Solo puedes ingresar número enteros.\nPor favor inténtalo de nuevo. ")
        break
    except ValueError:
        print("Solo puedes ingresar número enteros.\nPor favor inténtalo de nuevo. ")