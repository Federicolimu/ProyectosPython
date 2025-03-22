persona = {
    "nombre":"Federico",
    "edad":22,
    "profesion":"Estudiante"
    }
print(persona)

colores = dict(
    rojo="#1F0000",
    verde="#00FF00",
    azul="0000FF"
)
print(colores)
print("****************FRUTAS********************")
frutas = ["Manzana","Pera","Mango","Piña","Coco","Uva","Naranja","Coco","Uva","Naranja"] #Esta es mi lista de frutas disponibles al inicio
inventario={}
for i in frutas:
    if i in inventario:
        inventario[i] = inventario[i] + 1
        inventario[i]
    else:
        inventario[i] = 1
print("\n")
print(inventario)
print("Estas son las frutas disponibles",inventario.keys())
print("Estas son las cantidades disponibles",inventario.values())


diccionarioFrutas = {"Uva":3000,"Piña":4000,"Manzana":2000,"Pera":2000,"Mango":1500,"Sandía":8000,"Naranaja":1000}
precio = 0

for elemento in diccionarioFrutas.values():
    precio = precio + elemento
print("El valor de su compra es:",precio)
