# METODOS DE CADENAS

cadena1 = "Hola soy dalto"
cadena2 = "Bienvenido maquinola"
cadena3 = "1998"
cadena4 = "Solo"

# dir devuelve una lista con todos los metodos de una cadena
resultado_dir = dir(cadena1)


# upper convierte una cadena a mayúsculas
resultado_upper = cadena1.upper()
print(f"Todas las letra en Mayusculas: {resultado_upper}")

# lower convierte una cadena a minúsculas
resultado_lower = cadena1.lower()
print(f"Todas las letra en minusculas: {resultado_lower}")

# capitalize convierte la primer letra de una cadena en mayúscula
resultado_capitalize = cadena1.capitalize()
print(f"La primera letra en Mayuscula: {resultado_capitalize}")

# find devuelve el indice de la primera coincidencia
resultado_find = cadena1.find("D") # Devuelve -1 si no hay coincidencias
print(f"Indice de la primera coincidencia: {resultado_find}")

# index devuelve el indice de la primera coincidencia
resultado_index = cadena1.index("a") # Devuelve ValueError si no hay coincidencias
print(f"Indice de la primera coincidencia: {resultado_index}")

# isnumeric devuelve True si la cadena es numerica
resultado_isnumeric = cadena3.isnumeric()  # Devuelve True si la cadena es numerica
print(f"Es numerica: {resultado_isnumeric}")

# isalpha devuelve True si la cadena es alfabetica
resultado_isalpha = cadena4.isalpha()  # Devuelve True si la cadena es alfabetica
print(f"Es alfabetica: {resultado_isalpha}") # los espacios tambien cuentan son caracteres especiales

# count cuenta el numero de coincidencias de una cadena
resultado_count = cadena1.count("o")
print(f"El numero de coincidencias es: {resultado_count}")

# len devuelve la longitud de una cadena
resultado_len = len(cadena1)
print(f"La longitud de la cadena es: {resultado_len}")

# startswith devuelve True si la cadena empieza con el argumento
resultado_startswith = cadena1.startswith("Hola")
print(f"La cadena empieza con Hola: {resultado_startswith}")

# endswith devuelve True si la cadena termina con el argumento
resultado_endswith = cadena1.endswith("dalto")
print(f"La cadena termina con dalto: {resultado_endswith}")

# replace reemplaza una cadena por otra, sino conside con la cadena no se reemplasara nada y devolvera la misma cadena
resultado_replace = cadena1.replace("Hola", "Holo") # reemplace Hola por Holo
print(f"La cadena remplazada es: {resultado_replace}")

# split divide una cadena en una lista
resultado_split = cadena1.split(" ")
print(f"La cadena se divide en una lista: {resultado_split}")