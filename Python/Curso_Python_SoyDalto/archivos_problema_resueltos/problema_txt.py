# 2 listas, una con nombres otra con apellidos
nombres = ["Lucas", "Matias", "Camila", "Pedro", "Roberto"]
apellidos = ["Dalto", "Zing", "Dalto", "Robetix", "Tarado"]

# Registar esta informacion en un TXT de forma optima

# Abre el archivo "nombres_y_apellidos.txt" en modo escritura ("w").
# Si el archivo no existe, se creará.
with open("nombres_y_apellidos.txt","w") as arch:
    # Escribe un encabezado en el archivo.
    arch.writelines("Los datos son:\n\n")
    # Itera sobre las listas de nombres y apellidos usando zip para emparejar cada nombre con su apellido.
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-----------\n") for n,a in zip(nombres,apellidos)]
    