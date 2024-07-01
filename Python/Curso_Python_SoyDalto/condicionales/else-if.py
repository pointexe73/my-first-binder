# ELSE IF

# else-if otra condicional
# El else-if es una combinacion de if y else, permite evaluar
# varias condiciones y ejecutar el bloque de codigo que se cumpla
# primera condicion cierta

ingreso_mensual = 92000
gasto_mensual = 80000

# Evaluar si el ingreso es mayor a 10000
if ingreso_mensual > 10000:
    # Si es cierto, imprimir el mensaje
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficilt")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("esta bien")
    else:
        print("y pa estas gastando una banda")

# Evaluar si el ingreso es mayor a 1000
elif ingreso_mensual > 1000:
    # Si es así, imprimir el mensaje
    print("esta bien latinoamerica")

# Evaluar si el ingreso es mayor a 500
elif ingreso_mensual > 500:
    # Si es así, imprimir el mensaje
    print("esta bien en argentina")

# Evaluar si el ingreso es mayor a 200
elif ingreso_mensual > 200:
    # Si es así, imprimir el mensaje
    print("esta bien en venezuela")

# Si ninguna de las condiciones anteriores se cumple, ejecutar este bloque
else:
    # Imprimir el mensaje
    print("esta mal economicamente")
