# Codigo que calcula cuanto tardarias en decir una frase si tuvieras que decirla

# Solicita la frase al usuario
frase = input("Decime una frase y te calculo cuento tardarias si tuvieras que decirla: ")

# Separa las palabras de la frase en una lista
palabras_separadas = frase.split(" ")

# Cuenta la cantidad de palabras en la frase
cantidad_de_palabras = len(palabras_separadas)

# Comprueba si la cantidad de palabras es mayor a 120
if cantidad_de_palabras > 120:
    # Si es mayor, imprime un mensaje de humor
    print("Para flaco tampoco te pedi un testasmento")
    
# Imprime la cantidad de palabras y cuanto tardarias en decirlo
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')

# Calcula y imprime cuanto tardarias en decirlo si lo dijeras de forma rápida y clara
print(f'Dalto lo diria en {cantidad_de_palabras * 100 // 2 *1.3 / 100 } segundos')
