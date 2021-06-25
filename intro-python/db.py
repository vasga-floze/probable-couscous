import mysql.connector #libreria que permite la conexion con mysql

#la libreria permite la variable mysql con el metodo connector.connect
midb = mysql.connector.connect(
    #recibe cuatro argumentos
    host='localhost',
    user='user_name',
    password='password', 
    database='name_database' #indicar el nombre de la bd
) #este metodo devuelve la instancia

#con el metodo anterior obtenemos el cursor
#un cursor es un objeto que permite interactuar con la db mediante lenguaje SQL
cursor = midb.cursor()

cursor.execute('select * from usuario')

resultado = cursor.fetchall()

print(resultado)