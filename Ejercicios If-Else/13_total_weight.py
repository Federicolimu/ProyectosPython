"""Peso ideal (IMC).
Solicita peso y estatura. Calcula el IMC (peso / estatura**2). Si es mayor a 25, muestra “Sobrepeso”. Si no, “Peso adecuado”."""

weight = float(input("Ingresa tu peso (Kg): "))
height = float(input("Ingresa tu altura (m): "))
#height_2 = height * height
#total_weight = weight/ height_2
total = weight / (height * height)
#print("El peso",weight,"dividido en la altura cuadrada",(round(height_2)),"es igual",(round(total,3)))
if (total > 25.0):
    print("Tienes sobrepeso")
else:
    print("No estás en sobrepeso")