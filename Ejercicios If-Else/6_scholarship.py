"""Elegibilidad para beca.
Pide el promedio de notas y si el estudiante tiene certificación de voluntariado.
Si ambas condiciones se cumplen, muestra “Aplica a beca”. Si no, “No aplica”."""

while True:
    try:
        average = float(input("¿Cual es el promedio de tus notas? "))
        if (average >= 9.0):
            print("Tienes un buen promedio")
            while True:
                try:
                    certification = int(input("¿Tienes certificación de voluntariado? \nSi es así digita 1 de lo contrario digita 2: "))
                    if (certification == 1):
                        print("Felicitaciones. Aplicas para una beca")
                        break
                    elif (certification == 2):
                        print("Lo siento, debes tener una certificación de voluntariado. No aplicas a una beca")
                        break
                    else:
                        print("Este valor es incorrecto. Intentalo de nuevo")
                except ValueError:
                    print("Respuesta incorrecta. Intenta otra vez")
            break
        elif (average < 9.0):
            print("Lo siento, debes tener un promedio mayor a 9.0 en tus notas. No aplicas a una beca")
            break
        else:
            print("Este valor es incorrecto. Intentalo de nuevo")
    except ValueError:
        print("En este campo solo se pueden ingresar numeros decimales. Intenta otra vez")