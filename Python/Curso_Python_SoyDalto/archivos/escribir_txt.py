with open("archivos\\nu.txt","w", encoding="UTF-8") as archivo:
    # Sobreescribir el archivo con la nueva información
    archivo.write("Hola mundo")
    
    # Agregando 2 linea con writelines
    archivo.writelines(["\nBienvenidos a Python", "\nEstamos aprendiendo a escribir en archivos"])
    
    # Agregando otra lineas
    archivo.write("\nAdios")