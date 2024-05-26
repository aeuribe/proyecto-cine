import tkinter as tk
from tkinter import ttk, messagebox
from menu_principal import MenuPrincipal
from cartelera import Cartelera
from preview import PreviewPelicula
import dataBase as db

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("800x600")
        self.configure(bg="#222222")

        self.style = ttk.Style()
        self.style.configure("TLabel", foreground="white", background="#222222", font=("Helvetica", 16))
        self.style.configure("TEntry", foreground="black", font=("Helvetica", 16))
        self.style.configure("TButton", font=("Helvetica", 16, "bold"), background="#444444", foreground="white")
        self.style.map("TButton", background=[("active", "#666666")], foreground=[("active", "white")])
        self.style.configure("TFrame", background="#222222")

        self.create_widgets()

    def create_widgets(self):
        container = ttk.Frame(self, style="TFrame")
        container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        welcome_label = ttk.Label(container, text="¡Bienvenido al Cine!", style="TLabel", font=("Helvetica", 20, "bold"))
        welcome_label.grid(row=0, columnspan=2, pady=10)

        ttk.Label(container, text="Username:", style="TLabel").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.username_entry = ttk.Entry(container, style="TEntry")
        self.username_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

        ttk.Label(container, text="Password:", style="TLabel").grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.password_entry = ttk.Entry(container, show="*", style="TEntry")
        self.password_entry.grid(row=2, column=1, pady=10, padx=10, sticky="ew")

        ttk.Button(container, text="Login", command=self.login, style="TButton").grid(row=3, columnspan=2, pady=20)
        self.style.configure("TButton", font=("Helvetica", 16, "bold"), background="#444444", foreground="#800020")

        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=3)

    def login(self):
        db.createDataBase()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if db.validarUsers(username, password):
            messagebox.showinfo("Login", "Login successful")
            self.open_menu_principal()
        else:
            messagebox.showerror("Login", "Invalid username or password")

    def open_menu_principal(self):
        self.withdraw()
        menu_principal = MenuPrincipal(self, self.style)
        menu_principal.protocol("WM_DELETE_WINDOW", self.on_closing)

    def show_cartelera(self):
        self.withdraw()
        cartelera = Cartelera(self, self, self.style)
        cartelera.protocol("WM_DELETE_WINDOW", self.on_closing)

    def seleccionar_pelicula(self, pelicula):
        self.preview_pelicula = PreviewPelicula(self, pelicula, self.style, self)
        self.preview_pelicula.deiconify()

    def centrar_ventana(self, ventana):
        ventana.update_idletasks()
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()
        window_width = ventana.winfo_width()
        window_height = ventana.winfo_height()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        ventana.geometry(f"+{x}+{y}")

    def on_closing(self):
        self.destroy()

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
