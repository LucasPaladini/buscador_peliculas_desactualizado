# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)

class Ui_Ventana_principal(object):
    def setupUi(self, Ventana_principal):
        if not Ventana_principal.objectName():
            Ventana_principal.setObjectName(u"Ventana_principal")
        Ventana_principal.resize(263, 199)
        self.centralwidget = QWidget(Ventana_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_ingreso_nombre = QLineEdit(self.centralwidget)
        self.line_ingreso_nombre.setObjectName(u"line_ingreso_nombre")
        self.line_ingreso_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.line_ingreso_nombre, 2, 0, 1, 1)

        self.boton_buscar_pelicula = QPushButton(self.centralwidget)
        self.boton_buscar_pelicula.setObjectName(u"boton_buscar_pelicula")

        self.gridLayout.addWidget(self.boton_buscar_pelicula, 2, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)

        self.line_ingreso_actor_2 = QLineEdit(self.centralwidget)
        self.line_ingreso_actor_2.setObjectName(u"line_ingreso_actor_2")
        self.line_ingreso_actor_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.line_ingreso_actor_2, 8, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 2)

        self.line_ingreso_actor_1 = QLineEdit(self.centralwidget)
        self.line_ingreso_actor_1.setObjectName(u"line_ingreso_actor_1")
        self.line_ingreso_actor_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.line_ingreso_actor_1, 7, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 2)

        self.boton_buscar_actor = QPushButton(self.centralwidget)
        self.boton_buscar_actor.setObjectName(u"boton_buscar_actor")

        self.gridLayout.addWidget(self.boton_buscar_actor, 8, 1, 1, 1)

        Ventana_principal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Ventana_principal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 263, 22))
        Ventana_principal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Ventana_principal)
        self.statusbar.setObjectName(u"statusbar")
        Ventana_principal.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_principal)
        self.boton_buscar_actor.clicked.connect(Ventana_principal.buscar_peliculas_por_actores)
        self.boton_buscar_pelicula.clicked.connect(Ventana_principal.buscar_peliculas)

        QMetaObject.connectSlotsByName(Ventana_principal)
    # setupUi

    def retranslateUi(self, Ventana_principal):
        Ventana_principal.setWindowTitle(QCoreApplication.translate("Ventana_principal", u"MainWindow", None))
        self.line_ingreso_nombre.setPlaceholderText(QCoreApplication.translate("Ventana_principal", u"Buscar por nombre", None))
        self.boton_buscar_pelicula.setText(QCoreApplication.translate("Ventana_principal", u"Buscar", None))
        self.label.setText(QCoreApplication.translate("Ventana_principal", u"Busqueda de pel\u00edculas", None))
        self.line_ingreso_actor_2.setPlaceholderText(QCoreApplication.translate("Ventana_principal", u"Buscar actor 2", None))
        self.line_ingreso_actor_1.setPlaceholderText(QCoreApplication.translate("Ventana_principal", u"Buscar actor 1", None))
        self.label_2.setText(QCoreApplication.translate("Ventana_principal", u"<html><head/><body><p align=\"center\">Busqueda por actor/es</p></body></html>", None))
        self.boton_buscar_actor.setText(QCoreApplication.translate("Ventana_principal", u"Buscar", None))
    # retranslateUi

