#**************LEYENDO****************
"""#leyendo archivos
txt = open('texto.txt')

#leyendo archivo completo
print(txt.read())


#leyendo linea por linea
print(txt.readline())

#leyendo linea por linea en un ciclo
for eachLine in txt:
    print(eachLine)
txt.close() #como buena practica cerrar el archivo """


#*********************ESCRIBIENDO***********************
#Agreganfo una texto al final del doc
""" 
txt = open('texto.txt', 'a') #abrir primero el archivo y asignar el permiso append = 'a' --> agregar al final

txt.write('\n Esta es la linea que agrego nueva') #Escribiendo en archivo

txt.close() #como buena practica cerrar el archivo
 """

#Reescribiendo todo el archivo
"""txt = open('texto.txt', 'w') #asignar permiso write --> sobreescribe el archivo completo

txt.write('\n Esta es la linea que agrego nueva') #Escribiendo en archivo

txt.close() #como buena practica cerrar el archivo
"""
#*********************ELIMINANDO***********************

#primero se necesita importar una libreria que nos proveera los metodos necesarios para eliminar
import os
#eliminando un archivo y validando que exista 
""" 
if os.path.exists('new.txt'):
    os.remove('new.txt')
    print('Archivo eliminado baby')
else:
    print('El archivo no existe baby')
 """
#eliminando una carpeta 
os.rmdir("miCarpeta")