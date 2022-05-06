while True:
    n1 = int(input("ingrese un numero"))
    n2 = int(input("ingrese otro numero"))
    try:
        print(n1+n2)
        print("quiere seguir sumando numeros?")
        seguir = input()
        if seguir == "s":
            n1 = int(input("ingrese un numero"))
            n2 = int(input("ingrese otro numero"))
        else:
            break
    except ValueError as e:
        print ('Value Error')
        
    


