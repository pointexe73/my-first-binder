""" Estructuras Condicionales"""
# if elif else

A = 10
B = 12

if (A > B): # La condicion tiene que ser (True)
    print("Hola")
elif (A == B):
    print("Los numeros son iguales.")
else:
    print("B es mayor")     
    
edad = 18

if (A>=B and edad>=18 and A%2==0):
    print("La condicion compleja se ejecuto")
else:
    print("No se ejecuto la condicion compleja")