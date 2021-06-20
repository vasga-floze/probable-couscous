#*****************FUNCIONES********************

#crea funcion mediante def
def myFirstFunction():
    print("Mi primera funcion")

#llama funcion
#myFirstFunction()
#************************************************************
#Usando argumentos
"""
def printData(nombre, apellido):
    print("El nombre completo es: ", nombre, apellido)

printData("Gaby","Flores") #pasando los parametros a los args de la funcion
 """
#

 #************************************************************
#Usando argumentos
def printData2(apellido, nombre):
    print("El nombre completo es: ", nombre, apellido)

#printData2(nombre= "Gabriela", apellido="Flores") #Accediendo a la llave del argumento

#************************************************************
def concat(lista):
    c = ''
    for item in lista:
        c = " " + c + item + ' '
        return c
#print lista
#print(*concat(["Vasti", "Flores"]))

#print lista con separador
#print(*concat(["Vasti", "Flores"]), sep = ',')

#print lista con salto de linea
#print(*concat(["Vasti", "Flores"]), sep = '\n')

#************************************************************
#Acceder a los argumentos de la fucnion, como si fueran diccionarios

def printData3(**keyWordArgs): #Argumento por llaves mediante **
    print(keyWordArgs["nombre"], keyWordArgs["edad"])

#printData3(nombre="Gaby", edad= 20)

#************************************************************
#MAS FUNCIONES
#Pasando un valor por defecto en el argumento

def segundFuncion( argumento = "She is the best"):
    print(argumento)

segundFuncion()
segundFuncion("Yasmin")

#************************************************************
#En lugar de agrupar argumentos en una lista, mejor pasar lista
def listaFunction(lista):
    for item in lista:
        print(item)
#llamar funcion, rellenando la lista de la funcion
#listaFunction(["She", "is", "a", "great", "person"])

#************************************************************
#Retonar un valor a utilizar luego 
def concatNames(lista):
    c = ''
    for item in lista:
        c = c + item + " "
    return c
# no se si es igual o  similar a lo que se hace en SQL, pero WoOoOoW
nameComplete = concatNames(["Gabriela", "Flores", "Daniela", "Flores"])
#print(nameComplete)
#************************************************************
#********** UN ASOMO A LO QUE ES RECURSIVIDAD ***************
def recursion(i):
    if i < 1:
        return i
    print(i)
    recursion(i - 1)
recursion(0) #lo tengo en cero porque lo llamo desde modules

"""La recursividad se utiliza por ejemplo cuando se quiere hacer un 
reintentos de conexiones a un servidor, se puede crear una 
fucnion recursiva para que al agotarse el numero limite de itentos 
lance un mensaje de error, que ha sido imposible la conexion"""
