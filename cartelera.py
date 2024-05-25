import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Cartelera(tk.Toplevel):
    def __init__(self, master, app, style):
        super().__init__(master)
        self.master = master
        self.app = app
        self.style = style
        self.title("Cartelera")
        self.geometry("800x600")
        self.configure(bg="#222222")

        self.peliculas = [
            {"titulo": "Kung Fu Panda 4 (ESP)", "imagen": "imagenes/kung_fu_panda_4.jpg", "genero": "Acción/Comedia", "duracion": "1h 45min", "sinopsis": "Po debe enfrentar un nuevo desafío cuando un villano llamado El pavo real amenaza con robar el chi de todos los maestros de kung fu."},
            {"titulo": "Bufón (ESP)", "imagen": "imagenes/bufon.jpg", "genero": "Drama/Crimen", "duracion": "2h 12min", "sinopsis": "Arthur Fleck es un hombre ignorado por la sociedad que encuentra su camino como el criminal y payaso psicópata Joker."},
            {"titulo": "Amigos Imaginarios (ESP)", "imagen": "imagenes/amigos_imaginarios.jpg", "genero": "Fantasía/Aventura", "duracion": "1h 50min", "sinopsis": "Un niño solitario se hace amigo de un dragón imaginario, pero pronto descubre que no es tan imaginario como pensaba."}
        ]

        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        for i in range(4):
            self.grid_rowconfigure(i, weight=1)

        for i in range(len(self.peliculas)):
            self.grid_columnconfigure(i, weight=1)

        titulo_frame = ttk.Frame(self, style="TFrame")
        titulo_frame.grid(row=0, column=0, columnspan=len(self.peliculas), pady=(20, 10), sticky="ew")
        titulo_cartelera = ttk.Label(titulo_frame, text="Cartelera", font=("LEMON MILK", 24, "bold"))
        titulo_cartelera.pack(anchor="center")

        mensaje_frame = ttk.Frame(self, style="TFrame")
        mensaje_frame.grid(row=1, column=0, columnspan=len(self.peliculas), pady=(20, 10), sticky="ew")
        mensaje_cartelera = ttk.Label(mensaje_frame, text="Selecciona la película que más te guste!", font=("Roboto Light", 24))
        mensaje_cartelera.pack(anchor="center")

        for i, pelicula in enumerate(self.peliculas):
            imagen = Image.open(pelicula["imagen"])
            imagen = imagen.resize((200, 300), Image.LANCZOS)
            imagen_tk = ImageTk.PhotoImage(imagen)

            boton_pelicula = ttk.Button(self, image=imagen_tk, command=lambda p=pelicula: self.app.seleccionar_pelicula(p))
            boton_pelicula.image = imagen_tk
            boton_pelicula.grid(row=2, column=i, padx=10, pady=10, sticky="nsew")

            label_nombre = ttk.Label(self, text=pelicula["titulo"], font=("Roboto Light", 14))
            label_nombre.grid(row=3, column=i, pady=(0, 10))

        self.crear_boton_volver()

    def crear_boton_volver(self):
        ttk.Button(self, text="Volver al Menú", command=self.volver_al_menu).grid(row=4, column=0, columnspan=len(self.peliculas), pady=20)

    def volver_al_menu(self):
        self.destroy()
        self.app.deiconify()
        self.app.open_menu_principal()

    def on_closing(self):
        self.destroy()
        self.app.deiconify()

if __name__ == "__main__":
    app = tk.Tk()
    style = ttk.Style(app)
    style.theme_use("clam")

    app.mainloop()
