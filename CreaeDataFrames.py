#Creación de una Serie ¿Cómo crearías una Serie de Pandas a partir de la lista [10, 20, 30, 40]
# y asignarle índices personalizados ['a', 'b', 'c', 'd']?
import pandas as pd
df_lista=pd.Series([10,20,30,40],index=['a','b','c','d'])
print(df_lista)


#Series desde un diccionario Explica cómo crear una Serie a partir del diccionario
# {'x': 100, 'y': 200, 'z': 300}. ¿Cuál será el índice en esta Serie?
import pandas as pd
diccionario={'x':100, 'y':200,'z':300}
df_diccionario=pd.Series(diccionario)
print(df_diccionario)

#Selección de elementos en una Serie Dada la Serie 
# serie = pd.Series([5, 10, 15, 20], index=['a', 'b', 'c', 'd']), 
# ¿cómo obtienes el valor asociado al índice 'c'? ¿Qué tipo de dato (Python vs. NumPy) te devuelve?
import pandas as pd
serie = pd.Series([5, 10, 15, 20], index=['a', 'b', 'c', 'd'])
print(serie['c'])
print(type(serie['c']))

#Operaciones aritméticas
# Teniendo dos Series con índices coincidentes, por ejemplo:
#serie1 = pd.Series([1, 2, 3], index=['a','b','c'])
#serie2 = pd.Series([4, 5, 6], index=['a','b','c'])
#¿cómo realizas la suma y la multiplicación de ambos objetos y qué sucede si los índices no coinciden?
import pandas as pd
serie1 = pd.Series([1, 2, 3, 4, 5], index=['a','b','c','d','e'])
serie2 = pd.Series([4, 5, 6], index=['a','b','c'])
suma = serie1 + serie2
print("Suma")
print(suma)
multiplicacion = serie1 * serie2
print("Multiplicación")
print(multiplicacion)

#Creación de un DataFrameCrea un DataFrame que contenga tres columnas:
# Nombre, Edad y Ciudad, a partir de un diccionario de listas. Menciona cómo Pandas “agrupa”
# Series para formar un DataFrame.
import pandas as pd
personas={
    "Nombre":["Daniel","Federico","Jennifer","Diego"],
    "Edad":[24,22,32,37],
    "Ciudad":["Armenia","Circasia","Salento","Pijao"]
}
df_personas=pd.DataFrame(personas)
print(df_personas)
#Un DataFrame ó DataSet es un conjunto de series de datos (Columna)
#En este caso estamos convirtiendo cada diccionario a columna (SERIE)
#Y con todas estas columnas estamos formando un DataFrame

#Acceso y filtrado de datos en un DataFrame
#¿Cómo seleccionarías solo la columna Edad de tu DataFrame?
#¿Cómo filtrarías las filas para ver únicamente las personas con edad mayor a 30 años?
import pandas as pd
edades=df_personas[df_personas["Edad"]>30]
print(edades)
#Me trae las personas que cumplan con la condición (Mayores a 30)

