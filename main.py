from PySide6.QtWidgets import QApplication
import sys
from ventana import VentanaPrincipal


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana_principal = VentanaPrincipal()
    ventana_principal.show()

    sys.exit(app.exec())

