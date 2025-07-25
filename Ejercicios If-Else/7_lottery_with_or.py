"""Elegibilidad para sorteo.
Pregunta si el usuario participó en la actividad o realizó una compra mayor a $200.000.
Si alguna condición es verdadera, muestra “Participas en el sorteo”. Si no, “No participas”."""

while True:
    try:
        participation = int(input("¿Participaste en la actividad?\nPor favor digita 1 = Si ó 2 = No: "))
        if (participation == 1 or participation == 2):
            while True:
                try:
                    buy = float(input("¿Cuál fue el valor de tu compra? "))
                    if (participation == 1 or buy > 200.000):
                        print("Participas en el sorteo")
                        break
                    else:
                        print("No participas")
                        break
                except ValueError:
                    print("Valor de compra incorrecto.\nIntenta de nuevo")
            break
        else:
            print("Opción incorrecta\nIntenta de nuevo")
    except ValueError:
        print("Respuesta incorrecta.\nIntenta de nuevo")