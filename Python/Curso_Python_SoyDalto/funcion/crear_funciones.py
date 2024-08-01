# CREAR FUNCIONES

def saludar(): 
    # Imprime un saludo
    print("Hola Luis como estas maquina")
    
saludar()


# Crear un funcion que tenga un parametros
def saludar(nombre, sexo):
    # Convierte el sexo a minúsculas
    sexo = sexo.lower()
    # Define el adjetivo basado en el sexo
    if (sexo == "mujer"):
        adjetivo = "mujer"
    elif (sexo == "hombre"):
        adjetivo = "Hombre"
    else:
        adjetivo = "Totin"
        
    # Imprime un saludo personalizado
    print(f'Hola {nombre}, mi {adjetivo}, Como andas')
    
saludar("Luis", "hombre")
saludar("Sofia", "mujer")
saludar("LO","No binario" )


# Crear una funcion que nos retorne valores
def crear_contrasena_random(num):
    # Define los caracteres para la contraseña
    chars = "abcdefghij"
    # Convierte el número a string
    num_entero = str(num)
    # Obtiene el primer dígito del número
    num = int(num_entero[0])
    # Calcula los índices de los caracteres
    c1 = num - 2
    c2 = num
    c3 = num - 5
    # Genera la contraseña
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    # Devuelve el valor a la funcion
    return contrasena,num

# Desempaquetando la funcion
password, primer_numero = crear_contrasena_random(1)

# Mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El número utilizado para crearla fue: {primer_numero}")