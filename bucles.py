contador_arroba = 0
contador_punto = 0
email = input("Ingrese su e-mail: ")
for i in email:
    if (i == "@"):
        contador_arroba += 1
    if (i == "."):
        contador_punto += 1
if contador_arroba == 1 and contador_punto == 1:
    print("Su correo es correcto")
else:
    print ("Su correo es incorrecto")

for i in range (5):
    print(f"Valor de la variable:{i}")