# ITERAR DICCIONARIOS

# Diccionario para iterar
diccionario = {
    "nombre":   "lucas",
    "apellido": "dalto",
    "subs":     1000000
}

# Iteración por las claves
# Imprime cada clave en pantalla
for key in diccionario:
    key
    print(f'La clave es : {key}')

# Iteración por las claves y valores
# Imprime cada clave y valor en pantalla
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es : {key} y el valor es : {value}')
