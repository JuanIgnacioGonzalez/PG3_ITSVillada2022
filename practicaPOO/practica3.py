class Triangulo:
    def inicializar(self, lado1, lado2, lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
        self.lista = [self.lado1, self.lado2, self.lado3]

    def lado_mayor(self):
        print(max(self.lista))
    
    def equilatero(self):
        if self.lado1==self.lado2 and self.lado3==self.lado1:
            print("es equilatero")
        else:
            print("no es")

        
triangulo1 = Triangulo()
triangulo1.inicializar(3,3,3)
triangulo1.lado_mayor()
triangulo1.equilatero()







