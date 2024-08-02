# FUNCIONES LAMBDA

# Creando un lista de numeros
numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,20]

# Creando una funcion lambda para multiplicar por 2
multiplicar_por_dos = lambda x : x * 2
# Imprime 10, que es el resultado de multiplicar 5 por 2
print(f'Mult en Lambda: {multiplicar_por_dos(5)}')

# Creando funcion comun que diga si es par o no
def es_par(num):
    if (num%2==0):
        return True

# Utilizando filter con una funcion comun
numeros_pares = filter(es_par, numeros)
# Imprimer numero pares de la lista de numeros
print(f'Numeros pares: {list(numeros_pares)}')

# El mismo codigo pero con Lambda
numeros_pares = filter(lambda numero: numero%2 == 0, numeros)
# Imprimer el mismo resulado que el anterior pero con Lambda
print(f'Funcion con Lambda: {(list(numeros_pares))}')