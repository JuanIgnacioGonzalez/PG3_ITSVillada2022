lista = [1,3,5,6,7,9,12,34,67,2,4]
print(lista)
num = int(input("que numero"))
try :
    print(lista.index(num))
except :
    print("no se encuentra")