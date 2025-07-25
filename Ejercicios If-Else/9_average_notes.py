"""Promedio de notas.
Solicita tres notas. Calcula el promedio. Si es mayor o igual a 3.0, muestra “Aprobado”. Si no, “Reprobado”."""

note_1 = float(input("Ingresa tu primera nota: "))
note_2 = float(input("Ingresa tu segunda nota: "))
note_3 = float(input("Ingresa tu tercera nota: "))

average = (note_1 + note_2 + note_3) / 3
print(f"Tu promedio es {(round(average,3))}")

if(average >= 3.0):
    print("Aprobado")
else:
    print("Reprobado")