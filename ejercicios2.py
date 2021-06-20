#***************Multiplicar dos numeros sin usar simbolo de multiplicaion**********
a = 5
b = 6
resul = 0

for n in range(a):
    resul += b

#print( a, "* ", b, " =", resul)

#****************Ingresar nombre y apellido e imprimirlo al reved***************
nombre = "Vasti"
apellido = "Flores"

concat = nombre + ' ' + apellido

#print(concat [:: -1]) # se usa una operacion de slais [::-1]

#************Escribir una funcion que encuentre el numero menor de una lista**********
#imprimir numero menor de la lista
lista = [365, 43, 23, 22, 56, 87, 29, -2, 55]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
         menor = x if x < menor else menor

#print('menor:', menor)

#*****************Calcular el volumen de una esfera por su radio***************
# 4/3 * pi * r **3

def calcularVolumen(r):
    return 4/3 * 3.1416 * r **3

print(calcularVolumen(6))

#*****************Verificar si el usuario es mayor de edad***************
def esMayor(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario = Usuario(15)
usuario2 = Usuario(20)

resul1 = esMayor(usuario)
resul2 = esMayor(usuario2)

#print('User 1 es mayor:', resul1 , '\nUser 2 es mayor: ', resul2)

#*****************Verificar si el usuario es masculino***************
def esMasculino(user):
    return user.sex == "m"

class User:
    def __init__(self, sex):
        self.sex = sex

user = User("m")
user2 = User("f")


res1 = esMasculino(user)
res2 = esMasculino(user2)

#print('Usuario uno es masculino:', res1,'\nUsuario dos es masculino: ', res2)

#**********************************************************
# Ask for the user’s first name and
# display the output message
# Hello [First Name] 

#name = input("Type you first name:")

#print('Hello:',name)


#**********************************************************
# Ask for the user’s first name and then ask for
# their surname and display the output message
# Hello [First Name] [Surname]. 
'''
name = input('Type your first name:')
surName = input('Type your surname:')

print('Hello ', name, surName )
 '''
#**********************************************************
# Write code that will display the joke “What do you call a bear with no
# teeth?” and on the next line display the answer “A gummy bear!” Try to
# create it using only one line of code. 

#print('What do you call a bear with no teeth?\nA gummy bear!')
#**********************************************************
# Ask the user to enter
# two numbers. Add
# them together and
# display the answer as
# The total is
# [answer]. 
'''
num1 = int(input('Type a number:'))
num2 = int(input('Type another number:'))

result = num1 + num2

print('The total is: ', result)
'''
#**********************************************************
# Ask the user to enter three
# numbers. Add together the first
# two numbers and then multiply
# this total by the third. Display the
# answer as The answer is
# [answer]. 

# num1 = int(input('Type num1: '))
# num2 = int(input('Type num2: '))
# num3 = int(input('Type num3: '))

# result = (num1 + num2) * num3

# print('The answer is:', result)

#**********************************************************
# Ask how many slices
# of pizza the user
# started with and ask
# how many slices
# they have eaten.
# Work out how many
# slices they have left
# and display the
# answer in a userfriendly format. 

# startedSlices = (int(input("Enter how many slices of pizza you started with:\n")))

# eatenSlices = (int(input("Enter how many slices of pizza have you eaten:\n")))

# enjoy = (startedSlices - eatenSlices)
# print('You still have:', enjoy , 'slices of pizza, enjoy it!')

#**********************************************************
# Ask for the total price of the bill, then ask how
# many diners there are. Divide the total bill by the
# number of diners and show how much each
# person must pay. 

# bill = int(input('Enter the total price of the bill:\n'))
# diners = int(input('How many diners there are?\n'))
# payEachOne = float(bill/diners)
# print('Each one should pay: $',payEachOne)

#********************************************************************
# Write a program
# that will ask for a
# number of days
# and then will
# show how many
# hours, minutes
# and seconds are
# in that number of
# days. 

# days = int(input('Write the number of days you want to convert to hours, minutes and seconds:\n'))
# convertHours = int(days*24)
# convertMinutes = int(convertHours*60)
# convertSeconds = int(convertMinutes*60)
# print()
# print(days, 'days are equal to ', convertHours, 'hours')
# print(days, 'days are equal to ', convertMinutes, 'minutes')
# print(days, 'days are equal to ', convertSeconds, 'seconds')
# print()

#********************************************************************
# There are 2,204 pounds in a kilogram. Ask the
# user to enter a weight in kilograms and convert it
# to pounds. 

# weightKg     =  float(input('Enter your weight in kilograms:\n'))
# weightPounds = float(weightKg*2.204)
# print()
# print("Your weigth in pounds is:", weightPounds)

#********************************************************************
# Task the user to enter a number over 100 and then enter a number under
# 10 and tell them how many times the smaller number goes into the larger
# number in a user-friendly format. 

# bigOne = int(input('Enter a number over 100:\n'))
# smallOne = int(input('Enter a number under 10:\n'))
# numberGoes = bigOne//smallOne
# print('The number', smallOne, 'goes ',numberGoes, 'times in',bigOne)

#********************************************************************
#crear funcion para verificar si el numero es par o impar
# def par(n):
#     return n % 2 == 0

# resultado = par(15)
"""if resultado == True:
    print('El numero es par')
else:
    print('El numero es impar')"""

#********************************************************************
#Escribir una funcion que indique cuantas vocales tiene una palabra
# palabra = 'MurCIElagO'
# vocales = 0
# for letra in palabra:
#     y = letra.lower()
#     vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

# print(vocales)

#********************************************************************
#cantidad infinita de numeros de numeros hasta
#decir basta,  luego que devuelva la suma de los numeros

# lista = []
# print('*****Ingrese cuantos numeros desee y para salir escriba "basta" sin comillas*****')
# while True:
#     valor = input('ingrese valor:')
#     if valor == 'basta':
#         break
#     else:
#         try:
#             valor = int(valor)
#             lista.append(valor)
#         except:
#             print('Dato ingresado es invalido')
#             exit()

# resultado = 0
# for val in lista:
#     resultado += val

# print(resultado)

#********************************************************************
#escribir una funcion que reciba nombre y apelido y los vaya agregandi a un archivo
# def addName(nombre,apellido):
#     archivo = open('nombreCompleto.txt', 'a')
#     archivo.write(nombre+ ' '+apellido+ '\n')
#     archivo.close()

# addName('Gabriela', 'Flores')
#********************************************************************
