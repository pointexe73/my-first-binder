
# listas (list) 
lista = ["Lucas Dalto", "Soy Dalto", True, 185] # se puede modificar

# tuplas (tuple)
tupla = ("Lucas Dalto", "Soy Dalto", True, 185) # no se puede modificar

# agregar elementos a una lista, agregar elementos a una tupla da un error
lista[3] = "Maquinola"

# creando un conjunto (set)
conjunto = {"Lucas Dalto", "Soy Dalto", True, 185} # no se puede modificar, no se puede llamar por indice
# se puede agregar elementos a un conjunto con el método .add(), 
# pero no se puede modificar
# no accepta datos duplicados

# diccionarios (dict) key : value
diccionario = { 
    "nombre": "Lucas",
    "canal": "Soy Dalto",
    "esta emocionado": True,
    "altura": 1.85,
    "dato_duplicado": "Soy Dalto"
}


print(diccionario['altura']) 