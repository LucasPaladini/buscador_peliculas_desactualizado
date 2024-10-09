from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox
from ui.ventana_principal import Ui_Ventana_principal
from ui.actores_peliculas import Ui_dialog_actor
from ui.datos_pelicula import Ui_Dialog
from pelicula import Pelicula  # Asegúrate de importar la clase Pelicula


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Ventana_principal()
        self.ui.setupUi(self)
        self.setWindowTitle("Ventana principal")

    def obtener_nombres_actores(self):
        return self.ui.line_ingreso_actor_1.text(), self.ui.line_ingreso_actor_2.text()

    def mostrar_error(self, mensaje):
        QMessageBox.warning(self, "Error", mensaje)

    def buscar_peliculas_por_actores(self):
        actor_1, actor_2 = self.obtener_nombres_actores()

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
                    self.mostrar_error("No se encontraron películas con esos actores.")
            except (FileNotFoundError, ValueError) as e:
                self.mostrar_error(str(e))
        else:
            self.mostrar_error("El actor no puede ser el mismo.")

    def buscar_peliculas(self):  # Método para buscar películas por nombre
        self.hide()
        nombre_pelicula = self.ui.line_ingreso_nombre.text()  # Asegúrate de que este campo esté en la UI

        if not nombre_pelicula:
            QMessageBox.warning(self, "Error", "Ingresa una película")
            return

        pelicula = Pelicula("", "", [], 0, "")
        pelicula_encontrada = pelicula.pelicula_existe(nombre_pelicula,
                                                       'peliculas/peliculas.txt')

        if pelicula_encontrada:
            ventana_pelicula = VentanaPelicula(pelicula_encontrada)
            ventana_pelicula.exec()
        else:
            QMessageBox.warning(self, "Película no encontrada", f"La película '{nombre_pelicula}' no está disponible.")


class VentanaActor(QDialog):
    def __init__(self, actor_1, actor_2, peliculas):
        super().__init__()
        self.__ui = Ui_dialog_actor()
        self.__ui.setupUi(self)
        self.setWindowTitle("Ventana Actores")
        self.__ui.actor_ingresado.setText(f"{actor_1} y {actor_2}")
        self.__ui.label_peliculas_juntos.setText(", ".join([p['titulo'] for p in peliculas]))
