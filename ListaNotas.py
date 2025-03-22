notas=[]
suma = 0
for i in range (5):
    try:
        nota=(int(input("Por favor ingrese la nota:")))   
        if nota <= 5:
            print("")
    except ValueError:
        print("Ingrese una nota válida")
    notas.append(nota)
    suma = suma + nota
    promedio = suma/5       
print("Sus notas son:")
print(notas)
print("El promedio de sus notas es: ",promedio)
if promedio > 3:
    print("Usted aprobó la asignatura")
elif promedio >= 2.5 and promedio <= 2.9:
    print("Usted deberá habilitar la asignatura")
print("Usted reprobó la asignatura")

