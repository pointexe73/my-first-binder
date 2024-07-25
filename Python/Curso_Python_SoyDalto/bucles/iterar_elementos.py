# ITERAR LISTAS
# FOR

animales = ["perro", "gato", "pajaro", "loro", "cocodrilo"]

numeros = [52 , 16, 14, 72]

# Muestra todos los elementos de la lista "animales"
for animal in animales:
    # Muestra el valor actual de la variable "animal" en cada iteracion
    print(f'Ahora la varible animal es igual a: {animal}')

# Muestra todos los elementos de la lista "numeros"    
for numero in numeros:
    # Multiplica cada elemento por 10 y lo muestra
    resultado = numero * 10
    print(resultado)

# FOR anidados, iterar dos listas en simultaneo 
for animal, numero in zip(animales, numeros):
    print(f'recorriendo lista 1: {animal}')
    print(f'recorriendo lista 2: {numero}') 

# Forma no optima de recorrer una lista con su indice
# No funciona en conjuntos
for num in range(len(numeros)):
    print(numeros[num])
    
# Forma optima de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y el valor es: {valor}')
    
# Usando el FOR/ELSE
for numero in numeros:
    print(f'Ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print("El bucle ha terminado")
    
# TODO LO ANTERIOS FUNCIONA EXACTAMENTE IGUAL PARA TUPLAS Y CONJUNTOS