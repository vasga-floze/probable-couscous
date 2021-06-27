import mysql.connector #libreria que permite la conexion con mysql

#la libreria permite la variable mysql con el metodo connector.connect
midb = mysql.connector.connect(
    #recibe cuatro argumentos
    host='localhost',
    user='root',
    password='root21', 
    database='pruebauno' #indicar el nombre de la bd
) #este metodo devuelve la instancia

#con el metodo anterior obtenemos el cursor
#un cursor es un objeto que permite interactuar con la db mediante lenguaje SQL
cursor = midb.cursor()


#LISTAR DATOS
#esta consulta indica que se va a mostrar todos los registros en el modelo Usuario
# cursor.execute('select * from usuario')
# resultado = cursor.fetchall() #fetchall() DEVUELVE TODAS LAS INSTANCIAS QUE ENCUENTRA
# print(resultado)

#resultado = cursor.fetchone() #fetchone() DEVUELVE EL PRIMER REGISTRO QUE ENCUENTRA


#INSERTAR DATOS
#cursor.execute('show create table usuario') #consultar script con el que se creo la tabla
# sql = 'INSERT INTO usuario(nombre, apellido, edad) VALUES (%s, %s, %s)' #insertar datos
# values = ('Carmen', 'Morataya', 56)
# cursor.execute(sql, values)


# midb.commit() #se compromenten los datos para que puedan ser guardados en la base de datos

# print(cursor.rowcount)

# #ACTUALIZAR DATOS
sql = 'UPDATE usuario SET nombre = %s WHERE id = %s'
values = ('Victoria', 6)
cursor.execute(sql, values)

midb.commit() #compromete datos para que se ejecute la consulte