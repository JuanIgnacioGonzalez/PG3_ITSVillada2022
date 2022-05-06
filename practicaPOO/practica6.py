
class Familia:
    def __init__(self,hijos):
        self.nombre_p = input("nombre del padre ")
        self.nombre_m = input("nombre de la madre ")
        self.hijos = hijos
        self.hijos.append(self.nombre_p)
        self.hijos.append(self.nombre_m)
        self.familia = ''
        cont =0
        for i in self.hijos:
            if cont == 0:
                self.familia += i
            else:
                self.familia += ', '+i
            cont+=1
             

    def __str__(self):
        return(str(self.familia))
        
        

familia1=Familia(["pedro",'juan','luli'])
print(familia1)
