import tkinter as tk
from tkinter import ttk

class MenuPrincipal(tk.Toplevel):
    def __init__(self, master, style):
        super().__init__(master)
        self.title("Menú de Cine")
        self.geometry("800x600")
        self.configure(bg="#222222")

        self.style = style
        self.master = master  # Guardar una referencia a la instancia de CineApp

        self.create_widgets()

    def button_click(self, option):  # Método button_click movido aquí
        if option == "Cartelera y Reserva":
            self.withdraw()
            self.master.show_cartelera()
        else:
            print(f"Botón '{option}' presionado")

    def create_widgets(self):
        title_label = ttk.Label(self, text="Menú de Cine", font=("LEMON MILK", 32, "bold"))
        title_label.pack(pady=30)

        menu_frame = ttk.Frame(self)
        menu_frame.pack(padx=50, pady=20)

        options = ["Cartelera y Reserva", "Cancelar el Asiento", "Factura del Cliente"]

        for option in options:
            button = ttk.Button(menu_frame, text=option, command=lambda o=option: self.button_click(o))
            button.pack(fill=tk.X, pady=10)
            self.style.configure("TButton", font=("Helvetica", 22, "bold"))

        footer_label = ttk.Label(self, text="© 2024 Cine", font=("Helvetica", 10))
        footer_label.pack(side=tk.BOTTOM, pady=10)

        # Frame para los botones en la parte inferior
        botones_frame = tk.Frame(self, bg="#222222")
        botones_frame.pack(side=tk.BOTTOM, pady=20)

        # Botón "Cerrar"
        boton_cerrar = tk.Button(
            botones_frame,
            text="Cerrar",
            command=self.close_application,
            bg="#333333",
            fg="white",
            font=("Helvetica", 16, "bold"),
            bd=0,
            relief=tk.FLAT
        )
        boton_cerrar.pack(side=tk.LEFT, padx=10)

    def close_application(self):
        self.master.quit()

    def on_closing(self):
        self.destroy()
        self.master.deiconify()

if __name__ == "__main__":
    app = tk.Tk()
    style = ttk.Style(app)
    style.theme_use("clam")

    menu_principal = MenuPrincipal(app, style)
    menu_principal.mainloop()
    app.mainloop()
