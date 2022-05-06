#Realizar la carga de dos números por teclado e imprimir la división del primero
#  respecto al segundo, capturar las excepciones 
# ZeroDivisionError y ValueError.

while True:
    try:
        n1 = int(input("ingrese un numero"))
        n2 = int(input("ingrese otro numero"))
        try:
            print(n1+n2, n1/n2)
            print("quiere seguir sumando numeros?")
            seguir = input()
            if seguir == "s":
                pass
            else:
                break
        except ZeroDivisionError as e:
            print ('Error')

    except ValueError as f:
        print("un numero flaco!")
    
