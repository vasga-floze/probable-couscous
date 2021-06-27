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
#cursor.execute('select * from usuario')


#INSERTAR DATOS
#cursor.execute('show create table usuario') #consultar script con el que se creo la tabla
sql = 'INSERT INTO usuario(nombre, apellido, edad) VALUES (%s, %s, %s)' #insertar datos
values = ('Carmen', 'Morataya', 56)
cursor.execute(sql, values)


midb.commit() #se compromenten los datos para que puedan ser guardados en la base de datos

print(cursor.rowcount)

#fetchall() DEVUELVE TODAS LAS INSTANCIAS QUE ENCUENTRA
#resultado = cursor.fetchall()

#fetchone() DEVUELVE EL PRIMER REGISTRO QUE ENCUENTRA
#resultado = cursor.fetchone()

#print(resultado)