print("""Aprueba la materia con una nota final igual o superior a 3.0 "
"y la reprueba con una nota final igual o inferior a 2.9"
"Recuerde que la nota miníma es 0.0 y la nota máxima es 5.0\n""")
validar = 0
while validar != 1:
    nota1 = float(input("Por favor ingrese su primera nota:")) #30%
    while True:
        try:
            if nota1 > 0 and nota1 < 5:
                nota1 = float(input("Por favor ingrese su primera nota:"))
        except ValueError:
            print("Por favor ingrese una nota válida entre 0.0 y 5.0")
    else:
        nota1 =  (nota1 * 0.30)
        nota2 = float(input("Por favor ingrese su segunda nota:")) #30%
        if nota2 > 5:
            while True:
                print("Por favor ingrese una nota válida entre 0.0 y 5.0")
                nota2 = float(input("Por favor ingrese su segunda nota:"))
                break
        else:
            nota2 =  (nota2 * 0.30)
            nota3 = float(input("Por favor ingrese su tercera nota:")) #40%
            if nota3 > 5:
                while True:
                    print("Por favor ingrese una nota válida entre 0.0 y 5.0")
                    nota3 = float(input("Por favor ingrese su segunda nota:"))
                    break
            else:
                nota3 =  (nota3 * 0.40)
                notaFinal = (nota1 + nota2 + nota3)
                print("Su nota final es:",notaFinal)
                if notaFinal >= 3:
                    print("Aprobó la materia")
                    validar = 1
                else:
                    print("Reprobó la materia")
                    validar = 1
