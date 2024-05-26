import tkinter as tk
import dataBase as db

class AsientosDisponibles(tk.Toplevel):
    def __init__(self, master, pelicula):
        super().__init__(master)
        self.pelicula = pelicula
        self.title("Asientos Disponibles")
        self.geometry("800x600")  # Tamaño inicial
        self.configure(bg="#222222")

        self.create_widgets()

    def create_widgets(self):
        self.asientos_frame = tk.Frame(self, bg="#222222")
        self.asientos_frame.pack(fill=tk.BOTH, expand=True)

        self.num_filas = 8
        self.num_columnas = 8

        self.asientos = []

        for i in range(self.num_filas):
            fila = []
            for j in range(self.num_columnas):
                # Agregar etiquetas de fila en el borde izquierdo
                if j == 0:
                    etiqueta_fila = tk.Label(self.asientos_frame, text=f"{i+1}", bg="#222222", fg="white", font=("Helvetica", 16, "bold"))
                    etiqueta_fila.grid(row=i+1, column=0, padx=5, pady=5, sticky="nsew")

                # Agregar etiquetas de columna en el borde superior
                if i == 0:
                    etiqueta_columna = tk.Label(self.asientos_frame, text=f"{j+1}", bg="#222222", fg="white", font=("Helvetica", 16, "bold"))
                    etiqueta_columna.grid(row=0, column=j+1, padx=5, pady=5, sticky="nsew")

                boton_asiento = tk.Button(
                    self.asientos_frame,
                    text=f"{i+1}-{j+1}",
                    command=lambda row=i, col=j: self.seleccionar_asiento(row, col),
                    bg="#CCCCCC",
                    fg="red",
                    font=("Helvetica", 16, "bold"),
                    bd=0,
                    relief=tk.FLAT
                )
                boton_asiento.grid(row=i+1, column=j+1, padx=5, pady=5, sticky="nsew")
                fila.append(boton_asiento)
            self.asientos.append(fila)

        # Frame para los botones "Cerrar" y "Guardar"
        botones_frame = tk.Frame(self, bg="#222222")
        botones_frame.pack(pady=10)

        # Botón "Cerrar"
        boton_cerrar = tk.Button(
            botones_frame,
            text="Cerrar",
            command=self.withdraw,
            bg="#333333",
            fg="white",
            font=("Helvetica", 16, "bold"),
            bd=0,
            relief=tk.FLAT
        )
        boton_cerrar.pack(side=tk.LEFT, padx=10)

        # Botón "Guardar"
        boton_guardar = tk.Button(
            botones_frame,
            text="Guardar",
            command=self.guardar_asientos(self.asientos,2, self.pelicula),
            bg="#333333",
            fg="white",
            font=("Helvetica", 16, "bold"),
            bd=0,
            relief=tk.FLAT
        )
        boton_guardar.pack(side=tk.LEFT, padx=10)

        self.configurar_expansion()

    def configurar_expansion(self):
        for i in range(1, self.num_filas + 1):
            self.asientos_frame.grid_rowconfigure(i, weight=1)
        for j in range(1, self.num_columnas + 1):
            self.asientos_frame.grid_columnconfigure(j, weight=1)

        self.asientos_frame.grid_rowconfigure(self.num_filas + 1, weight=1)
        self.asientos_frame.grid_columnconfigure(self.num_columnas + 1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def seleccionar_asiento(self, fila, columna):
        boton_seleccionado = self.asientos[fila][columna]
        # Comprobar el color de fondo actual del botón
        if boton_seleccionado.cget("bg") == "#00FF00":
            # Si es verde, cambiarlo al color original
            boton_seleccionado.configure(bg="#CCCCCC", fg="red")
        else:
            # Si no es verde, cambiarlo a verde y letras negras
            boton_seleccionado.configure(bg="#00FF00", fg="black")
        print(f"Seleccionaste el asiento: {fila+1}-{columna+1}")
        self.master.logica_guardar(fila+1, columna+1)

    def guardar_asientos(self,fila, columna, pelicula):
        # Aquí puedes definir la funcionalidad que deseas para el botón "Guardar"
        print("fila",fila)
        '''butaca = db.reservaButaca(fila+1, columna+1, True ,pelicula['id_pelicula'])
        if butaca:
            print("Asientos guardados correctamente")
        else:
            print("Error al guardar los asientos")'''

if __name__ == "__main__":
    root = tk.Tk()
    app = AsientosDisponibles(root)
    app.mainloop()
