import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/Usuario/Desktop/my-first-binder/Python/Curso_Python_SoyDalto/archivos_problemas_graficos/cofla_ingresos.csv")

sns.barplot(x="fuente", y="ingresos", data=df)

total_ingresos = df['ingresos'].sum()

print(f'El total de ingresos es de: ${total_ingresos} USD')

plt.show()