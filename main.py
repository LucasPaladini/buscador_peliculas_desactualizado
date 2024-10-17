from PySide6.QtWidgets import QApplication
from busqueda_peliculas import VentanaPrincipal
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())
