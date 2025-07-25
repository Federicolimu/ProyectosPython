distancia = int(input("¿A que distancia vive del colegio? (Km) "))
hermanos = int(input("¿Cuántos hermanos tiene? "))
salarios = int(input("¿Cuanto salario gana su familia al mes? "))
print("Sus datos personles son:\nDistancia de su casa a su colegio:",distancia,"\nCantidad de hermanos:",hermanos,"\nSalario familiar por mes:",salarios)

if distancia > 85 and hermanos > 2 and salarios < 20000:
    print("Usted ha sido aprobado para obtener una beca.")
else:
    print("Usted no cumple con los requisitos. No es apto para recibir esta beca")