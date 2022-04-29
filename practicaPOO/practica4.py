class Operacion:
    def __init__(self):
        self.n1 = int(input("numero 1"))
        self.n2= int(input("numero 2"))
        
    def suma(self):
        print(self.n1+self.n2)
    
    def resta(self):
        print(self.n1-self.n2)

    def mult(self):
        print(self.n1*self.n2)

    def div(self):
        print(self.n1/self.n2)


o1=Operacion()
o1.div()
o1.mult()
o1.suma()
o1.resta()