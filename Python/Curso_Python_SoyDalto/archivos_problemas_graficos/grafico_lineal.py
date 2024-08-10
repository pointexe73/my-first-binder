import pandas as pd  # Importa la librería pandas para el manejo de datos
import matplotlib.pyplot as plt  # Importa la librería matplotlib.pyplot para crear gráficos
import seaborn as sns  # Importa la librería seaborn para crear gráficos estadísticos

# Lee el archivo CSV "pedos.csv" ubicado en la ruta especificada
df = pd.read_csv("C:/Users/Usuario/Desktop/my-first-binder/Python/Curso_Python_SoyDalto/archivos_problemas_graficos/pedos.csv")

# Crea un gráfico de línea utilizando seaborn, con "fecha" en el eje x y "pedos" en el eje y
sns.lineplot(x="fecha", y="pedos", data=df)

# Agrega un punto individual al gráfico en la posición "01-09" en el eje x y 17 en el eje y
plt.plot("01-09", 17, "o")

# Muestra el gráfico creado
plt.show()