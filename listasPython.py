milista=["Maria","Pepe","Marta","Antonio"]
print(milista)
milista.insert(2,"Sandra") #Agrega otro elemento a la lista 
#pero a diferencia del .append este lo inserta en la posición que le indico
print(milista)

print("Antonio está",milista.index("Antonio"),"veces en la lista")
#La linea anterior me dice cuantas veces está el elemento en mi lista
print("Pepe" in milista)#Busca a ese elemento en mi lista, si existe imprime True
print("Fede" in milista)#Busca a ese elemento en mi lista, si no existe imprime False

milista.pop() #Elimina el último elemento de mi lista
print(milista)