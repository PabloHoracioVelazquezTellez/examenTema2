from tkinter import ttk

class Desing:
    def setup_ui(self, root):
        # Tabla para mostrar los registros
        estilo = ttk.Style()
        estilo.theme_use("default")
        estilo.configure("Custom.Treeview", background="black", foreground="green", fieldbackground="black",
                         font=("Arial", 15))
        estilo.map("Custom.Treeview", background=[("selected", "black")], foreground=[("selected", "green")])

        self.tree = ttk.Treeview(root, columns=("ID", "Nombre", "Apellido", "Ciudad", "Calle", "Promedio"),
                                 show="headings", style="Custom.Treeview")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Ciudad", text="ciudad")
        self.tree.heading("Calle", text="Calle")
        self.tree.heading("Promedio", text="Promedio")
        self.tree.column("ID", width=50, anchor='center', stretch=False)
        self.tree.column("Nombre", width=125, anchor='w', stretch=False)
        self.tree.column("Apellido", width=155, anchor='w', stretch=False)
        self.tree.column("Ciudad", width=160, anchor='w', stretch=False)
        self.tree.column("Calle", width=200, anchor='w', stretch=False)
        self.tree.column("Promedio", width=70, anchor='w', stretch=False)
        self.tree.pack(pady=10, fill="both", expand=True)
