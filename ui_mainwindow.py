# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(709, 604)
        MainWindow.setStyleSheet(u"\n"
"\n"
"background-color: rgb(95, 99, 115);")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionPor_ID = QAction(MainWindow)
        self.actionPor_ID.setObjectName(u"actionPor_ID")
        self.actionPor_Distancia = QAction(MainWindow)
        self.actionPor_Distancia.setObjectName(u"actionPor_Distancia")
        self.actionPor_Velocidad_ascendente = QAction(MainWindow)
        self.actionPor_Velocidad_ascendente.setObjectName(u"actionPor_Velocidad_ascendente")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tab_4 = QTabWidget(self.centralwidget)
        self.tab_4.setObjectName(u"tab_4")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.destinoY_spinBox = QSpinBox(self.groupBox)
        self.destinoY_spinBox.setObjectName(u"destinoY_spinBox")
        self.destinoY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoY_spinBox, 4, 1, 1, 1)

        self.agregarInicio_pushButton = QPushButton(self.groupBox)
        self.agregarInicio_pushButton.setObjectName(u"agregarInicio_pushButton")

        self.gridLayout.addWidget(self.agregarInicio_pushButton, 10, 1, 1, 1)

        self.agregarFinal_pushButton = QPushButton(self.groupBox)
        self.agregarFinal_pushButton.setObjectName(u"agregarFinal_pushButton")

        self.gridLayout.addWidget(self.agregarFinal_pushButton, 11, 1, 1, 1)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")

        self.gridLayout.addWidget(self.id_spinBox, 0, 1, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 12, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(85, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.origenX_spinBox = QSpinBox(self.groupBox)
        self.origenX_spinBox.setObjectName(u"origenX_spinBox")
        self.origenX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenX_spinBox, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.velocidad_lineEdit = QLineEdit(self.groupBox)
        self.velocidad_lineEdit.setObjectName(u"velocidad_lineEdit")

        self.gridLayout.addWidget(self.velocidad_lineEdit, 5, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.green_spinBox, 7, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.red_spinBox, 6, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.destinoX_spinBox = QSpinBox(self.groupBox)
        self.destinoX_spinBox.setObjectName(u"destinoX_spinBox")
        self.destinoX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoX_spinBox, 2, 1, 1, 1)

        self.BluespinBox = QSpinBox(self.groupBox)
        self.BluespinBox.setObjectName(u"BluespinBox")
        self.BluespinBox.setMaximum(255)

        self.gridLayout.addWidget(self.BluespinBox, 8, 1, 1, 1)

        self.origenY_spinBox = QSpinBox(self.groupBox)
        self.origenY_spinBox.setObjectName(u"origenY_spinBox")
        self.origenY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenY_spinBox, 3, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.gridLayout_2.addWidget(self.salida, 0, 1, 1, 1)

        self.tab_4.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.buscar = QLineEdit(self.tab_3)
        self.buscar.setObjectName(u"buscar")

        self.gridLayout_5.addWidget(self.buscar, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_3)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_5.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_3)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_5.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.tableWidget = QTableWidget(self.tab_3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_5.addWidget(self.tableWidget, 0, 0, 1, 3)

        self.tab_4.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pantalla = QGraphicsView(self.tab_2)
        self.pantalla.setObjectName(u"pantalla")

        self.gridLayout_4.addWidget(self.pantalla, 0, 0, 1, 2)

        self.limpiar_pushButton = QPushButton(self.tab_2)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout_4.addWidget(self.limpiar_pushButton, 1, 1, 1, 1)

        self.dibujar_pushButton = QPushButton(self.tab_2)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")

        self.gridLayout_4.addWidget(self.dibujar_pushButton, 1, 0, 1, 1)

        self.tab_4.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tab_4, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 709, 21))
        self.menuAbrir = QMenu(self.menubar)
        self.menuAbrir.setObjectName(u"menuAbrir")
        self.menuOrdenar = QMenu(self.menubar)
        self.menuOrdenar.setObjectName(u"menuOrdenar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbrir.menuAction())
        self.menubar.addAction(self.menuOrdenar.menuAction())
        self.menuAbrir.addAction(self.actionGuardar)
        self.menuAbrir.addAction(self.actionAbrir)
        self.menuOrdenar.addAction(self.actionPor_ID)
        self.menuOrdenar.addAction(self.actionPor_Distancia)
        self.menuOrdenar.addAction(self.actionPor_Velocidad_ascendente)

        self.retranslateUi(MainWindow)

        self.tab_4.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionPor_ID.setText(QCoreApplication.translate("MainWindow", u"Por ID(ascendente)", None))
        self.actionPor_Distancia.setText(QCoreApplication.translate("MainWindow", u"Por Distancia(descendente)", None))
        self.actionPor_Velocidad_ascendente.setText(QCoreApplication.translate("MainWindow", u"Por Velocidad(ascendente)", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.agregarInicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.agregarFinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar Informacion capturada", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.tab_4.setTabText(self.tab_4.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Capturar", None))
        self.buscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Particula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tab_4.setTabText(self.tab_4.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.tab_4.setTabText(self.tab_4.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.menuAbrir.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuOrdenar.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar", None))
    # retranslateUi

