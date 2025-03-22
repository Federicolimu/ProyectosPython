    #CALCULADORA CON TRY EXCEPT
operacion = 0
while operacion != 5: # while inicia en 0 y por lo que es diferente de 5 se ejecuta
    try:
        operacion = int(input("Menú...\nIngrese: 1 para sumar, 2 para restar,"
                            "3 para multiplicar, 4 para dividir, 5 para salir \n¿Qué operación desea realizar? "))
        print("Usted ingresó ",operacion)

        if operacion > 0 and operacion < 6:
            if (operacion == 5):
                print("Saliendo de la calculadora...")
            else:
                try:
                    x = int(input("Ingrese el valor del primer número: "))
                    try:
                        y = int(input("Ingrese el valor del segundo número: "))
                        print("Los valores que usted ingresó son: ",x,"y",y)
                        if (operacion == 1):
                            print("***USTED SELECCIONÓ LA OPCIÓN DE SUMA***")
                            Suma = (x + y)
                            print("El resultado de la suma es:",Suma)
                        elif (operacion == 2):
                            print("***USTED SELECCIONÓ LA OPCIÓN DE RESTA***")
                            Resta = (x - y)
                            print("El resultado de la resta es:",Resta)
                        elif (operacion == 3):
                            print("***USTED SELECCIONÓ LA OPCIÓN DE MULTIPLICACIÓN***")
                            Multiplicacion = (x * y)
                            print("El resultado de la multiplicación es:",Multiplicacion)
                        elif (operacion == 4):
                            print("***USTED SELECCIONÓ LA OPCIÓN DEDIVISIÓN***")
                            Division = x / y
                            print("El resultado de la división es:",Division)
                        else:
                            print("*ERROR* Seleccionó una opción Incorrecta.")
                            print("Por favor intentelo de nuevo.")
                    except ValueError:
                        print("Por favor digite un número válido")
                except ValueError:
                    print("Por favor digite un número válido")
        else:
            print("*ERROR* Seleccionó una opción Incorrecta.")
            print("Por favor intentelo de nuevo.")
    except ValueError:
        print("*ERROR* Seleccionó una opción Incorrecta.")
        print("Por favor intentelo de nuevo.")
