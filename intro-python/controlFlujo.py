"""if 2 < 5:
    print("2 es menor que 5")

if 2==2:
    print("2 es igual a 3")

if 2==3:
    print("2 es igual a 3")

if 2>5:
    print("2 es mayor a 5")

if 2 != 2:
    print("2 es distinto a 2")    

if 3!= 2:
    print("3 es distinto a 2")

if 3<= 3:
    print("3 es menor o igual a 3")"""

if 2>10:
    print("2 es mayor a 10")
elif 2<10:
    print("2 es menor a 10")
else:
    print("Imprime si las envaluaciones anteriores son falsas")


print("**********if de una sola linea**************")
if 2 < 5 : print("if de una sola linea")

print("*************If ternario**********")
print("cuando sea cierto") if 5<2 else print("cuando sea falso")

print("************* operadores AND, OR **********")
if 2 < 5 and 3>2:
    print("ambas son verdaderas")

if 2 > 5 and 3>2:
    print("no se muestra si una no es verdaderas")

if 2 > 5 or 3>2:
    print("una es verdadera")

if 2 > 5 or 3<2:
    print("ninguna es verdadera")

