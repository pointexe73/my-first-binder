# Creando mi propia excepcion personalizada
class MiExcepcion(exception):
	def __init__(self,err):
		print(f'Impresionante, cometiste el siguiente error: {err}')

# Lanzando mi propia excepcion
''' raise MiExcepcion("Jajajaj, persona poco culta") '''

try: 
	reise MiExcepcion("jajajaj, persona poco culta")
except:
	print("Como vas a comenter ese error")