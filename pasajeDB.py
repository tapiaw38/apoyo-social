import sqlite3
try:
	bd = sqlite3.connect("pasajes.db")
	cursor = bd.cursor()
	tablas = [
		"""
			CREATE TABLE IF NOT EXISTS pasajes(
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre_apellido VARCHAR NOT NULL,
				dni VARCHAR NOT NULL,
				fecha_nacimiento DATE NOT NULL,
				monto REAL NOT NULL,
				motivo VARCHAR NOT NULL,
				fecha_solicitud DATE NOT NULL,
				destino VARCHAR NOT NULL
			);
		"""
	]
	for tabla in tablas:
		cursor.execute(tabla);
	print("Tablas creadas correctamente")
except sqlite3.OperationalError as error:
	print("Error al abrir:", error)
