import tkinter as tk
from tkinter import simpledialog

class ButtonHandler:
    def __init__(self, show_information, window_instance):
        self.show_information = show_information
        self.window_instance = window_instance  # Guardar la instancia de Windows
        self.create_buttons()

    def create_buttons(self):
        # Botón para obtener todos los registros
        boton_todos = tk.Button(self.window_instance.root, text="Obtener Todos los Registros", command=self.show_information.get_and_show)
        boton_todos.pack(pady=10)

        # Botón para buscar un registro específico
        boton_especifico = tk.Button(self.window_instance.root, text="Buscar Registro Específico", command=self.buscar_registro)
        boton_especifico.pack(pady=10)

    def buscar_registro(self):
        """Solicita un ID de registro y busca el registro específico."""
        registro_id = simpledialog.askstring("Buscar Registro", "Ingresa el ID del registro:")
        if registro_id is not None:  # Verifica que el usuario no haya cancelado
            try:
                registro_id = int(registro_id)  # Convierte a entero
                registros = self.show_information.data_source.get_dates()  # Obtiene todos los registros
                rMax = len(registros)
                if 1 <= registro_id <= rMax:  # Verifica que el ID esté en el rango válido
                    self.show_information.buscar_registro_especifico(registro_id)  # Pasa el ID convertido
                else:
                    self.window_instance.error()  # Llama al método error de Windows
            except ValueError:
                self.window_instance.error()  # Llama al método error de Windows
