# FUNCIONES

# Lista de números
numeros = [4, 7, 1, 42, 15]

# Encontrar el número más alto en la lista
numero_mas_alto = max(numeros)
# Imprimir el número más alto (42)
print(f'El numero mas alto es: {numero_mas_alto}')

# Encontrar el número más bajo en la lista
numero_mas_bajo = min(numeros)
# Imprimir el número más bajo (1)
print(f'El numero mas bajo es: {numero_mas_bajo}')

# Redondeando decimales
numero = round(12.345678,3) # Primer valor es el numero a redondear,
# el segundo es el numero de decimales a los que se quiere redondear
# Imprime (12.346)
print(f'Redondeo a 3 cifras: {numero}')

# Retorna False 0, vacio, None, False, None, [], {}, ()
resultado = bool(0) # Retorna False si el valor esta vacio o es 0 o nada 
# Imprime False 
print(f'Retorna False: {resultado}') # Si el valor diferente devuelve True

# Retorna True si todos los valores son verdaderos
resultado = all([1, True, [12, 34, 56]]) # Retorna True si todos los valores son verdaderos,
# si uno es falso devuelve False
# Imprime True
print(f'Retorna True si todos los valores son verdaderos: {resultado}') # Si el valor diferente devuelve False.

# Suma todos los valores de un iterable
suma_total = sum(numeros) # Suma todos los valores de un iterable
# Imprime 79
print(f'Suma todos los valores de un iterable: {suma_total}') # Todos los valores de la cadena tienen que ser-
# numero si hay otro valor da un expeccion