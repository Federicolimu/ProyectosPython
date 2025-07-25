def suma(num1, num2):
    resultado = num1 + num2
    return resultado
almacena_resultado = suma(5,8)
print(almacena_resultado)

print("Programa de evaluación de alumnos: ")
nota_alumno = input()
def evaluacion(nota_alumno):
    valoracion="Aprobado"
    if nota_alumno < 5:
        valoracion ="Suspenso"
    return valoracion

print(evaluacion(int(nota_alumno)))

