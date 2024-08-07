
# usando open para abrir un archivo con una codificacion universal (UTF-8)
archivo = open("C:/Users/2024/Desktop/my-first-binder/Python/Curso_Python_SoyDalto/archivos/nu.txt", encoding="UTF-8")

# Leer archivo completo
archivo = archivo.read()

# Leer una sola linea 
linea = archivo.readline()

# Leer linea por linea
linea = archivo.readline()

# Cerrar el archivo
archivo.close()

print(linea)