class Animal:
    def __init__(self, tipo, nombre):
        self.tipo=tipo
        self.nombre= nombre
        print("Elementos de la clase Base Animal: ", self.tipo, self.nombre)
    def saludo(self):
        print ("Hola desde la clase Base")

#al extender se heredan las propiedades de la clase padre, 
class Gato(Animal):
    def __init__(self, tipo, nombre, edad): #edad es una propiedad específica de la clase Gato
        Animal.__init__(self,tipo,nombre)
        self.edad = edad  #propiedad específica de la clase Gato
        print ("edad: ", self.edad)  # al extender permite modificar, como en este caso se imprime la edad
    def saludo(self):#extendiendo metodo saludo()
        super().saludo()
        print("Hola desde la clase derivada")
#gato= Gato("Gato","Minimi", 2)
#gato.saludo()

class OtraClase(Gato):
    def __init__(self, tipo, nombre, edad, genero):
        Gato.__init__(self, tipo, nombre, edad)
        self.genero=genero
        print ("genero: ", self.genero)
    def saludo(self):
        super().saludo()
        print("Hola desde la clase OtraClase")

class OtraOtraClase(OtraClase):
    def __init__(self, tipo, nombre, edad, genero, duenio):
        OtraClase.__init__(self, tipo, nombre, edad, genero)
        self.duenio = duenio
        print ("El dueño de ",  self.nombre, "es ", self.duenio)


otra=OtraOtraClase("Gato","Minimi", 2, "Masculino", "Gys")
otra.saludo()