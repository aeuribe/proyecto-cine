import tkinter as tk
from tkinter import messagebox
import dataBase as db

class AsientosDisponibles(tk.Toplevel):
    def __init__(self, master, pelicula, modo):
        super().__init__(master)
        self.pelicula = pelicula
        self.modo = modo
        self.title("Asientos Disponibles")
        self.geometry("800x600")  # Tamaño inicial
        self.configure(bg="#222222")
        self.asientos_seleccionados = []

        # Obtener los asientos reservados desde la base de datos
        reservados = db.obtenerAsientosReservados(self.pelicula['id_pelicula'])
        self.asientos_reservados = [(int(fila), int(columna)) for fila, columna in reservados]

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

                asiento_actual = (i + 1, j + 1)
                boolean = asiento_actual in self.asientos_reservados

                boton_asiento = tk.Button(
                    self.asientos_frame,
                    text=f"{i+1}-{j+1}",
                    command=lambda row=i, col=j: self.seleccionar_asiento(row, col),
                    bg="#FF0000" if boolean else "#CCCCCC",
                    fg="black" if boolean else "green",
                    font=("Helvetica", 16, "bold"),
                    bd=0,
                    relief=tk.FLAT
                )
                
                boton_asiento.grid(row=i+1, column=j+1, padx=5, pady=5, sticky="nsew")
                fila.append(boton_asiento)
            self.asientos.append(fila)

        # Frame para los botones "Cerrar" y "Guardar" / "Cancelar asiento"
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

        if self.modo == 1:
            # Botón "Guardar"
            boton_guardar = tk.Button(
                botones_frame,
                text="Guardar",
                command=self.guardar_asientos,
                bg="#333333",
                fg="white",
                font=("Helvetica", 16, "bold"),
                bd=0,
                relief=tk.FLAT
            )
            boton_guardar.pack(side=tk.LEFT, padx=10)
        else:
            # Botón "Cancelar asiento"
            boton_cancelar = tk.Button(
                botones_frame,
                text="Cancelar asiento",
                command=self.cancelar_asientos,
                bg="#333333",
                fg="white",
                font=("Helvetica", 16, "bold"),
                bd=0,
                relief=tk.FLAT
            )
            boton_cancelar.pack(side=tk.LEFT, padx=10)

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
        if boton_seleccionado.cget("bg") == "#00FF00":
            boton_seleccionado.configure(bg="#CCCCCC", fg="green")
            self.asientos_seleccionados.remove((fila + 1, columna + 1))
        else:
            boton_seleccionado.configure(bg="#00FF00", fg="black")
            self.asientos_seleccionados.append((fila + 1, columna + 1))
        print(f"Seleccionaste el asiento: {fila + 1}-{columna + 1}")
        print(f"Asientos seleccionados: {self.asientos_seleccionados}")

    def guardar_asientos(self):
        print(f"Asientos seleccionados para guardar: {self.asientos_seleccionados}")
        print(f"Id de la pelicula: {self.pelicula['id_pelicula']}")

        exito = True

        for fila, columna in self.asientos_seleccionados:
            print(f"fila: {fila}, columna: {columna}")
            try:
                butaca = db.reservaButaca(fila, columna, True, self.pelicula['id_pelicula'])
                print(f"Asiento {fila}-{columna} guardado correctamente")
            except Exception as e:
                print(f"Error al guardar el asiento {fila}-{columna}: {e}")
                exito = False
                
        if exito:
            messagebox.showinfo("Éxito", "Asientos guardados exitosamente")
            self.withdraw()
        else:
            messagebox.showerror("Error", "Hubo un error al guardar algunos asientos")


    def cancelar_asientos(self):
        print(f"Asientos seleccionados para cancelar: {self.asientos_seleccionados}")
        print(f"Id de la pelicula: {self.pelicula['id_pelicula']}")

        exito = True

        for fila, columna in self.asientos_seleccionados:
            print(f"fila: {fila}, columna: {columna}")
            try:
                db.cancelarButaca(fila, columna, self.pelicula['id_pelicula'])
                print(f"Asiento {fila}-{columna} cancelado correctamente")
            except Exception as e:
                print(f"Error al cancelar el asiento {fila}-{columna}: {e}")
                exito = False
                
        if exito:
            messagebox.showinfo("Éxito", "Asientos cancelados exitosamente")
            self.withdraw()
        else:
            messagebox.showerror("Error", "Hubo un error al cancelar algunos asientos")



if __name__ == "__main__":
    root = tk.Tk()
    app = AsientosDisponibles(root, pelicula={'id_pelicula': 1, 'titulo': 'Kung Fu Panda 4'}, modo=2)
    app.mainloop()
