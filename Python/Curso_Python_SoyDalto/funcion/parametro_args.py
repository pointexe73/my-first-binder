# PARAMETRO ARGS

# Forma no optima de sumar valores
def suma(lista):
    # Inicializa la variable que almacenará la suma
    numeros_sumados = 0
    # Itera sobre cada elemento de la lista
    for numero in lista:
        # Suma el elemento actual al valor acumulado
        numeros_sumados = numeros_sumados + numero
    # Devuelve la suma total
    return numeros_sumados

# Llama a la función suma con una lista de dos elementos
resultado1 = suma([2,1])
# Imprime el resultado de la suma
print(resultado1)

# Forma optima de sumar valores
def suma_total(numeros):
    # Utiliza la función sum() para sumar todos los elementos de la lista
    return sum([*numeros])

# Llama a la función suma_total con una lista de diez elementos
resultado2 = suma_total([2,1,3,4,5,6,7,8,9,10])
# Imprime el resultado de la suma
print(resultado2)

# Utilizando el operadar *args para sumar valores de una lista
def suma(nombre,*numeros):
    # Crea un string con el nombre y la suma de los números
    return f'{nombre}, La suma de tus numeros es: {sum(numeros)}'

# Llama a la función suma con un nombre y una lista de diez números
resultado3 = suma("lucas",2,1,3,4,5,6,7,8,9,10)
# Imprime el resultado
print(resultado3)
