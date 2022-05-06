class Operacion:
    def __init__(self):
        self.n1 = int(input("numero 1"))
        self.n2= int(input("numero 2"))
        self.operaciones()
        
        
    def operaciones(self):
        print(self.n1+self.n2)
        print(self.n1-self.n2)
        print(self.n1*self.n2)
        print(self.n1/self.n2)

o1=Operacion()
