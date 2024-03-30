""" Ejemplos """

estado=True 
total=0

def suma(numA,NumB):
    resultado=numA+NumB
    return resultado

try:
    while(estado):
        dato=input("Ingrese el valor del preducto o ingrese (S) para salir:")
        if(dato!='S'):
            total=suma(total,int(dato))
        else:
            estado=False
    
    print("El total es de $",total)

except ValueError:
    print("El valor que ingreso no es valido, intente otra vez.")    
except Exception as error:
    print(error)
           