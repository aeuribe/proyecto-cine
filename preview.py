import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class PreviewPelicula(tk.Toplevel):
    def __init__(self, master, pelicula, style, app):
        super().__init__(master)
        self.app = app
        self.pelicula = pelicula
        self.configure(bg="#222222")

        self.title(f"Vista Previa: {pelicula['titulo']}")
        self.style = style


        self.style.configure("Preview.TLabel", font=("Helvetica", 14), wraplength=400, background="#222222", foreground="#EEEEEE")
        self.style.configure("TButton", font=("Helvetica", 16, "bold"), background="#333333", foreground="#800020")
        
        self.minsize(800, 600)

        # Obtener el tamaño de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        ancho_ventana = int(screen_width * 0.5)
        alto_ventana = int(screen_height * 0.75)
        
        # Centrar la ventana en la pantalla
        x_pos = (screen_width - ancho_ventana) // 2
        y_pos = (screen_height - alto_ventana) // 2
        self.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

        imagen_path = pelicula["imagen"]
        imagen = Image.open(imagen_path)
        imagen.thumbnail((ancho_ventana - 40, int(alto_ventana * 0.6)))  # No distorsionar la imagen, solo ajustar su tamaño
        photo = ImageTk.PhotoImage(imagen)
        label_imagen = ttk.Label(self, image=photo, style="Preview.TLabel")
        label_imagen.image = photo
        label_imagen.pack(pady=10)

        ttk.Label(self, text=f"Título: {pelicula['titulo']}", style="Preview.TLabel").pack(pady=5)
        ttk.Label(self, text=f"Género: {pelicula['genero']}", style="Preview.TLabel").pack(pady=5)
        ttk.Label(self, text=f"Duración: {pelicula['duracion']}", style="Preview.TLabel").pack(pady=5)

        ttk.Button(self, text="Reservar", command=self.master.mostrar_asientos_disponibles, style="TButton").pack(side="left", padx=5, pady=10)
        ttk.Button(self, text="Cerrar", command=self.withdraw, style="TButton").pack(side="right", padx=5, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    pelicula = {
        "titulo": "Ejemplo de Película",
        "genero": "Acción",
        "duracion": "120 minutos",
        "sinopsis": "Esta es la sinopsis de la película.",
        "imagen": "ruta/a/imagen.jpg"  # Reemplaza con la ruta real de la imagen
    }
    style = ttk.Style(root)
    app = None  # Aquí deberías pasar la instancia de tu aplicación principal
    preview = PreviewPelicula(root, pelicula, style, app)
    root.mainloop()
