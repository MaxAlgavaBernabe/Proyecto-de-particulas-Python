from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from lista import ListaParticulas
from particula import Particula
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.lista=ListaParticulas()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregarInicio_pushButton.clicked.connect(self.agregar_Inicio)
        self.ui.agregarFinal_pushButton.clicked.connect(self.agregar_Final)
        self.ui.mostrar_pushButton.clicked.connect(self.mostrar)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_Archivo)
    @Slot( )
    def action_abrir_Archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if(self.lista.abrir(ubicacion)):
                QMessageBox.information(
                self,
                "Exito",
                "Se pudo abrir el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo abrir el archivo " + ubicacion
            )
        
    @Slot( )
    def action_guardar_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.lista.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )


    @Slot()
    def agregar_Inicio(self):
        id=self.ui.id_spinBox.value()
        origen_x=self.ui.origenX_spinBox.value()
        origen_y= self.ui.origenY_spinBox.value()
        destino_x= self.ui.destinoX_spinBox.value()
        destino_y =self.ui.destinoY_spinBox.value()
        velocidad =int(self.ui.velocidad_lineEdit.text())
        red =self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue =self.ui.BluespinBox.value()
        particula=Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        
        self.lista.agregarInicio(particula)
        

    @Slot()
    def agregar_Final(self):
        id=self.ui.id_spinBox.value()
        origen_x=self.ui.origenX_spinBox.value()
        origen_y= self.ui.origenY_spinBox.value()
        destino_x= self.ui.destinoX_spinBox.value()
        destino_y =self.ui.destinoY_spinBox.value()
        velocidad =int(self.ui.velocidad_lineEdit.text())
        red =self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue =self.ui.BluespinBox.value()
        particula=Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.lista.agregarFinal(particula)
    @Slot()
    def mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.lista))
