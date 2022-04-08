num = int(input())
lista = [int(x) for x in str(num)]
x = True
for i in range((len(lista)-1)):
    if lista[i]-lista[i+1] == 1 or lista[i]-lista[i+1] == -1:
        pass
    else:
        x = False
        
print(x)

        
        