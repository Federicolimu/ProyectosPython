dato1 = "Manzana"
dato2 = "Pera"
dato3 ="Sandia"

def menuFrutas():
        dato4=input("¡Qué fruta desea agregar al menú?: ")
        frutas=[dato1,dato2,dato3,dato4]
        print(frutas)

frutas=[dato1,dato2,dato3]
print(frutas)

opcion = int(input("¿Desea ingresar una nueva fruta al menú? 1 = SI, 2 = NO "))
if opcion == 1:
    menuFrutas()
else:
    print("No agregó más frutas, por lo que sus frutas disponibles son: ",frutas)


