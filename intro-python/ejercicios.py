"""dato = input("Ingrese dato: ") #solicitar datos

lista = ["hola", "mundo", "gatitos", "leones", "coders"]

if  lista.count(dato)>0:
    print("El dato --> " , dato ," <-- existe")
else:
    print("El dato -->" , dato ," <-- NO existe")
"""



print("******************SUMA DOS NUM************")
#num1= input("Ingrese primer numero: ")
#num2= input("Ingrese segundo numero: ")

#firstNum = int(num1) #convertir string a int
#secondNum= int(num2) #convertir string a int

#print(firstNum + secondNum)


"""print("************Validación de numero entero al final\
        de obtener los datos del usuario************")

#Solicitar numero uno y capturar posible error
num1= input("Ingrese primer numero: ")
try:
    num1 = int(num1)
except:
    num1 = "Letras"

num2= input("Ingrese segundo numero: ")

#Solicitar numero dos y capturar posible error
try:
    num2 = int(num2)
except:
    num2 = "Letras"

#Validar el mensaje de salida del error mediante un if
if num1 == "Letras" or num2 == "Letras":
    print("Para hacer una suma debe ingresar numeros")
else:
    print("La suma es: ", num1+num2)"""


#Validar las entradas del usuario despues de cada input
#Solicitar numero uno y capturar posible error
num1= input("Ingrese primer numero: ")
try:
    num1 = int(num1)
except:
    num1 = "Letras"

if num1 == "Letras" :
    print("El primer numero ingresado es invalido")
    exit()

num2= input("Ingrese segundo numero: ")

#Solicitar numero dos y capturar posible error
try:
    num2 = int(num2)
except:
    num2 = "Letras"

if num2 == "Letras" :
    print("El segundo numero ingresado es invalido")
    exit()

print("La suma es: " , num1 + num2)

print("****Agregando mas operaciones y solicitando al user el operador****")

simb = input("ingrese operador: ")

if simb == "+":
    print("Suma: ", num1 + num2)
elif simb == "-":
    print("resta: ", num1 - num2)
elif simb == "*":
    print("multiplicacion:", num1 * num2)
elif simb == "/":
    print("division: ", num1 / num2)
else:
    print("El numero ingresado no es valido")
