# DICCIONARIOS

# Creando diccionario con dict()
diccionario = dict(nombe="lucas", apellido="dalto")

# Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto","rancio" ]):"ajaja"}

# Crenado un diccionario con fromkeys() valor por defecto: None
diccionario = dict.fromkeys(["nombre", "apellido"])

# Creando un diccionario con fromkeys() cambiando el valor por defecto a "No se"
diccionario = dict.fromkeys(["nombre", "apellido"])

# Imprime el valor de la clave
print(diccionario["nombre"])