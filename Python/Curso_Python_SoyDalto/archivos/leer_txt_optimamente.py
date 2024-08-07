
# Abrimos el archivo con with open
with open("C:/Users/2024/Desktop/my-first-binder/Python/Curso_Python_SoyDalto/archivos/nu.txt", encoding="UTF-8") as archivo:
    
    # Leermos el archivo
    contenido = archivo.read()
    
    # Mostramos el contenido
    print(contenido)
    
# No es necesario cerrarlo al usar with open