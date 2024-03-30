lista = ["A", "B", "C", "D"]

diccionario = {"A":["1", "2", "3"], "B":"BBBB", "C": "CCCCC"}



for i in diccionario:
    print(diccionario[i])
    if diccionario[i] == "BBBB":
        diccionario[i] = "Hola"
        
print(diccionario)