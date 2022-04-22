class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota


    def imprimir(self):
        print(self.nombre)
    

    def estado(self):
        if self.nota>=4:
            print("regular")

        else:
            print("libre")

alumno1=Alumno()
alumno1.inicializar("diego",10)
alumno1.imprimir()
alumno1.estado()

alumno2=Alumno()
alumno2.inicializar("ana",2)
alumno2.imprimir()
alumno2.estado()