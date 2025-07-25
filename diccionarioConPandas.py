import pandas as pd
inventariofrutas={
    "productos":["Manzanas","Peras","Mangos"],
    "cantidad":[100,50,None],
    "precio":[1000,2000,4000]
    }

df_inventario=pd.DataFrame(inventariofrutas)
print("Inventario en estado inicial:")
print(df_inventario)

#RECUENTA CUANTOS CAMPOS TIENEN VALORES NULOS.
df_reconteo = df_inventario.isnull().sum()
print("Inventario de reconteo de valores nulos:")
print(df_reconteo)

#AQUÍ ELIMINAMOS LA FILA QUE TENGA VALORES NULOS:
#EN ESTE CASO ELIMINA LA FILA DE MANGOS.
df_sin_nulos = df_inventario.dropna()
print("Inventario sin filas de valores nulos:")
print(df_sin_nulos)

#AQUI VAMOS A RELLENAR EL DATO NULO CON EL PROMEDIO DE LOS DEMÁS DATOS:
#EN ESTE CASO AGREGÓ EL PROMEDIO A LA FILA DE MANGOS.
print("Inventario rellenado con promedio en los valores nulos:")
df_rellenado = df_inventario.fillna(df_inventario.mean(numeric_only=True))
print(df_rellenado)