import tkinter as tk
from buttonHandler import ButtonHandler

class Windows:
    def __init__(self, root, show_information):
        self.root = root
        self.show_information = show_information
        self.button_handler = ButtonHandler(self.show_information, self)
        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz de usuario."""
        self.root.title("Registro de Estudiantes de 2do Semestre de Ing en Sistemas Computacionales")
        self.root.geometry("760x500")
        self.root.resizable(False, False)
        self.root.config(bg="black")


    def error(self):
        ventana_error = tk.Tk()
        ventana_error.title("Error")
        ventana_error.config(bg="black")
        tk.Label(ventana_error, text="ID Invalido.", padx=20, pady=20, bg="black", fg="red").pack()
        ventana_error.mainloop()
