# EJERCICIO 2.2

# Creando una función que nos devuelva los numero primos
# Entre 0 y el argumento introducido por teclado.

# funcion verifica si es primo o no
def es_primo(num):
    # Función que devuelve True si el número es primo, False si no
    for i in range(2, num-1):
        # 0 y 1 no son primos, el 2 si. No obstante-
        # ningún número par es primo, excepto el 2, así que no chequeo si num es par
        if num%i == 0: return False
    return True

# funcion que devuelve los numeros primos hasta el numero introducido por teclado
def primos_hasta(num):
    primos = []
    # 0 y 1 no son primos, el 2 si. Así que empiezo en el 3
    for i in range(3, num+1):
        resultado = es_primo(i)
        # Si es_primo(i) devuelve True, lo añado a la lista
        if resultado == True: primos.append(i)
    return primos

# Llamada a la función y print del resultado
resultado = primos_hasta(int(input("Numero: ")))
print(f'Numeros primos: {resultado}')