class Persona:

    def inicializar(self,nombre):
        self.nombre=nombre

    def imprimir(self):
        print(self.nombre)

persona1=Persona()
persona1.inicializar("nacho")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("tomi")
persona2.imprimir()