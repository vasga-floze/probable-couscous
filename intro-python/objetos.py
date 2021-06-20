#Objetos y clases
class User:
    def  __init__(self, name, lastName):
        self.name = name
        self.lastName= lastName
    #Metodos
    def saludo(self):
        print("Hola, mi nombre es: ", self.name, self.lastName)


#user = User("Gabriela", "Flores")
#user2 = User("Daniela", "Flores")
#print(user.name, user.lastName,user2.name, user2.lastName )

#user.saludo()
#user2.saludo()

#************************Herencia**************************
"""
class Admin(User):
    def superSaludo(self):
        print("Hola mi nombre es: ", self.name, " soy Administrador")

admin = Admin("Super", "Feliz")
admin.saludo()
admin.superSaludo()
 """

#***************** Ejercicio de herencia *****************
class Animal:
    def __init__ (self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
        
    def saludo(self):
        print("Hola, soy un " , self.tipo , "y me llamo " , self.nombre, " y mi sonido es el ", self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya): #Extendiendo metodo __init__ de la clase padre
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola, soy un gato extendido')

class Perro(Animal):
    tipo = 'perro'
    def __init__( self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print("instanciando un perro, para que? - no se xD")


class Canario(Animal):
    tipo = "canario"

class Delfin(Animal):
    tipo = "delfin"

gato = Gato("Ceniza", 'maullido')
gato.saludo()

perro = Perro("Ranger", 'ladrido')
perro.saludo()

canario = Canario("Piolin", "cantar")
canario.saludo()

delfin = Delfin("Shark", "Silvido")
delfin.saludo()


