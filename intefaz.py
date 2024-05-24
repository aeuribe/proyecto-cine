import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CineApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Menú de Cine")
        self.master.geometry("800x600")
        self.master.configure(bg="#222222")
        self.centrar_ventana(self.master)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(".", background="#222222", foreground="#EEEEEE", font=("Helvetica", 12))
        self.style.configure("TButton", background="#333333", foreground="#FF0000")
        self.style.map("TButton", background=[("active", "#550000")])

        self.create_widgets()

    def create_widgets(self):
        title_label = ttk.Label(self.master, text="Menú de Cine", font=("LEMON MILK", 32, "bold"))
        title_label.pack(pady=30)

        self.menu_frame = ttk.Frame(self.master)
        self.menu_frame.pack(padx=50, pady=20)
        self.cartelera_window = None

        options = ["Cartelera y Reserva", "Próximos Estrenos", "Cancelar el Asiento", "Factura del Cliente", "Contacto"]

        for option in options:
            button = ttk.Button(self.menu_frame, text=option, command=lambda o=option: self.button_click(o))
            button.pack(fill=tk.X, pady=10)
            self.style.configure("TButton", font=("Helvetica", 16, "bold")) 
        footer_label = ttk.Label(self.master, text="© 2024 Cine Ejemplo", font=("Helvetica", 10))
        footer_label.pack(side=tk.BOTTOM, pady=10)
    

    def button_click(self, option):
        if option == "Cartelera y Reserva":
            self.show_cartelera()


    def show_cartelera(self):
        self.master.withdraw()    
        self.cartelera_window = tk.Toplevel(self.master)
        self.cartelera_window.title("Cartelera")
        self.cartelera_window.geometry("800x600")
        self.cartelera_window.after(100, lambda: self.centrar_ventana(self.cartelera_window)) 
        self.cartelera_window.configure(bg="#222222")
        

        # Cargar y redimensionar imágenes (reemplaza con tus imágenes)
        peliculas = [
            ("Kung Fu Panda 4 (ESP)", "imagenes/kung_fu_panda_4.jpg"),
            ("Bufón (ESP)", "imagenes/bufon.jpg"),
            ("Amigos Imaginarios (ESP)", "imagenes/amigos_imaginarios.jpg"),
        ]
        # Configurar grid para centrar los botones
        self.cartelera_window.grid_rowconfigure(0, weight=1)  # Fila expandible
        for i in range(len(peliculas)):
            self.cartelera_window.grid_columnconfigure(i, weight=1)  # Columnas expandibles

        for i, (nombre, ruta_imagen) in enumerate(peliculas):
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((200, 300), Image.LANCZOS)
            imagen_tk = ImageTk.PhotoImage(imagen)

            boton_pelicula = ttk.Button(self.cartelera_window, image=imagen_tk, command=lambda n=nombre: self.seleccionar_pelicula(n))
            boton_pelicula.image = imagen_tk
            boton_pelicula.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")  # Centrar en cada columna

            label_nombre = ttk.Label(self.cartelera_window, text=nombre, font=("Helvetica", 14))
            label_nombre.grid(row=1, column=i, pady=(0, 10))  # Debajo del botón

        ttk.Button(self.cartelera_window, text="Volver al Menú", command=self.show_menu).pack(pady=20)  # Cambiamos cartelera_frame por cartelera_window


        for nombre, ruta_imagen in peliculas:
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((200, 300), Image.LANCZOS)  # Ajusta el tamaño según tus necesidades
            imagen_tk = ImageTk.PhotoImage(imagen)

            frame = ttk.Frame(self.cartelera_window)
            frame.pack(side=tk.LEFT, padx=10, pady=10)

            label_imagen = ttk.Label(frame, image=imagen_tk)
            label_imagen.image = imagen_tk  # Mantener referencia
            label_imagen.pack()

            label_nombre = ttk.Label(frame, text=nombre, font=("Helvetica", 14))
            label_nombre.pack()

    def show_menu(self):
        if self.cartelera_window is not None:
            self.cartelera_window.destroy()  # Cerrar la ventana de cartelera
        self.cartelera_window = None  # Reiniciar cartelera_window a None
        self.master.deiconify()
        #self.menu_frame.pack(padx=50, pady=20)  # Mostrar el menú

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()
        window_width = ventana.winfo_width()
        window_height = ventana.winfo_height()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        ventana.geometry(f"+{x}+{y}")
if __name__ == "__main__":
    root = tk.Tk()
    app = CineApp(root)
    root.mainloop()

