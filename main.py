import tkinter as tk
from tkinter import ttk 
from menu_principal import MenuPrincipal  # Importa la clase MenuPrincipal desde su archivo
from cartelera import Cartelera  # Importa la clase Cartelera desde su archivo
from preview import PreviewPelicula

class CineApp:
    """
    Clase principal que controla la aplicación del cine.
    """
    def __init__(self, master):
        """
        Inicializa la aplicación.

        Args:
            master: La ventana raíz de Tkinter.
        """
        self.master = master
        self.style = ttk.Style()  # Crea un objeto de estilo para personalizar los widgets
        self.style.theme_use("clam")  # Usa el tema "clam"
        self.style.configure(".", background="#222222", foreground="#EEEEEE", font=("Helvetica", 12))  # Configura el estilo base
        self.style.configure("TButton", background="#333333", foreground="#FF0000")  # Configura el estilo de los botones
        self.style.map("TButton", background=[("active", "#550000")])  # Cambia el color de fondo al pasar el mouse sobre un botón
        

        # Crea una instancia de la ventana del menú principal
        #self.menu_principal = MenuPrincipal(self.master, self, self.style)
        self.cartelera = None  # Inicialmente, no hay ventana de cartelera abierta
        self.preview_pelicula = None

    def show_cartelera(self):
        self.menu_principal.destroy()
        if self.cartelera is None:
            self.cartelera = Cartelera(self.master, self, self.style)
        else:
            self.cartelera.deiconify()
        self.centrar_ventana(self.cartelera)  # Centrar la cartelera

    def show_menu(self):
        if self.cartelera is not None:  # Si la cartelera está abierta
            self.cartelera.destroy()  # Cierra la ventana de la cartelera
            self.cartelera = None  # Establece la cartelera a None para indicar que está cerrada

        self.menu_principal = MenuPrincipal(self.master, self, self.style)  # Recrear el menú principal
        self.centrar_ventana(self.menu_principal)  # Centrar el menú principal
        self.menu_principal.deiconify()  # Trae al frente la ventana del menú principal

    def seleccionar_pelicula(self, pelicula):
        self.preview_pelicula = PreviewPelicula(self.master, pelicula, self.style, self)
        self.preview_pelicula.deiconify() 

    def centrar_ventana(self, ventana):
        """
        Centra una ventana en la pantalla.

        Args:
            ventana: La ventana que se quiere centrar.
        """
        ventana.update_idletasks()
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()
        window_width = ventana.winfo_width()
        window_height = ventana.winfo_height()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        ventana.geometry(f"+{x}+{y}")


if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana raíz de Tkinter
    app = CineApp(root)  # Crea una instancia de la aplicación CineApp
    root.withdraw()  # Ocultar la ventana raíz (opcional, si quieres que el menú principal sea la primera ventana visible)
    root.after(100, app.show_menu) 
    root.mainloop()  # Inicia el bucle de eventos de Tkinter para que la interfaz gráfica responda a eventos
