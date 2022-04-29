class Persona:
    def __init__(self):
        self.nombre = input("nombre ")
        self.edad = int(input("edad "))
        
    def imprimir(self):
        print("nombre:", self.nombre)
        print("edad:" ,self.edad)

persona1=Persona()
persona1.imprimir()


class Empleado(Persona):
    def __init__(self):
        self.sueldo = int(input("sueldo "))

    def impuestos(self):
        if self.sueldo >= 3000:
            print(persona1.nombre, "debe pagar impuestos")

        else:
            print(persona1.nombre  , "no debe pagar impuestos")


empleado1 = Empleado()
empleado1.impuestos()
