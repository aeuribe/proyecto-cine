import sqlite3 as sql
import os

def eliminarBaseDatos():
    if os.path.exists('cine.db'):
        os.remove('cine.db')
    else:
        print("La base de datos no existe")

def createDataBase():
    conn = sql.connect('cine.db') # Crea la conexion a la base de datos
    conn.commit()
    return conn

def createTable():
    conn = createDataBase()
    cursor = conn.cursor()

    cursor.execute(
        ''' CREATE TABLE user( 
          id_user INTEGER PRIMARY KEY AUTOINCREMENT, 
          username TEXT,
          password TEXT
        )''')
    
    cursor.execute(
        ''' CREATE TABLE pelicula(  
          id_pelicula INTEGER PRIMARY KEY AUTOINCREMENT,
          titulo TEXT,
          genero TEXT,
          duracion TEXT,
          sinopsis TEXT,
          imagen TEXT,
          sala TEXT
        )''')
    
    cursor.execute(
        ''' CREATE TABLE butaca(
          id_butaca INTEGER PRIMARY KEY AUTOINCREMENT,
          fila TEXT,
          columna TEXT,
          reserva BOOLEAN,
          id_pelicula INTEGER,
          FOREIGN KEY(id_pelicula) REFERENCES pelicula(id_pelicula)
        )''')
    
    cursor.execute(
        ''' CREATE TABLE factura(
          id_factura INTEGER PRIMARY KEY AUTOINCREMENT,
          total REAL,
          pagada BOOLEAN,
          metodo_pago TEXT,
          id_user INTEGER,
          id_butaca INTEGER,
          FOREIGN KEY(id_user) REFERENCES user(id_user),
          FOREIGN KEY(id_butaca) REFERENCES butaca(id_butaca)
        )''')
    
    conn.commit()
    conn.close()

def insertUser():
    conn = createDataBase()
    cursor = conn.cursor()

    cursor.execute(
        ''' INSERT INTO user(username, password) VALUES('user1@gmail.com','user1')'''
        )

    cursor.execute(
        ''' INSERT INTO user(username, password) VALUES('user2','123')'''
        )
    
    conn.commit()
    conn.close()

def validarUsers(username, password):
    conn = createDataBase()
    cursor = conn.cursor()

    cursor.execute(
        ''' SELECT id_user FROM user where username = ? and password = ?''', (username,password)
        )

    users = cursor.fetchall()
    if users:
        conn.close()
        return users[0][0]
    else:
        conn.close()
        return False
    
def insertarPelicula():
    conn = createDataBase()
    cursor = conn.cursor()

    cursor.executemany(
        ''' INSERT INTO pelicula(titulo, genero, duracion, sinopsis,imagen, sala) VALUES(?,?,?,?,?,?)''',
        [
            ('Kung fu panda 4 (esp)', 'Acción/comedia', '1:45m', 'Sigue a Po en sus aventuras por la antigua china, donde su amor por el kung fu solo es superado por su amor por la comida.','imagenes/kung_fu_panda_4.jpg', 'Sala 1'),

            ('El bufón (esp)', 'Fantasia', '2h 39m', 'Un malevolo ser conocido como el Bufon aterroriza a los habitantes de un peque�o pueblo en la noche de halloween, incluyendo a dos hermanas separadas que deben unirse paraencontrar la manera de derrotar esta entidad.', 'imagenes/bufon.jpg','Sala 2'),

            ('Amigos imaginarios (esp)', 'Drama', '2h 55m', 'Sigue a una nina que pasa por una experiencia dificil y entonces empieza a ver a los amigos imaginarios de todo el mundo que se han quedado atras cuando sus amigos de la vida real han crecido', 'imagenes/amigos_imaginarios.jpg','Sala 3')
        ]
    )
    
    conn.commit()
    conn.close()

def listarPelicular():
    conn = createDataBase()
    conn.row_factory = sql.Row  # Esto hará que la consulta devuelva un diccionario
    cursor = conn.cursor()
    cursor.execute(
        ''' SELECT * FROM pelicula '''
        )
    peliculas = cursor.fetchall()
    conn.close()
    lista_peliculas = [dict(pelicula) for pelicula in peliculas]
    return lista_peliculas

def reservaButaca(fila, columna, reserva, id_pelicula):
    conn = createDataBase()
    cursor = conn.cursor()

    cursor.execute(
        ''' INSERT INTO butaca(fila, columna, reserva, id_pelicula) VALUES(?,?,?,?)''', (fila, columna, reserva, id_pelicula)
        )
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    #eliminarBaseDatos()
    #createTable()
    #insertUser()
    #insertarPelicula()
    #listarPelicular()
    pass