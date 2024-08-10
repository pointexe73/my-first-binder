# Creando funcion que suma numeros
def sumar_dos():
    # Iniciando un bucle
    while True:
        # Pidiendo numeros
        num1 = input("Ingrese el primer numero: ")
        num2 = input("Ingrese el segundo numero: ")
        # Intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(num1) + int(num2)
        except:
            print("Te pedi un numero salame, no te hagas el gracioso")
        # Si todo salio bien terminamos el bucle
        else:
            break
        finally:
            print("Siempre se ejecuta, no importa si hubo error o no")
        
    # Imprimiendo el resultado
    return resultado

print(sumar_dos())