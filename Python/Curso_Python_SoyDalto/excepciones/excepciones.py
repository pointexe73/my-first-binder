# Creando funcion que suma numeros
def sumar_dos():
    # Iniciando un bucle
    while True:
        # Pidiendo numeros
        num1 = input("Numero 1: ")
        num2 = input("Numero 2: ")
        # Intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(num1) + int(num2)
        except:
            print("Te pedi un numero salame, no te hagas el gracioso")
        # Si todo salio bien terminamos el bucle
        else:
            break
        finally:
            print("Manejo de excepcion finalizado")
        
    # Imprimiendo el resultado
    return resultado

print(sumar_dos())