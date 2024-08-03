# EJERCICIO 2.3

# Creando una funcion que muestre la serie fibonacci entre 0 y el numero dado

# Funcion fibonacci
def fibonacci(num):
    # Varibles 
    a, b = 0, 1
    # Lista 
    fibonacci_lista = []
    for i in range(num):
        # Verifica si el numero es mayor que b, si es asi retorna la lista
        if b > num: return fibonacci_lista
        else:
            # Agrega el numero a la lista
            fibonacci_lista.append(b)
            a, b = b, a + b
            
resultado = fibonacci(int(input("Ingrese un numero fib: ")))
print(resultado)