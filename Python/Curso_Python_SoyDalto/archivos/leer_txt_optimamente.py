
# Abrimos el archivo con with open
with open("archivos\\nu.txt", encoding="UTF-8") as archivo:
    
    # Leermos el archivo
    contenido = archivo.read()
    
    # Mostramos el contenido
    print(contenido)
    
# No es necesario cerrarlo al usar with open