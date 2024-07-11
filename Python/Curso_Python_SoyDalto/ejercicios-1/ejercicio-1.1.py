# EJERCICIO 1.1 

# promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

# diferencia de duración
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

# calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10



# mostrando las diferencias de duracion ( ejercicio A )
print(f'EL curso de Dalto dura un {diferencia_con_min}% menos que el más rapido')
print(f'EL curso de Dalto dura un {diferencia_con_max}% menos que el más lento')
print(f'EL curso de Dalto dura un {diferencia_con_promedio}% menos que el promedio')

# mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio')

