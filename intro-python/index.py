#Este es un comentario

if 5>3:
    print('5 es mayor a 3')

if 5<3:
    print('Esto no se va  a imprimir')

x= 5
y = 'Gaby feliz'

#print(x, y)

email = 'gaby.floze@email.sv'

#print(email)

userName = 'Gaby'
#print(userName)

a, b, c = 'Nana', 'Nena', 'Nona'
#print(a, b, c)

a=b=c=d= 'Gabriela Codeando'
print(a, b, c,d)

inicio = 'hola'
final = 'mundo'

#print (inicio + ' ' + final)

palabra = 'Hola Gaby' #String

complemento = "Sigue aprendiendo"

enteroNum = 20 #int
decimalNum = 20.3 #float

complejoNUm = 1j #complejo

#print(palabra, complemento, enteroNum, decimalNum, complejoNUm)

lista = ['Hola', 'Mundo', 'Gaby']
lista2 = lista.copy()
lista2.append('Coding')
#lista.clear()
#print(lista2, lista.count(2))
#print(len(lista))

largoLista = len(lista2) #El metodo len() --> cuenta la cantidad de elementos en una lista
largoLista2 = len(lista)

#print(largoLista, largoLista2)
#print(lista[2])

lista.pop() # pop() --> Elimina el ultimo elemento de una lista
lista.pop()
#print(lista)

lista.remove('Hola') # remove() --> Especifica el elemento a eliminar
#print(lista)

lista2.reverse() #Ordena listas sin importar tipos de datos
#lista2.sort() #Ordena listas del mismo tipo de dato
#print(lista2)

tupla = ('hola', 'mundo', 'somos', 'chidos')
listaDeTupla = list(tupla)
listaDeTupla.append('y geniales')
#print(listaDeTupla)


rango = range(6)
#print(rango)

dictionario = {
    "nombre": "Ceniza",
    "raza": "Persa",
    "edad": 1
}

print(dictionario)
print(dictionario['nombre'])
print(dictionario['raza'])
print(dictionario.get('edad'))

print('-----------------------------')

dictionario['nombre']= "Cenizas"
print(len(dictionario))

#ADD A VALUE IN DICTIONARY
dictionario['ronronea'] = "Si"

print("-----------------------------")
print(dictionario)

print("****ELIMINAR UN VALOR DE DICCIONARIO****")
#ELIMINAR UN VALOR DEL DICCIONARIO
#dictionario.pop('ronronea') 
dictionario.popitem()
#del dictionario ['ronronea']
print(dictionario) #COMPROBAR QUE SE HA ELIMINADO

print("---------#CREAR COPIA DICCIONARIO-----") 
copiaGatito = dictionario.copy() #usando metodo .copy()
print(dictionario, copiaGatito)

print("********COPIA DE DICCIONARIO*********")
#OTRO METODO
copiaGatito = dict(dictionario)
print(copiaGatito)

print("********ELIMINAR DICCIONARIO*********")
dictionario.clear()

print("********DICCIONARIOS ANIDADOS*********")

misGatitos = {
    "Gatito1" : {
        "nombre" : "Carbon",
        "edad": 10
    },
    "Gatito2" : {
        "nombre" : "Cenizas",
        "edad": 1
    }
}

#print(misGatitos) 

print("********DICCIONARIOS PASANDOLOS POR PARAMETROS*********")

cat1 = {
    "nombre" : "Carbon",
        "edad": 10
}
cat2 = {
     "nombre" : "Cenizas",
        "edad": 1
}
misGatitos = {
    "Gatito1" : cat1,
    "Gatito2" : cat2
}

#print(misGatitos)

print("***********CONSTRUCTOR DICT(_)**************")
perritos = dict(nombre = "Ranger", edad= 5)
print(perritos)

print("***********BOOLEANOS**************")
verdadero = True
falso = False

print(verdadero, falso)