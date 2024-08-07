with open("C:/Users/2024/Desktop/my-first-binder/Python/Curso_Python_SoyDalto/archivos/nu.txt","a", encoding="UTF-8") as archivo:
    # Usando un bucle para agregar varias linea 
    archivo.write("\n")
    for i in range(5): 
        # Agreganos la linea i+1 al archivo
        archivo.write(f"Esta es la linea {i+1}\n") 