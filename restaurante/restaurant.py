valor_perro_caliente, valor_pizza, valor_hamburguesa, valor_papa_frita, valor_gaseosa = 7000, 10000, 15000, 5000, 2000
total_perro_caliente, total_pizza, total_hamburguesa, total_papa_frita, total_gaseosa = 0, 0, 0, 0, 0
cantidad_perro_caliente, cantidad_pizza, cantidad_hamburguesa, cantidad_papa_frita, cantidad_gaseosa = 0, 0, 0, 0, 0
count_perro_caliente, count_pizza, count_hamburguesa, count_papa_frita, count_gaseosa = 0, 0, 0, 0, 0
print("Menu: \n#1 Perro caliente $7.000 \n#2 Pizza $10.000 \n#3 Hamburguesa $15.000 \n#4 Papas fritas $5.000 \n#5 Gaseosa $2.000")
print("------------------------")
cuestion = "si"
option = 0
while (cuestion == "si"):  
    option = int(input("\n¿Qué producto deseas comprar? "))
    if(option == 1):
        count_perro_caliente = int(input("¿Cuántos perros calientes quieres? "))
        cantidad_perro_caliente = cantidad_perro_caliente + count_perro_caliente
        cuestion = input("¿Deseas agregar otro poducto al carrito? Responde 'si' ó 'no': ")

    elif(option == 2):
        count_pizza = int(input("¿Cuántas pizzas quieres? "))
        cantidad_pizza = cantidad_pizza + count_pizza
        cuestion = input("¿Deseas agregar otro poducto al carrito? Responde 'si' ó 'no': ")

    elif(option == 3):
        count_hamburguesa = int(input("¿Cuántas hamburguesas quieres? "))
        cantidad_hamburguesa = cantidad_hamburguesa + count_hamburguesa
        cuestion = input("¿Deseas agregar otro poducto al carrito? Responde 'si' ó 'no': ")

    elif(option == 4):
        count_papa_frita = int(input("¿Cuántas papas fritas quieres? "))
        cantidad_papa_frita = cantidad_papa_frita + count_papa_frita
        cuestion = input("¿Deseas agregar otro poducto al carrito? Responde 'si' ó 'no': ")

    elif(option == 5):
        count_gaseosa = int(input("¿Cuántas gaseosas quieres? "))
        cantidad_gaseosa = cantidad_gaseosa + count_gaseosa
        cuestion = input("¿Deseas agregar otro poducto al carrito? Responde 'si' ó 'no': ")

    else:
        print("Opción incorrecta")
        cuestion = input("¿Desea agregar algún producto al carrito? Responde 'si' ó 'no':")

print("\n------------------------ \nTe confirmamos tu compra:")

if(cantidad_perro_caliente != 0):
    total_perro_caliente = cantidad_perro_caliente * valor_perro_caliente
    if(cantidad_perro_caliente == 1):
        print(f"*{cantidad_perro_caliente} perro caliente = ${total_perro_caliente}")
    else:
        print(f"*{cantidad_perro_caliente} perros calientes = ${total_perro_caliente}")

if(cantidad_pizza != 0):
    total_pizza = cantidad_pizza * valor_pizza
    if(cantidad_pizza == 1):
        print(f"*{cantidad_pizza} pizza = ${total_pizza}")
    else:
        print(f"*{cantidad_pizza} pizzas = ${total_pizza}")

if(cantidad_hamburguesa != 0):
    total_hamburguesa = cantidad_hamburguesa * valor_hamburguesa
    if(cantidad_hamburguesa == 1):
        print(f"*{cantidad_hamburguesa} hamburguesa = ${total_hamburguesa}")
    else:
        print(f"*{cantidad_hamburguesa} hamburguesas = ${total_hamburguesa}")

if(cantidad_papa_frita != 0):
    total_papa_frita = cantidad_papa_frita * valor_papa_frita
    if(cantidad_papa_frita == 1):
        print(f"*{cantidad_papa_frita} porción de papas fritas = ${total_papa_frita}")
    else:
        print(f"*{cantidad_papa_frita} porciones de papas fritas = ${total_papa_frita}")

if(cantidad_gaseosa !=0):
    total_gaseosa = cantidad_gaseosa * valor_gaseosa
    if(cantidad_gaseosa == 1):
        print(f"*{cantidad_gaseosa} gaseosa = ${total_gaseosa}")
    else:
        print(f"*{cantidad_gaseosa} gaseosas = ${total_gaseosa}")

total_buy = (total_perro_caliente + total_pizza + total_hamburguesa + total_papa_frita + total_gaseosa)
print(f"El valor total de tu compra es ${total_buy} \n------------------------\n\nGracias por tu compra\n")
