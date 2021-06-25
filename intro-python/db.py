import mysql.connector #libreria que permite la conexion con mysql

#la libreria permite la variable mysql con el metodo connector.connect
midb = mysql.connector.connect(
    #recibe cuatro argumentos
    host='localhost',
    user='root',
    password='root', 
    database='pruebauno' #indicar el nombre de la bd
) #este metodo devuelve la instancia

#con el metodo anterior obtenemos el cursor
#un cursor es un objeto que permite interactuar con la db mediante lenguaje SQL
cursor = midb.cursor()

#esta consulta indica que se va a mostrar todos los registros en el modelo Usuario
cursor.execute('select * from usuario')

#fetchall() devuelve todas las instancias que encuentra
resultado = cursor.fetchall()

#fetchone() devuelve la primera que encuentra
#resultado = cursor.fetchone()

print(resultado)