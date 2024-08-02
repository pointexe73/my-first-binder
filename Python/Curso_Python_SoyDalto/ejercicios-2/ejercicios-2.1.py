# EJERCICIOS 2.1

# Falto el profe y los chicos van a armar la clase

# Impresar el nombre y la edad de los compañeros que vinieron hoy a clase
def obtener_compa_eros(cantidad_de_compa_eros):
    # Lista para almacenar los compañeros
    compa_eros = [] 
    for i in range(cantidad_de_compa_eros): 
        nombre = input("Ingrese el nombre del compa_ero: ") 
        edad = int(input("Ingrese la edad del compa_ero: ")) 
        # Tupla con el nombre y la edad del compañero
        compa_ero = (nombre, edad) 
        # Agregamos la tupla a la lista de compañeros
        compa_eros.append(compa_ero) 
        # Ordenamos la lista de compañeros por edad
    compa_eros.sort(key = lambda x : x[1]) 
    # El asistente es el compañero mas joven, que esta en la primera posición de la lista
    asistente = compa_eros[0][0] 
    # El profesor es el compañero mas viejo, que esta en la ultima posición de la lista
    profesor = compa_eros[-1][0] 
    # Devolvemos el nombre del asistente y el profesor
    return asistente, profesor 

# Llamamos a la función y le pasamos la cantidad de compañeros que vinieron a clase
asistente, profesor = obtener_compa_eros(5) 
# Imprimimos el nombre del profesor y el asistente
print(f"El profesor es: {profesor} y su asistente es {asistente}") 