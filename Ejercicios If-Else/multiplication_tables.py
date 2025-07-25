start = "si"
while (start == "si"):
    number = int(input("¿Qué tabla de multiplicar deseas conocer? "))
    for i in range (1,11):
        print(f"{number} * {i} = {i * number}")
    start = input("¿Desea conocer más tablas de multiplicar?\nSi es así, escibra 'si', de lo contrario 'no' ")
print("Apagando el sistema...\nApagado")
