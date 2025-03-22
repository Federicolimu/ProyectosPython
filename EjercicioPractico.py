#numeroSecreto = 10
import random #importa librería random que escoge un número aleatorio
numeroSecreto = random.randint(1, 10)
numero = 0
intentosDisponibles = 5 
vecesIntentadas = 0
print("Tienes 5 intentos")
while intentosDisponibles >0:
    numero = int(input("Adivina un número entre 1 y 10:\n"))
    if numero < 1 or numero > 10:
        print("El número ingresado no está en el rango permitido (1-10).\nIntenta de nuevo")
        continue
    else:
        vecesIntentadas = vecesIntentadas + 1
        if numero == numeroSecreto:
            if numero % 5 == 0:
                print("***El número ingresado (",numero,"), es divisible entre 5***")
                pass
            print("¡¡Adivinaste el número Secreto!!")
            print("En",vecesIntentadas,"intento(s)")
            break
        elif numeroSecreto > numero:
            intentosDisponibles -= 1
            if numero % 5 == 0:
                print("***El número ingresado (",numero,") es divisible entre 5***")
                pass
            if intentosDisponibles != 0:
                print("Muy bajo, intenta de nuevo")
                print("Te queda(n)...",intentosDisponibles,"intento(s) disponible(s)")
        else:
            intentosDisponibles -= 1
            if numero % 5 == 0:
                print("***El número ingresado",numero,"es divisible entre 5***")
                pass
            if intentosDisponibles != 0:
                print("Muy alto, intenta de nuevo")
                print("Te queda(n)...",intentosDisponibles,"intento(s) disponible(s)")       
if intentosDisponibles == 0:
    print("¡CANTIDAD DE INTENTOS ALCANZADA!")    

