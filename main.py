from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
import sys
from ui.ventana_principal import Ui_Ventana_principal
from ui.actores_peliculas import Ui_dialog_actor
from ui.datos_pelicula import Ui_Dialog


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_Ventana_principal()
        self.__ui.setupUi(self)
        self.setWindowTitle("Ventana principal")

class VentanaActor(QDialog):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_dialog_actor()
        self.__ui.setupUi(self)
        self.setWindowTitle("Ventana Actores")

class VentanaPelicula(QDialog):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_Dialog()
        self.__ui.setupUi(self)
        self.setWindowTitle("Ventana pelicula")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_actor = VentanaActor()
    ventana_pelicula = VentanaPelicula()

    ventana_pelicula.show()
    ventana_principal.show()
    ventana_actor.show()
    sys.exit(app.exec())

