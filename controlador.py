from PySide6.QtGui import QStandardItem, QStandardItemModel
# from PySide6.QtWidgets import QMessageBox
# from pelicula import Pelicula




class ConectarBotones:
    def __init__(self, ventanaprincipal):
        self.__ventana_principal = ventanaprincipal

        # self.__modelo_tareas_vacias = QStandardItemModel()
        # self.__modelo_tareas_completadas = QStandardItemModel()
        # self.__ventana.tableTareaVacia.setModel(self.__modelo_tareas_vacias)  # (izq)
        # self.__ventana.tableTareaCompletada.setModel(self.__modelo_tareas_completadas)  # (derec)

    def abrir_actores(self):
        from ventana import VentanaActor
        print("Abriendo ventana Actor")
        ventana_actor = VentanaActor()
        ventana_actor.exec()

