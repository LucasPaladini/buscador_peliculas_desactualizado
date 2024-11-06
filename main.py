from PySide6.QtWidgets import QApplication
import sys

from controlador import Controlador

if __name__ == "__main__":
    app = QApplication(sys.argv)

    controlador = Controlador()
    controlador.ejecutar()
    sys.exit(app.exec())
