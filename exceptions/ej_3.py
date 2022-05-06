while True:
    tupla = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
            "Agosto","Septiembre","Octubre","Noviembre","Diciembre")

    print(tupla)
    try:
        numero = int(input("Ingrese el número del mes que desea mostrar: "))

        print(tupla[numero-1])
        break
    except IndexError as e:
        print("index error")
