import tkinter as tk
from tkinter import ttk 
from PIL import Image, ImageTk 


class PreviewPelicula(tk.Toplevel):
    def __init__(self, master, pelicula, style, app):  # Añadir app como argumento
        super().__init__(master)
        self.app = app  # Almacenar referencia a la aplicación para centrar ventana

        self.title(f"Vista Previa: {pelicula['titulo']}")
        self.style = style

        # Configurar estilo de la ventana (similar a MenuPrincipal)
        self.configure(background=self.style.lookup(".", "background"))
        self.style.configure("Preview.TLabel", font=("Helvetica", 14), wraplength=400, background="#222222", foreground="#EEEEEE")
        self.style.configure("TButton", font=("Helvetica", 16, "bold"), background="#333333", foreground="#FF0000")
    
        # Dimensiones de la ventana
        ancho_ventana = 500
        alto_ventana = 600
        self.geometry(f"{ancho_ventana}x{alto_ventana}")

        # Centrar la ventana después de establecer las dimensiones (usando el método de CineApp)
        self.after(100, lambda: self.app.centrar_ventana(self))  

        # Cargar y mostrar la imagen de la película (redimensionada)
        imagen_path = pelicula["imagen"]
        try:
            imagen = Image.open(imagen_path)
            imagen = imagen.resize((ancho_ventana - 40, 400), Image.LANCZOS) 
            photo = ImageTk.PhotoImage(imagen)
            label_imagen = ttk.Label(self, image=photo, style="Preview.TLabel")
            label_imagen.image = photo  
            label_imagen.pack(pady=10)
        except FileNotFoundError:
            ttk.Label(self, text="Imagen no encontrada", style="Preview.TLabel").pack(pady=10)

        # Mostrar detalles de la película
        ttk.Label(self, text=f"Título: {pelicula['titulo']}", style="Preview.TLabel").pack()
        ttk.Label(self, text=f"Género: {pelicula['genero']}", style="Preview.TLabel").pack()
        ttk.Label(self, text=f"Duración: {pelicula['duracion']}", style="Preview.TLabel").pack()

        # Sinopsis con scrollbar si es necesario
        frame_sinopsis = ttk.Frame(self)
        frame_sinopsis.pack(pady=10, fill="both", expand=True)  

        canvas_sinopsis = tk.Canvas(frame_sinopsis)
        canvas_sinopsis.pack(side="left", fill="both", expand=True)

        scrollbar_sinopsis = ttk.Scrollbar(frame_sinopsis, orient="vertical", command=canvas_sinopsis.yview)
        scrollbar_sinopsis.pack(side="right", fill="y")

        canvas_sinopsis.configure(yscrollcommand=scrollbar_sinopsis.set)
        canvas_sinopsis.bind("<Configure>", lambda e: canvas_sinopsis.configure(scrollregion=canvas_sinopsis.bbox("all")))

        frame_interno_sinopsis = ttk.Frame(canvas_sinopsis)
        canvas_sinopsis.create_window((0, 0), window=frame_interno_sinopsis, anchor="nw")

        label_sinopsis = ttk.Label(frame_interno_sinopsis, text=f"Sinopsis: {pelicula['sinopsis']}", style="Preview.TLabel", wraplength=ancho_ventana - 60)
        label_sinopsis.pack(pady=10)

        # Crear botón "Volver al Menú"
        ttk.Button(self, text="Volver al Menú", command=self.app.show_menu).grid(row=4, column=0, columnspan=len(self.peliculas), pady=20)
