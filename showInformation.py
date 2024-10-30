from desing import Desing

class ShowInformation(Desing):
    def __init__(self, data_source, root):
        self.data_source = data_source
        self.tree = None
        self.setup_ui(root)

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
            promedioO = "{:.2f}".format(promedio / 1000)
            self.tree.insert("", "end", values=(id, nombre, apellido, ciudad, calle, promedioO))

    def buscar_registro_especifico(self, registro_id):
        registro = self.data_source.solicitar_id(registro_id)

        self.tree.delete(*self.tree.get_children())
        if "error" in registro:
            print(registro["error"])
        else:
            id = registro.get("id", "N/A")
            nombre = registro.get("nombre", "N/A")
            apellido = registro.get("apellido", "N/A")
            ciudad = registro.get("ciudad", "N/A")
            calle = registro.get("calle", "N/A")
            promedio = registro.get("promedio", "N/A")
            promedioO = "{:.2f}".format(promedio / 1000)
            self.tree.insert("", "end", values=(id, nombre, apellido, ciudad, calle, promedioO))
