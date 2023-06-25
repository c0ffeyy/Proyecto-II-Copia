import sqlite3 # Importamos el módulo SQLite3 para la base de datos.

class ConexionDB: # Clase que establece una conexión a la base de datos SQLite
    def __init__(self):
        # Atributos:
        
        self.base_datos = "database/peliculas.db" # Variable que guarda la ruta al archivo de la base de datos SQLite

        self.conexion = sqlite3.connect(self.base_datos) # Objeto que representa la conexión a la base de datos
        
        self.cursor = self.conexion.cursor() # Objeto que permite ejecutar consultas SQL en la base de datos

    # Método que cierra la conexión a la base de datos y guarda los cambios realizados:
    def cerrar(self):
        self.conexion.commit() 
        self.conexion.close()