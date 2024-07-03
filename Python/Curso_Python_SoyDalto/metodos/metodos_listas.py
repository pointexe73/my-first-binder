# METODOS LISTAS

# (-- LIST --)
# creando una lista con list()
lista = list(["Lucas Dalto", "Soy Dalto", True, 185])

# (-- LEN --) devuelve la cantidad de elementos de una lista
cantidad_elementos = len(lista)

# (-- APPEND --) agrega un elemento al final de la lista
agrega_elemento = lista.append("jajaja")

# (-- INSERT --) agrega un elemento en una posicion determinada
inserta_elemento = lista.insert(2, "test")

# (-- EXTENT --) agrega varios elementos al final de la lista
extiende_lista = lista.extend(["test2", "test3"]) # se agrega en forma de lista




print(f"Lista '--List--': {lista}")
print(f"Cantidad de elementos '--Len--': {cantidad_elementos}")
print(f"Agregando un elemento '--Append--': {agrega_elemento}")
print(f"Insertando un elemento en una posicion determinada '--Insert--': {inserta_elemento}")
pritn(f"Extendiendo una lista '--Extend--': {extiende_lista}")


2.17.41