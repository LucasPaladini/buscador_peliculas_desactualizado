import json
import os

class Pelicula:
    def __init__(self, titulo, sinopsis, actores, puntuacion, poster):
        self.titulo = titulo
        self.sinopsis = sinopsis
        self.actores = actores
        self.puntuacion = puntuacion
        self.poster = poster

    def pelicula_existe(self, nombre_pelicula, archivo):
        try:
            with open(archivo, 'r') as file:
                peliculas = json.load(file)
                for pelicula in peliculas:
                    if pelicula['titulo'].lower() == nombre_pelicula.lower():
                        return Pelicula(**pelicula)  # Devuelve una instancia de Pelicula
        except FileNotFoundError:
            raise FileNotFoundError("El archivo de películas no fue encontrado.")
        except json.JSONDecodeError:
            raise ValueError("Error al leer el archivo de películas.")

    def cargar_peliculas(self, archivo):
        try:
            with open(archivo, 'r') as file:
                peliculas_data = json.load(file)
                return [Pelicula(**data) for data in peliculas_data]  # Devuelve una lista de objetos Pelicula
        except FileNotFoundError:
            raise FileNotFoundError("El archivo de películas no fue encontrado.")
        except json.JSONDecodeError:
            raise ValueError("Error al leer el archivo de películas.")
