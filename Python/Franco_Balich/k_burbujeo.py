lista = [6,5,3,1,8,7,2,4]

def ordenar(lista):
    for i in range(1, len(lista)):
        for j in range(0, len(lista)-1):
            if (lista[j+1] < lista[j]):
                aux = lista[j];
                lista[j] = lista[j+1];
                lista[j+1] = aux;
    return lista

print(lista)
print(ordenar(lista))