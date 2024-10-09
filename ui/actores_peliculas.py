# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'actores_peliculas.ui'
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

class Ui_dialog_actor(object):
    def setupUi(self, dialog_actor):
        if not dialog_actor.objectName():
            dialog_actor.setObjectName(u"dialog_actor")
        dialog_actor.resize(294, 233)
        self.gridLayout = QGridLayout(dialog_actor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.actor_ingresado = QLabel(dialog_actor)
        self.actor_ingresado.setObjectName(u"actor_ingresado")
        self.actor_ingresado.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.actor_ingresado, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_texto = QLabel(dialog_actor)
        self.label_texto.setObjectName(u"label_texto")

        self.gridLayout.addWidget(self.label_texto, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_peliculas_juntos = QLabel(dialog_actor)
        self.label_peliculas_juntos.setObjectName(u"label_peliculas_juntos")

        self.gridLayout.addWidget(self.label_peliculas_juntos, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(dialog_actor)

        QMetaObject.connectSlotsByName(dialog_actor)
    # setupUi

    def retranslateUi(self, dialog_actor):
        dialog_actor.setWindowTitle(QCoreApplication.translate("dialog_actor", u"Dialog", None))
        self.actor_ingresado.setText(QCoreApplication.translate("dialog_actor", u"a", None))
        self.label_texto.setText(QCoreApplication.translate("dialog_actor", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Trabajaron en:</span></p></body></html>", None))
        self.label_peliculas_juntos.setText(QCoreApplication.translate("dialog_actor", u"a", None))
    # retranslateUi

