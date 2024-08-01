# FUNCIONES EXTRAS

# Creando una funcion de 3 parametros

def frase(nombre, apellido, adjetivo):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}!'

fraseR = frase("Juan", "Perez", "capo")
print(fraseR)

# Creando la misma funcion con un parametro opcional
def frase(nombre, apellido, adjetivo = "capo"): # Parametro definido por defecto
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}!'

fraseRE = frase("Juan", "Perez","inteligente") # Parametro opcional cambiado
print(fraseRE)