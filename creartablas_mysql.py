import pymysql

conn = pymysql.connect(host="127.0.0.1",user="root",passwd="", db="datos")
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS subsidios('ID INT PRIMARY KEY AUTO_INCREMENT,nombre_apellido VARCHAR(30),dni VARCHAR(8),fecha_nacimiento DATE,monto DOUBLE)')
conn.close()
