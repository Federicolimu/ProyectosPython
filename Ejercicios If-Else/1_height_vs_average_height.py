"""Comparar altura con la estatura promedio.
Solicita la estatura. Si es mayor o igual a 1.70 m, muestra “Estás por encima o igual al promedio”.
Si no, muestra “Estás por debajo del promedio”."""

while True:
    try :
        height = float(input("Por favor ingrese su altura en metros (Eje: 1.70)\n"))
        break
    except ValueError:
        print("Por favor ingrese una estatura válida: ")

if (height >= 1.70):
    print("Estás por encima o igual al promedio")
else:
    print("Estás por debajo del promedio")