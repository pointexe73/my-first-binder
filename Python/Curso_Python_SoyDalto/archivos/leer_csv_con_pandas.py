import pandas as pd

# Usando la funcion read_csv para lee el archivo CSV
df = pd.read_csv("C:/Users/2024/Desktop/my-first-binder/Python/Curso_Python_SoyDalto/archivos/datos.csv")
df1 = pd.read_csv("C:/Users/2024/Desktop/my-first-binder/Python/Curso_Python_SoyDalto/archivos/datos.csv")

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

# Accediendo a la cantidad de filas y columnas con shape
filas_totales,columna_totales = df.shape

# Obteniendo data estadistica del dataframe
df_info = df.describe()

# Accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]

# Accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2]

# Accediendo a todos los apellidos con loc
apellido_loc = df.loc[:"apellido"]

# Accediendo a todos los apellidos con iloc
apellidos = df.iloc[:,1]

# Accediento a la fila 3 con loc
fila_3 = df.loc[2,:]

# Accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

# Accediendo a filas cn edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]

 
print()