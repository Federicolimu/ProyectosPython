frutas = ["Manzana","Pera","Mango","Piña","Coco","Uva","Naranja","Coco","Uva","Naranja"] #Esta es mi lista de frutas disponibles al inicio
inventario={}
print("Estas son sus frutas disponibles:",frutas)
for elemento in frutas:
    if elemento in inventario:
        inventario[elemento] = inventario[elemento] + 1
        inventario[elemento]
    else:
        inventario[elemento] = 1
print("\n")
print("Usted tiene disponible las siguientes cantidades:")
print(inventario)
