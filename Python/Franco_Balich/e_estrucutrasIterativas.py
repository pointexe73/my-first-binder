""" Estructuras Iterativas """
# for 
for i in range(1,6):
    print(i) 
    
# while
numA = 5
numB = 15

while (numA <= numB):
    numA=numA+1
    if (numA==11):
        continue # continue se salta el numero 11 y break se detiene el numero 11
    print(numA)   