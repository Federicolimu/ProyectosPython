import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/content/ventas.csv')
#print(df.head()) #Trae los primeros (yo le puedo indicar cuantos)
#de.tail() #Trae los últimos (yo le puedo indicar cuantos)

plt.figure(figsize=(8,5))
plt.hist(df['Cantidad vendida'], bins=20, edgecolor='black')

plt.title('Histograma de Cantidad Vendida')
plt.xlabel('Cantidad vendida')
plt.ylabel('Frecuencia')
plt.grid(axis='y',alpha=0.75)
plt.show()

