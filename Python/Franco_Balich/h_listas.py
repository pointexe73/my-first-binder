var = 100

tupla = ("a", "b", "c", "d")
chat = ["Angel", "Raptor", "drkbugs", "franco"]

#for nombre in chat:
#    print(nombre)

num = 0 
while num < len(chat):
    #print(chat[num])
    if (chat[num] == "franco"):
        chat[num] = 'Tomy'
    num = num+1
    
print(chat)