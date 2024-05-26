import sqlite3 as sql

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
          nombre TEXT,
          genero TEXT,
          duracion TEXT,
          descripcioN TEXT
        )''')
    
    cursor.execute(
        ''' CREATE TABLE sala( 
          id_sala INTEGER PRIMARY KEY AUTOINCREMENT,
          nombre TEXT,
          id_pelicula INTEGER,
          FOREIGN KEY (id_pelicula) REFERENCES pelicula(id_pelicula)
        )''')
    
    cursor.execute(
        ''' CREATE TABLE butaca(
          id_butaca INTEGER PRIMARY KEY AUTOINCREMENT,
          fila TEXT,
          columna TEXT,
          reserva BOOLEAN,
          id_sala INTEGER,
          id_user INTEGER,
          FOREIGN KEY(id_user) REFERENCES user(id_user),
          FOREIGN KEY(id_sala) REFERENCES sala(id_sala)
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

if __name__ == '__main__':
    print(validarUsers('user2', '123'))