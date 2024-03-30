""" Try Except """

def suma(numA,numB):
    resultado=numA+numB
    return resultado
try:
    print(suma(1,3))
    
except Exception as error:
    print(error)
    
finally:
    print("Se termino el codigo")