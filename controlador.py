from vista import VentanaPrincipal, VentanaActor
from pelicula import Pelicula

class Controlador:
    def __init__(self):
        self.vista = VentanaPrincipal()

    def buscar_peliculas_por_actores(self):
        actor_1, actor_2 = self.vista.obtener_nombres_actores()

        if actor_1 != actor_2:
            try:
                pelicula = Pelicula("", "", [], 0, "")
                peliculas = pelicula.cargar_peliculas('peliculas/peliculas.txt')

                peliculas_encontradas = [p for p in peliculas if
                                         actor_1.lower() in [a.lower() for a in p.actores] and actor_2.lower() in [
                                             a.lower() for a in p.actores]]

                if peliculas_encontradas:
                    ventana_actor = VentanaActor(actor_1, actor_2, peliculas_encontradas)
                    ventana_actor.exec()
                else:
                    self.vista.mostrar_error("No se encontraron películas con esos actores.")
            except (FileNotFoundError, ValueError) as e:
                self.vista.mostrar_error(str(e))
        else:
            self.vista.mostrar_error("El actor no puede ser el mismo.")
