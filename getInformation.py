import requests
import tkinter as tk
from tkinter import simpledialog

class GetInformation:
    def __init__(self):
        self.__url = "https://671be4152c842d92c381a493.mockapi.io/test"
        self.__id = None

    def get_dates(self):
        try:
            response = requests.get(self.__url)
            response.raise_for_status()
            data = response.json()

            if isinstance(data, list) and data:
                return data
            else:
                return {"error": "No se encontraron registros."}
        except Exception as e:
            return {"error": f"Error: {e}"}

    def solicitar_id(self):
        ventana = tk.Tk()
        ventana.withdraw()
        user_input = simpledialog.askstring("Entrada", "¿Qué registro deseas ver?")
        ventana.destroy()

        try:
            registro_id = int(user_input)

            if 1 <= registro_id <= 100:
                url = f"{self.__url}/{registro_id}"
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                return data
            else:
                return GetInformation.error(self)

        except ValueError:
            return {"error": "Por favor, ingresa un número válido."}
        except Exception as e:
            return {"error": f"Error: {e}"}

    def error(self):
        ventana_error = tk.Tk()
        ventana_error.title("Error")
        tk.Label(ventana_error, text="Id Invalido.", padx=20, pady=20).pack()
        #tk.Button(ventana_error, text="Cerrar", command=ventana_error.destroy).pack(pady=(0, 20))
        ventana_error.mainloop()