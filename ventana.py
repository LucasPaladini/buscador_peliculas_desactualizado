from PySide6.QtWidgets import QMainWindow, QDialog
from ui.ventana_principal import Ui_Ventana_principal
from ui.actores_peliculas import Ui_dialog_actor
from ui.datos_pelicula import Ui_Dialog
from controlador import ConectarBotones


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Abriendo App")
        self.__ui = Ui_Ventana_principal()
        self.__ui.setupUi(self)
        self.setWindowTitle("Ventana principal")

        # instancio ConectarBotones y paso la ventana a los métodos
        self.__botones_controlador = ConectarBotones(self)
        self.__ui.boton_buscar_actor.clicked.connect(self.__botones_controlador.abrir_actores)

        # self.__ui.b.clicked.connect(self.__botones_controlador.completar_tarea)
        # self.__ui.boton_eliminar_tarea.clicked.connect(self.__botones_controlador.eliminar_tarea)

class VentanaActor(QDialog):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_dialog_actor()
        self.__ui.setupUi(self)
        self.setWindowTitle("Ventana Actores")

# class VentanaPelicula(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.__ui = Ui_Dialog()
#         self.__ui.setupUi(self)
#         self.setWindowTitle("Ventana pelicula")

