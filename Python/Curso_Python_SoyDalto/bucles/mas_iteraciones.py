# MAS ITERACIONES

# Lista de frutas
frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = "Hola soy Luis"

# Iterar sobre cada fruta
for fruta in frutas:
    # Si la fruta es "manzana", saltar a la siguiente iteración
    if fruta == "manzana": 
        continue # Saltar a la siguiente iteración
    # Imprimir el texto "Me voy a comer {fruta}"
    print(f'Me voy a comer {fruta}')

print('Fin del programa 1 \n') 

# Iterar sobre cada fruta en la lista "frutas"
for fruta in frutas:
    # Si la fruta es "pera", salir del ciclo for
    if fruta == "pera":
        break # Salir del ciclo for
    # Imprimir el texto "Me voy a comer {fruta}"
    print(f'Me voy a comer {fruta}')

# Imprimir el mensaje "Fin del programa" una vez el ciclo for ha finalizado
print('Fin del programa 2 \n')


# Iterar sobre cada letra en la cadena "HolasoyDalto"
for letra in cadena:
    print(letra)