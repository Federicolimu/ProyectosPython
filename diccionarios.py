equipo = {7:"Cristiano Ronaldo",10:"James Rodriguez",8:"Juan Fernando Quintero",1:"Jorge Soto"} #aquí he creado un diccionario con claves y valores

print(equipo.get(6,"No existe un jugador con ese dorsal")) #En caso de que no encuentre esa clave me muestra error.
                                                            #para que se más elegente se hace de esta manera
print(equipo[7])
print(12 in equipo) #busca la clave 12 si la encuentra imprime True, de lo contrario imprime Flase
print(10 in equipo)#imprime esta clave de mi diccionario
print(equipo.keys()) #Me imprime solo las claves del diccionario
print(equipo.values()) #imprime solo los valores del diccionario
print(equipo) #me imprime el diccionario completo
print(equipo.items()) #me imprime el diccionarios separado por tuplas eje: separa cada elemto clave-valor en parentesis y por comas
print(len(equipo)) #cuenta cuantos elementos hay en mi diccionario)
#equipo.clear() #Vacea todo mi diccionario. lo limpia
equipo[9]= "Mbappe" #me agrega un nuevo elemento a mi diccionario
equipo[7]= "Cr7" #Sobre escibe el valor de la clave, en este caso la 7
del(equipo[1]) #Elimina esa clave del diccionario, por ende su valor
print(equipo)

diccionario = {"Federico":{"edad":22,"estatura":1.70}}
# Mi diccionario #Mi clave #Todo esto es mi valor, que a su vez se compone de más claves y valores  
print(diccionario)