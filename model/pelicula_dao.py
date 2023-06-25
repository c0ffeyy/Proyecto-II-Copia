from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla(): # Función que crea la tabla "peliculas" en la base de datos si no existe
    conexion = ConexionDB()

    sql = """
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    """

    try: # Intento de ejecutar la consulta SQL y mensaje por si lo hace
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Crear Registro"
        mensaje = "Se creó la tabla en la base de datos"
        messagebox.showinfo(titulo, mensaje)
    except: # Excepción por si la tabla ya está creada en la base de datos
        titulo = "Crear Registro"
        mensaje = "La tabla ya está creada"
        messagebox.showwarning(titulo, mensaje)

def borrar_tabla(): # Borra la tabla "peliculas" de la base de datos
    conexion = ConexionDB()

    sql = "DROP TABLE peliculas"

    try: # Intento de ejecutar la consulta SQL y mensaje por si lo hace
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Borrar Registro"
        mensaje = "La tabla de la base de datos se borró con éxito"
        messagebox.showinfo(titulo, mensaje)
    except: # Excepción por si se intenta borrar una tabla, pero no está creada
        titulo = "Borrar Registro"
        mensaje = "No hay tabla para borrar"
        messagebox.showerror(titulo, mensaje)

class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
    
    def __str__(self): # Método que devuelve una representación en cadena de la película.
        return f"Película[{self.nombre}, {self.duracion}, {self.genero}]"

def guardar(pelicula): # Función que guarda una película en la base de datos
    conexion = ConexionDB()

    sql = f"""INSERT INTO peliculas (nombre, duracion, genero)
    VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""

    try: # Intento de ejecutar la consulta SQL
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except: # Excepción por si se intenta guardar un registro, pero no existe la tabla
        titulo = "Conexión al Registro"
        mensaje = "La tabla 'películas' no está creada en la base de datos"
        messagebox.showerror(titulo, mensaje)

def listar(): # Función que btiene una lista de todas las películas almacenadas en la base de datos
    conexion = ConexionDB()

    lista_peliculas = []

    sql = "SELECT * FROM peliculas"

    try: # Intento de ejecutar la consulta SQL y recibimos todas las filas de resultados
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except: # Excepción por si no existe la tabla en la base de datos
        titulo = "Conexión al Registro"
        mensaje = "Crea la tabla en la base de datos"
        messagebox.showerror(titulo, mensaje)

    return lista_peliculas

def editar(pelicula, id_pelicula): # Función que edita los datos de una película en la base de datos
    conexion = ConexionDB()

    sql = f"""UPDATE peliculas
    SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}', genero = '{pelicula.genero}'
    WHERE id_pelicula = {id_pelicula}"""

    try: # Intento de ejecutar la consulta SQL
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except: # Excepción por si hay algún error al editar un registro
        titulo = "Edición de Datos"
        mensaje = "No se ha podido editar este registro."
        messagebox.showerror(titulo, mensaje)

def eliminar(id_pelicula): # Función que elimina una película de la base de datos.
    conexion = ConexionDB()

    sql = f"DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}"

    try: # Intento de ejecutar la consulta SQL
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except: # Excepción por si hay algún error al eliminar un registro
        titulo = "Eliminar Datos"
        mensaje = "No se ha podido eliminar el registro."
        messagebox.showerror(titulo, mensaje)