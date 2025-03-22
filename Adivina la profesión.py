profesionOriginal = "ingeniero"
while True:
    profesionAdivinada = str(input("Adivina la profesión:")).lower()
    print("La profesión ingresada ha sido:",profesionAdivinada)
    if profesionOriginal == profesionAdivinada:
        print("La profesión original es:",profesionOriginal)
        print("Correcto! Adivinaste la profesión")
        break
    else:
        print("Intentalo de neuvo")
