import requests

class GetInformation:
    __registro_id=None
    def __init__(self):
        self.__url = "https://671be4152c842d92c381a493.mockapi.io/test"

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

    def solicitar_id(self, registro_id):
        registros = self.get_dates()
        rMax = len(registros)
        try:
            registro_id = int(registro_id)
            if registro_id >= 1 and registro_id <= rMax:
                # Consulta de registro si está en el rango válido
                url = f"{self.__url}/{registro_id}"
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                return data
            else:
                return {"error": "ID fuera del rango válido."}
        except ValueError:
            return {"error": "Por favor, ingresa un número válido."}
        except Exception as e:
            return {"error": f"Error: {e}"}

