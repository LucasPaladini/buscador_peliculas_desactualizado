# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datos_pelicula.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(336, 231)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_sinopsis = QLabel(Dialog)
        self.label_sinopsis.setObjectName(u"label_sinopsis")

        self.gridLayout.addWidget(self.label_sinopsis, 8, 1, 1, 2)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_actores = QLabel(Dialog)
        self.label_actores.setObjectName(u"label_actores")

        self.gridLayout.addWidget(self.label_actores, 9, 1, 1, 2)

        self.label_puntuacion = QLabel(Dialog)
        self.label_puntuacion.setObjectName(u"label_puntuacion")

        self.gridLayout.addWidget(self.label_puntuacion, 10, 1, 1, 2)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 10, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)

        self.label_titulo_ingresado = QLabel(Dialog)
        self.label_titulo_ingresado.setObjectName(u"label_titulo_ingresado")

        self.gridLayout.addWidget(self.label_titulo_ingresado, 6, 1, 1, 2)

        self.label_poster = QLabel(Dialog)
        self.label_poster.setObjectName(u"label_poster")

        self.gridLayout.addWidget(self.label_poster, 5, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_sinopsis.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"T\u00edtulo:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Actores:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Pelicula:</span></p></body></html>", None))
        self.label_actores.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_puntuacion.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"puntuacion:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Sinopsis:", None))
        self.label_titulo_ingresado.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_poster.setText("")
    # retranslateUi

