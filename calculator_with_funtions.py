option = 5
while option != 0:
    option = int(input("\nSeleccione la operación que desea realizar:\n 1. Sumar\n 2. Restar\n 3. Multiplicar\n 4. Dividir\n 0. Salir\n\n"))

    if option >= 5:
        print("*** Opción incorrecta ***")
        continue
    
    if option == 0:
        print("Saliendo...")
        
    else:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo numero: "))

        if option == 1:
            print("Elegiste sumar")
            def addition(num1, num2):
                return num1 + num2
            print(addition(num1, num2))

        elif option == 2:
            print("Elegiste restar")
            def subtraction(num1, num2):
                return num1 - num2         
            print(subtraction(num1, num2))

        elif option == 3:
            print("Elegiste multiplicar")
            def multiplication(num1, num2):
                return num1 * num2
            print(multiplication(num1, num2))

        elif option == 4:
            print("Elegiste dividir")
            def division(num1, num2):
                return num1 / num2
            print(division(num1, num2))
