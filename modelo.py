import json
import os


class Pelicula:
    def obtener_peliculas(self):
        ruta_archivo = os.path.join("peliculas", "peliculas.json")

        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)

        except Exception as e:
            print(f"Ocurrió un error: {e}")
