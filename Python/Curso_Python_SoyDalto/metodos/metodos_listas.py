# METODOS LISTAS

# (-- LIST --)
# creando una lista con list()
lista = ["Lucas Dalto", "Soy Dalto"]

# (-- LEN --) devuelve la cantidad de elementos de una lista
cantidad_elementos = len(lista)

# (-- APPEND --) agrega un elemento al final de la lista
lista.append("jajaja")

# (-- INSERT --) agrega un elemento en una posicion determinada
lista.insert(2, "test")

# (-- EXTENT --) agrega varios elementos al final de la lista
lista.extend(["test2", "test3"])  # se agrega en forma de lista

# (-- POP --) elimina un elemento de la lista
lista.pop(0)  # para eliminar el primer elemento (-1)

# (-- REMOVE --) elimina el primer elemento que se encuentre
lista.remove("jajaja")  # elimina el valor por su nombre

# (-- CLEAR --) elimina todos los elementos de la lista
# lista.clear() # se comenta la linea para no eliminar la lista

# (-- SORT --) ordena los elementos de la lista
lista.sort()  # ordena de menor a mayor
# lista.sort(reverse=True) # ordena de mayor a menor

# (-- REVERSE --) invierte el orden de los elementos de la lista
lista.reverse()

print(f"'--List--'    Lista                  : {lista}")
print(f"'--Len--'     Cantidad de elementos  : {cantidad_elementos}")
print(f"'--Append--'  Agregando un elemento  : {lista[-1]}")
print(f"'--Insert--'  Insertando un elemento : {lista[2]}")
print(f"'--Extend--'  Extendiendo una lista  : {lista[-2:]}")
print(f"'--Pop--'     Eliminando un elemento : {lista[0]}")
print(f"'--Remove--'  Eliminando un elemento : {lista[1]}")
print(f"'--Clear--'   Limpando la lista      : {lista}")
print(f"'--Sort--'    Ordenando la lista     : {lista}")
print(f"'--Reverse--' Revertiendo la lista   : {lista[::-1]}")
print(lista)