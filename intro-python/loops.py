
#while
"""i=0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)"""



"""
#For loop
#Interando sobre listas
usuarios = ["Gabriela", "Yasmin", "Juan", "Mateo"]

for user in usuarios:
    print(user)

#Iterando sobre strings del last indice de lista anterior
for c in user:
    print(c)

"""

# Loops usando break
"""
users = ["Gabriela", "Yasmin", "Juan", "Mateo"]

for user in users:
    print(user)
    if user == "Yasmin":
        break
"""

# Loops usando continue
"""
users = ["Gabriela", "Yasmin", "Juan", "Mateo"]

for user in users:
    
    if user == "Gabriela": #Si user es Gabriela se lo saltará e imprimira el next
        continue
    print(user)
 """


# Loops usando el range
"""
for x in range(1, 100, 5):
    print(x)
else:
    print("Hemos terminado")
"""

# Loops usando for anidado
"""
users = ["Gabriela", "Yasmin", "Juan", "Mateo"]

edades = [20, 35, 30, 25]

for user in users:
    for edad in edades:
        print(user, edad)
 """


