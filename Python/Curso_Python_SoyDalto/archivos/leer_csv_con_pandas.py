import pandas as pd

# Usando la funcion read_csv para lee el archivo CSV
df = pd.read_csv("C:/Users/Usuario/Desktop/my-first-binder/Python/Curso_Python_SoyDalto/archivos/datos.csv")
df1 = pd.read_csv("C:/Users/Usuario/Desktop/my-first-binder/Python/Curso_Python_SoyDalto/archivos/datos.csv")

# Obteniendo los datos de la columna nombre
nombres = df["nombre"]

# Ordenando el dataframe por la edad
df_ordenado_ascendente = df.sort_values("edad")

# Ordenando de forma descendete 
df_ordenado_descendente = df.sort_values("edad", ascending=False)

# Concatenando los 2 dataframes
df_concatenado = pd.concat([df,df1])

# Accediendo a las 3 primeras fila con head()
primeras_fila = df.head(3)

# Accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)
 
print(ultimas_filas)