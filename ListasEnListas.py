print("La lista que usted deberá llenar se compone de la siguiente manera:") #Información
print("[Nombre],[Edad],[Peso(Kg)]:\nAhora ingresa tus datos:")
pregunta = 0
def preguntar ():
        #while pregunta == 0:
            while True:
                try:
                    pregunta=(int(input("¿Desea agregar más personas a la base de datos? Digite: 1 = SI, 0 = N0: ")))
                    if pregunta == 0 or pregunta == 1:
                        if pregunta == 1:
                            agregar()
                            break
                        elif pregunta == 0:
                            salir ()
                except ValueError:
                    print("Por favor ingrese un valor válido: ")
                def agregar ():
                    while True:
                        try:
                            nombre = str(input("Ingrese el nombre: "))
                            break
                        except ValueError:
                            print("**Error** Debe ingresar el nombre en letras.")
                    while True:
                        try:
                            edad = int(input("Ingrese la edad: "))
                            break
                        except ValueError:
                            print("**Error** Debe ser un valor numérico.")
                    while True:
                        try:
                            peso = int(input("Ingrese su peso: "))
                            break
                        except ValueError:
                            print("**Error** Debe ser un valor numérico.")
                        persona=[nombre,edad,peso]
                        print("Persona agregada:\n",persona)

            def salir ():
                print("Usted ha cerrado el programa...")
                pregunta = 2
                salir()
preguntar()

