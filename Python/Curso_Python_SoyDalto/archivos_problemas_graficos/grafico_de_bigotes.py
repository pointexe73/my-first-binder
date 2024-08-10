import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/Usuario/Desktop/my-first-binder/Python/Curso_Python_SoyDalto/archivos_problemas_graficos/bigotes.csv")

#creando el grafico
sns.boxplot(x="categoria",y="valor",data=df)

#mostrando el grafico
plt.show()
