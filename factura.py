import tkinter as tk
from tkinter import messagebox
import dataBase as db

class FacturaWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Factura")
        self.geometry("400x500")
        self.configure(bg="#222222")

        self.metodo_pago = tk.StringVar(value="")

        # Intentar obtener las películas y asientos
        self.peliculas_asientos = db.obtener_peliculas_y_asientos()
        if self.peliculas_asientos is None:
            self.peliculas_asientos = []
        
        self.costo_total = len(self.peliculas_asientos) * 74  # Asumiendo que cada asiento cuesta 74 Bs

        print()
        self.create_widgets()

    def create_widgets(self):
        # Título
        title = tk.Label(self, text="FACTURA", font=("Helvetica", 20, "bold"), bg="#222222", fg="white")
        title.pack(pady=10)

        # Información de las películas y asientos comprados
        info_text = "SALA 1\n"
        for id_pelicula, titulo, fila, columna in self.peliculas_asientos:
            info_text += f"({titulo}) - Asiento: {fila},{columna}\n"
        info_text += f"\nEl costo total por {len(self.peliculas_asientos)} asientos es de: {self.costo_total} Bs"
        info_label = tk.Label(self, text=info_text, font=("Helvetica", 12), bg="#222222", fg="white", justify=tk.LEFT)
        info_label.pack(pady=10)

        # Método de pago
        metodo_pago_label = tk.Label(self, text="METODO DE PAGO", font=("Helvetica", 16, "bold"), bg="#222222", fg="white")
        metodo_pago_label.pack(pady=10)

        # Opciones de método de pago
        metodos_pago = ["PAGO MOVIL", "PUNTO DE VENTA", "EFECTIVO", "REGRESAR AL MENU"]
        for metodo in metodos_pago:
            radio_button = tk.Radiobutton(
                self, 
                text=metodo, 
                variable=self.metodo_pago, 
                value=metodo, 
                font=("Helvetica", 12),
                bg="#222222", 
                fg="white", 
                selectcolor="#444444"
            )
            radio_button.pack(anchor=tk.W, padx=20, pady=5)

        # Botón de confirmar
        confirmar_button = tk.Button(
            self, 
            text="Confirmar", 
            command=self.confirmar_pago, 
            font=("Helvetica", 14, "bold"),
            bg="#333333", 
            fg="white", 
            bd=0, 
            relief=tk.FLAT
        )
        confirmar_button.pack(pady=20)

    def confirmar_pago(self):
        metodo_seleccionado = self.metodo_pago.get()
        if metodo_seleccionado:
            if metodo_seleccionado == "REGRESAR AL MENU":
                messagebox.showinfo("Información", "Regresando al menú principal.")
                self.destroy()
            else:
                messagebox.showinfo("Confirmación", f"Compra procesada!")
                # Aquí puedes agregar la lógica para procesar el pago según el método seleccionado
                self.master.open_menu_principal()
                self.destroy()
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un método de pago")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    factura_window = FacturaWindow(root)
    factura_window.mainloop()
