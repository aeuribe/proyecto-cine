import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class PreviewPelicula(tk.Toplevel):
    def __init__(self, master, pelicula, style, app):
        super().__init__(master)
        self.app = app
        self.pelicula = pelicula

        self.title(f"Vista Previa: {pelicula['titulo']}")
        self.style = style

        self.configure(background=self.style.lookup(".", "background"))
        self.style.configure("Preview.TLabel", font=("Helvetica", 14), wraplength=400, background="#222222", foreground="#EEEEEE")
        self.style.configure("TButton", font=("Helvetica", 16, "bold"), background="#333333", foreground="#FF0000")

        ancho_ventana = 500
        alto_ventana = 600
        self.geometry(f"{ancho_ventana}x{alto_ventana}")

        self.after(100, lambda: self.app.centrar_ventana(self))

        main_frame = ttk.Frame(self)
        main_frame.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        imagen_path = pelicula["imagen"]
        try:
            imagen = Image.open(imagen_path)
            imagen = imagen.resize((ancho_ventana - 40, 400), Image.LANCZOS)
            photo = ImageTk.PhotoImage(imagen)
            label_imagen = ttk.Label(main_frame, image=photo, style="Preview.TLabel")
            label_imagen.image = photo
            label_imagen.grid(row=0, column=0, columnspan=2, pady=10)
        except FileNotFoundError:
            ttk.Label(main_frame, text="Imagen no encontrada", style="Preview.TLabel").grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(main_frame, text=f"Título: {pelicula['titulo']}", style="Preview.TLabel").grid(row=1, column=0, columnspan=2, pady=5)
        ttk.Label(main_frame, text=f"Género: {pelicula['genero']}", style="Preview.TLabel").grid(row=2, column=0, columnspan=2, pady=5)
        ttk.Label(main_frame, text=f"Duración: {pelicula['duracion']}", style="Preview.TLabel").grid(row=3, column=0, columnspan=2, pady=5)

        frame_sinopsis = ttk.Frame(main_frame)
        frame_sinopsis.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")
        main_frame.grid_rowconfigure(4, weight=1)

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

        frame_botones = ttk.Frame(main_frame)
        frame_botones.grid(row=5, column=0, columnspan=2, pady=10)

        ttk.Button(frame_botones, text="Volver al Menú", command=self.withdraw).grid(row=0, column=0, padx=5)
        ttk.Button(frame_botones, text="Comprar", command=self.comprar_pelicula).grid(row=0, column=1, padx=5)

    def comprar_pelicula(self):
        # Aquí puedes definir la funcionalidad que deseas para el botón "Comprar"
        print(f"Comprando la película: {self.pelicula['titulo']}")
