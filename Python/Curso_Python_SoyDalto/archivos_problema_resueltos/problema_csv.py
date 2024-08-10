import pandas as pd  # Importa la librería pandas para la manipulación de datos

# Lee el archivo CSV en un DataFrame de pandas
df = pd.read_csv("C:/Users/Usuario/Desktop/my-first-binder/Python/Curso_Python_SoyDalto/archivos_problema_resueltos\datos.csv")

# Convierte la columna 'edad' a tipo cadena de texto
df['edad'] = df['edad'].astype(str) 

# Reemplaza todas las instancias de "dalto" con "maestro" en la columna 'apellido'
# El argumento 'inplace=True' modifica el DataFrame directamente
df['apellido'].replace("dalto", "maestro", inplace=True)

# Elimina las filas que contienen valores faltantes (NaN)
df = df.dropna()

# Elimina las filas duplicadas
df = df.drop_duplicates()

# Guarda el DataFrame limpio en un nuevo archivo CSV
df.to_csv("C:/Users/Usuario/Desktop/my-first-binder/Python/Curso_Python_SoyDalto/archivos_problema_resueltos\datos_limpios.csv")
