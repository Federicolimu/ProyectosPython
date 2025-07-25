#Las tuplas son inmutables, o sea no se pueden modificar
#Se pueden utilizar como claves de un diccionario

mitupla=("Juan",13,1,1995)
print("El elemento de la posición 2 es:")
print(mitupla[2]) #Imprime el lememnto en la posicion 2

#Una tupla se puede convertir en una lista

milista=list(mitupla) #Acá hemos convertido la tupla en formato de lista
print("Esta es una lista porque está en []")
print(milista) #Imprimimos la lista creada a base de la tupla

print("Esta es mi tupla original porque está en ()")
print(mitupla)

print(mitupla.count(1995))#Count me cuenta cuantas veces está el elemento en mi tupla
print("En la tupla hay una cantidad de elementos:")
print(len(mitupla))#Cuenta la cantidad de elementos que hay en el tupla

#Podemos unir tuplas con diccionarios:
tupla_pais=["España","Francia","Inglaterra","Alemania"]
diccionario_ciudad={tupla_pais[0]:"Madrid",tupla_pais[1]:"Paris", tupla_pais[2]:"Londres", tupla_pais[3]:"Berlin"}
print(diccionario_ciudad["Francia"])#Podemos buscar un valor por medio de la clave