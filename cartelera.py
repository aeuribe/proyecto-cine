import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Cartelera(tk.Toplevel):
    def __init__(self, master, app, style):
        super().__init__(master)
        self.master.withdraw()
        self.title("Cartelera")
        self.geometry("800x600")
        self.after(100, lambda: app.centrar_ventana(self))
        self.configure(bg="#222222")

        self.app = app
        self.style = style

        self.peliculas = [
            {"titulo": "Kung Fu Panda 4 (ESP)", "imagen": "imagenes/kung_fu_panda_4.jpg", "genero": "Acción/Comedia", "duracion": "1h 45min", "sinopsis": "Po debe enfrentar un nuevo desafío cuando un villano llamado El pavo real amenaza con robar el chi de todos los maestros de kung fu."},
            {"titulo": "Bufón (ESP)", "imagen": "imagenes/bufon.jpg", "genero": "Drama/Crimen", "duracion": "2h 12min", "sinopsis": "Arthur Fleck es un hombre ignorado por la sociedad que encuentra su camino como el criminal y payaso psicópata Joker."},
            {"titulo": "Amigos Imaginarios (ESP)", "imagen": "imagenes/amigos_imaginarios.jpg", "genero": "Fantasía/Aventura", "duracion": "1h 50min", "sinopsis": "Un niño solitario se hace amigo de un dragón imaginario, pero pronto descubre que no es tan imaginario como pensaba."}
        ]  # Ahora es un atributo de instancia

        # Configurar grid (3 filas)
        self.grid_rowconfigure(0, weight=0)  # Fila para el título
        self.grid_rowconfigure(1, weight=0)  # Fila para el mensaje
        self.grid_rowconfigure(2, weight=1)  # Fila para las películas (expandible)
        self.grid_rowconfigure(3, weight=0)  # Fila para el botón "Volver"
        for i, pelicula in enumerate(self.peliculas):
            self.grid_columnconfigure(i, weight=1)

        # Crear título de la cartelera
        titulo_frame = ttk.Frame(self)  # Frame contenedor para el título
        titulo_frame.grid(row=0, column=0, columnspan=len(self.peliculas), pady=(20, 10), sticky="ew")
        titulo_cartelera = ttk.Label(titulo_frame, text="Cartelera", font=("LEMON MILK", 24, "bold"))
        titulo_cartelera.pack(anchor="center")  # Centrado horizontal en el frame


        # Crear mensaje de la cartelera
        mensaje_frame = ttk.Frame(self)  # Frame contenedor para el mensaje
        mensaje_frame.grid(row=1, column=0, columnspan=len(self.peliculas), pady=(20, 10), sticky="ew")
        mensaje_cartelera = ttk.Label(mensaje_frame, text="Selecciona la película que mas te guste!", font=("Roboto Light", 24))
        mensaje_cartelera.pack(anchor="center")  # Centrado horizontal en el frame

        # Crear widgets de películas (modificado)
        for i, pelicula in enumerate(self.peliculas):
            imagen = Image.open(pelicula["imagen"])
            imagen = imagen.resize((200, 300), Image.LANCZOS)
            imagen_tk = ImageTk.PhotoImage(imagen)

            boton_pelicula = ttk.Button(self, image=imagen_tk, command=lambda p=pelicula: self.app.seleccionar_pelicula(p))
            boton_pelicula.image = imagen_tk
            boton_pelicula.grid(row=2, column=i, padx=10, pady=10, sticky="nsew")

            label_nombre = ttk.Label(self, text=pelicula["titulo"], font=("Roboto Light", 14))
            label_nombre.grid(row=3, column=i, pady=(0, 10))

        # Crear botón "Volver al Menú"
        ttk.Button(self, text="Volver al Menú", command=self.app.show_menu).grid(row=4, column=0, columnspan=len(self.peliculas), pady=20)


    def configurar_grid_cartelera(self, num_peliculas):
        self.grid_rowconfigure(0, weight=1)
        for i in range(num_peliculas):
            self.grid_columnconfigure(i, weight=1)

    def crear_widget_pelicula_con_boton(self, i, nombre, ruta_imagen):
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((200, 300), Image.LANCZOS)
        imagen_tk = ImageTk.PhotoImage(imagen)

        boton_pelicula = ttk.Button(self, image=imagen_tk, command=lambda n=nombre: self.app.seleccionar_pelicula(n))
        boton_pelicula.image = imagen_tk
        boton_pelicula.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")

        label_nombre = ttk.Label(self, text=nombre, font=("Helvetica", 14))
        label_nombre.grid(row=1, column=i, pady=(0, 10))  # Debajo del botón

    def crear_boton_volver(self):
        ttk.Button(self, text="Volver al Menú", command=self.app.show_menu).grid(row=2, column=0, columnspan=3, pady=20)
