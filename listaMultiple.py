nombre = str
edad = int
peso = int
personas=[[],[]]
print("Ingrese los datos de la primera persona:")
nombre = personas[0] = input("Por favor ingrse el nombre:")
edad = personas[0] = int(input("Por favor ingrse el edad:"))
peso = personas[0] = int(input("Por favor ingrse el peso:"))
personas=[[nombre,edad,peso]]
print(personas)
pregunta = int(input("¿Si Dese agregar a otra persona? Ingrese: 1\n¿No desea ingresar a otra persona? Ingrese 0:\n"))
if pregunta == 1:
    print("Ingrese los datos de la segunda persona:")
    nombre = personas[1] = input("Por favor ingrse el nombre:")
    edad = personas[1] = int(input("Por favor ingrse el edad:"))
    peso = personas[1] = int(input("Por favor ingrse el peso:"))
    print("Sus listas quedaron de la siguiente manera:\n",personas)
else:
    print("No se agregará a otra persona...")
    print("Su lista quedó de la siguiente manera:\n",personas)