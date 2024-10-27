import tkinter as tk
from tkinter import ttk


class ShowInformation:
    __promedioO=0
    def __init__(self, root, data_source):
        self.tree = None
        self.root = root
        self.data_source = data_source
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Registro de Estudiantes de 2do Semestre de Ing en Sistemas Computacionales")
        self.root.geometry("760x500")
        self.root.resizable(False, False)
        self.root.config(bg="black")

        # Botón para obtener todos los registros
        boton_todos = tk.Button(self.root, text="Obtener Todos los Registros", command=self.get_and_show)
        boton_todos.pack(pady=10)

        # Botón para buscar un registro específico
        boton_especifico = tk.Button(self.root, text="Buscar Registro Específico", command=self.buscar_registro_especifico)
        boton_especifico.pack(pady=10)

        # Tabla para mostrar los registros
        estilo = ttk.Style()
        estilo.theme_use("default")
        estilo.configure("Custom.Treeview", background="black", foreground="green",  fieldbackground="black",font=("Arial",15))
        estilo.map("Custom.Treeview", background=[("selected", "black")], foreground=[("selected", "green")])
        
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Apellido", "Ciudad", "Calle","Promedio"), show="headings",style="Custom.Treeview")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Ciudad", text="Ciudad")
        self.tree.heading("Calle", text="Calle")
        self.tree.heading("Promedio",text="Promedio")
        self.tree.column("ID", width=50, anchor='center', stretch=False)
        self.tree.column("Nombre", width=125, anchor='w', stretch=False)
        self.tree.column("Apellido", width=155, anchor='w', stretch=False)
        self.tree.column("Ciudad", width=160, anchor='w', stretch=False)
        self.tree.column("Calle", width=200, anchor='w', stretch=False)
        self.tree.column("Promedio", width=70, anchor='w', stretch=False)
        self.tree.pack(pady=10, fill="both", expand=True)



    def get_and_show(self):
        registros = self.data_source.get_dates()
        self.tree.delete(*self.tree.get_children())
        if "error" in registros:
            print(registros["error"])
            return

        for registro in registros:
            id = registro.get("id", "N/A")
            nombre = registro.get("nombre", "N/A")
            apellido = registro.get("apellido", "N/A")
            ciudad = registro.get("ciudad", "N/A")
            calle = registro.get("calle", "N/A")
            promedio = registro.get("promedio", "N/A")
            promedioO="{:.2f}".format(promedio/1000)
            self.tree.insert("", "end", values=(id, nombre, apellido, ciudad, calle,promedioO))


    def buscar_registro_especifico(self):
        registro = self.data_source.solicitar_id()
        if not self.tree_exists():
            return

        self.tree.delete(*self.tree.get_children())

        if "error" in registro:
            print(registro["error"])
        else:
            id = registro.get("id", "N/A")
            nombre = registro.get("nombre", "N/A")
            apellido = registro.get("apellido", "N/A")
            ciudad = registro.get("ciudad", "N/A")
            calle = registro.get("calle", "N/A")
            promedio= registro.get("promedio","N/A")
            promedioO="{:.2f}".format(promedio/1000)
            self.tree.insert("", "end", values=(id, nombre, apellido, ciudad, calle,promedioO))

    def tree_exists(self):
        try:
            # Verificar si el Treeview sigue existiendo
            self.root.nametowidget(self.tree.winfo_pathname(self.tree.winfo_id()))
            return True
        except tk.TclError:
            return False
