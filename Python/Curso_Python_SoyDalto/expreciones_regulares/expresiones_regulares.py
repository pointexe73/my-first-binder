import re

texto = ''' Hola maestro, esta es la cadena 1, como estas mi capitan
			Esta es la linea 2 de texto
			Y Esta es la final (linea 3) definitiva mi capitan
		'''

# Haciendo una busqueda simple
resultado = re.findall("Esta", texto,)


# \d -> Busca digitos numericos del 0 - 9
resultado = re.findall(r"\d",texto)

# \D -> Busca TODO MENOS digitos numericos del 0 - 9
resultado = re.findall(r"\D",texto)

# \w -> Busca caracteres alfanumericos [a-z, A-Z, 0-9, _]
resultado = re.findall(r"\w",texto)

# \W -> Busca TODO MENOS caacteres alfanumericos [a-z, A-Z, 0-9, _]
resultado = re.findall(r"\W",texto)

# \s -> Busca espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r"\s",texto)

# \S -> Busca TODO MENOS espacios en blanco -> espacios tabs, saltos de linea
resultado = re.findall(r"\S",texto)

# . -> Busca TODO MENOS saltos de linea
resultado = re.findall(r".",texto)

# \n -> Busca saltos de linea
resultado = re.findall(r"\n",texto)

# \ -> Cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
resultado = re.findall(r"\.",texto)

# Armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r"\d\.\s",texto)

#^ Busca el principio de una linea
resultado = re.findall(r"^",texto)

#$ Busca el final de una linea
resultado = re.findall(r"$",texto)

# {n} -> Busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r"\d{4}",texto)

# {n,m} -> Busca al menos n, y como maximo m cantidad de veces el valor de la izquierda
resultado = re.findall(r"\d{1,4}",texto)

# | -> Busca una cosa o la otra
resultado = re.findall(r"\d{1,4}|Hola",texto)

print(resultado)