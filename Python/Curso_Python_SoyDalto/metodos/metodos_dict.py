# Este es un diccionario
diccionario = {
    "nombre" : 'lucas',    # Clave: nombre, valor: Lucas
    "apellido" : 'dalto',  # Clave: apellido, valor: Dalto
    "subs" : 1000000       # Clave: subs, valor: 1000000
}

# Obtiene todas las claves del diccionario
# Las claves son las identificadores únicos de los elementos del diccionario
claves_llaves = diccionario.keys()

# Obtiene el valor de la clave "subs"
# Devuelve el valor asociado a la clave "subs"
claves_enc_valor = diccionario.get("subs")

# Elimina todos los elementos del diccionario
# Devuelve None
elimina_dict = diccionario.clear()

# Elimina el elemento con la clave "nombre"
# Devuelve el valor asociado a la clave "nombre" y lo elimina del diccionario
elimina_elemento = diccionario.pop("nombre")

# Muestra todos los items del diccionario
# Devuelve un generador con los pares clave-valor
muestra_items = diccionario.items()

# Imprime las claves del diccionario
print(claves_llaves)
# Imprime el valor de la clave "subs"
print(claves_enc_valor)
# Imprime el resultado de eliminar todos los elementos del diccionario
print(elimina_dict)
# Imprime el valor del elemento eliminado
print(elimina_elemento)
# Imprime todos los items del diccionario
print(muestra_items)
