
import csv

with open("C:/Users/2024/Desktop/my-first-binder/Python/Curso_Python_SoyDalto/archivos/datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)