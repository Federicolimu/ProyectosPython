"""Decidir si se puede ver una película.
Pide si el usuario tiene más de 12 años y si tiene permiso. Si ambas condiciones se cumplen,
muestra “Puedes ver la película”. Si no, “No autorizado”."""
while True:
    try:
        permission = int(input("Digita 1 si tienes permiso de tus padres para ver la pelicula, sino digita 2: "))
        if (permission == 1):  
            while True:
                try:
                    age = int(input("Perfecto! Ahora que tienes el permiso de tus padres, dime ¿Qué edad tienes? "))
                    if (age > 12):
                        print("Excelente!!! Puedes ver la película")
                        break
                    else:
                        print("Lo siento. No tienes edad suficiente para ver la película")
                        break
                except ValueError:
                    print("Edad incorrecta. Intenta de nuevo")
            break
        elif (permission == 2):
            print("Lo siento. No estás autorizad@ para ver la película")
            break
        else:
            print("Opción incorrecta. Intenta de nuevo")
    except ValueError:
        print("Digito incorrecto. Intenta de nuevo")