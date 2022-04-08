vocales = ('a','e','i','o','u')
lista = list(input("dame una palabra").lower())
contador=0
for i in (lista):
    for x in (vocales):
        if i == x:
            contador = (contador+1)
        
print(contador)

