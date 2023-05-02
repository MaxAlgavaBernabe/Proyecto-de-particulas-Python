from PySide2.QtWidgets import QMainWindow, QGraphicsScene
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from lista import ListaParticulas
from particula import Particula
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide2.QtGui import QPen, QColor, QTransform

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.lista=ListaParticulas()
        self.ui = Ui_MainWindow()
        self.scene=QGraphicsScene()
        self.ui.setupUi(self)
        self.ui.agregarInicio_pushButton.clicked.connect(self.agregar_Inicio)
        self.ui.agregarFinal_pushButton.clicked.connect(self.agregar_Final)
        self.ui.mostrar_pushButton.clicked.connect(self.mostrar)
        self.ui.buscar_pushButton.clicked.connect(self.buscar)
        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_Archivo)
        self.ui.dibujar_pushButton.clicked.connect(self.dibujar_escena)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar_escena)
        self.ui.actionPor_ID.triggered.connect(self.ordenar_id)
        self.ui.actionPor_Distancia.triggered.connect(self.ordenar_distancia)
        self.ui.actionPor_Velocidad_ascendente.triggered.connect(self.ordenar_velocidad)
        self.ui.pantalla.setScene(self.scene)
    @Slot()
    def ordenar_id(self):
        
            self.lista.sort_id()
    @Slot()
    def ordenar_distancia(self):
        self.lista.sort_distancia()
    @Slot()
    def ordenar_velocidad(self):
        self.lista.sort_velocidad()
    @Slot()
    def dibujar_escena(self):
      
        for particula in self.lista:
            pen=QPen()
            pen.setWidth(2)
            r=particula.red
            g=particula.green
            b=particula.blue
            origen_x=particula.origen_x
            origen_y=particula.origen_y
            destino_x=particula.destino_x
            destino_y=particula.destino_y
            color=QColor(r,g,b)
            pen.setColor(color)
            self.scene.addEllipse(origen_x,origen_y,6,6,pen)
            self.scene.addEllipse(destino_x,destino_y,6,6,pen)
            self.scene.addLine(origen_x+3,origen_y+3,destino_x+3,destino_y+3,pen)

    @Slot()
    def limpiar_escena(self):
        self.scene.clear()
    def wheelEvent(self, event):
        
        if event.delta()>0:
            self.ui.pantalla.scale(1.2,1.2)
        else:
            self.ui.pantalla.scale(0.8,0.8)
    @Slot()
    def buscar(self):
        id_buscar=self.ui.buscar.text()
        encontrado=False
        for particula in self.lista:
            if id_buscar== str(particula.id):
                self.ui.tableWidget.clear()
                self.ui.tableWidget.setColumnCount(10)
                headers = ["ID","OrigenX","OrigenY","DestinoX","DestinoY","Velocidad","Red","Green","Blue","Distancia"]
                self.ui.tableWidget.setHorizontalHeaderLabels(headers)
                self.ui.tableWidget.setRowCount(1)
                id_widget= QTableWidgetItem(str(particula.id))
                origenX_widget= QTableWidgetItem(str(particula.origen_x))
                origenY_widget= QTableWidgetItem(str(particula.origen_y))
                destinoX_widget= QTableWidgetItem(str(particula.destino_x))
                destinoY_widget= QTableWidgetItem(str(particula.destino_y))
                velocidad_widget= QTableWidgetItem(str(particula.velocidad))
                red_widget= QTableWidgetItem(str(particula.red))
                green_widget= QTableWidgetItem(str(particula.green))
                blue_widget= QTableWidgetItem(str(particula.blue))
                distancia_widget= QTableWidgetItem(str(particula.distancia))
                

                self.ui.tableWidget.setItem(0,0,id_widget)
                self.ui.tableWidget.setItem(0,1,origenX_widget)
                self.ui.tableWidget.setItem(0,2,origenY_widget)
                self.ui.tableWidget.setItem(0,3,destinoX_widget)
                self.ui.tableWidget.setItem(0,4,destinoY_widget)
                self.ui.tableWidget.setItem(0,5,velocidad_widget)
                self.ui.tableWidget.setItem(0,6,red_widget)
                self.ui.tableWidget.setItem(0,7,green_widget)
                self.ui.tableWidget.setItem(0,8,blue_widget)
                self.ui.tableWidget.setItem(0,9,distancia_widget)
                encontrado = True
        
                return
        if encontrado is False:
              QMessageBox.information(
                self,
                "Error",
                "No se encontro el id " + id_buscar
            )

    @Slot()
    def mostrar_tabla(self):
        self.ui.tableWidget.setColumnCount(10)
        headers = ["ID","OrigenX","OrigenY","DestinoX","DestinoY","Velocidad","Red","Green","Blue","Distancia"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.tableWidget.setRowCount(len(self.lista))
        row=0
        for particula in self.lista:
            id_widget= QTableWidgetItem(str(particula.id))
            origenX_widget= QTableWidgetItem(str(particula.origen_x))
            origenY_widget= QTableWidgetItem(str(particula.origen_y))
            destinoX_widget= QTableWidgetItem(str(particula.destino_x))
            destinoY_widget= QTableWidgetItem(str(particula.destino_y))
            velocidad_widget= QTableWidgetItem(str(particula.velocidad))
            red_widget= QTableWidgetItem(str(particula.red))
            green_widget= QTableWidgetItem(str(particula.green))
            blue_widget= QTableWidgetItem(str(particula.blue))
            distancia_widget= QTableWidgetItem(str(particula.distancia))
            

            self.ui.tableWidget.setItem(row,0,id_widget)
            self.ui.tableWidget.setItem(row,1,origenX_widget)
            self.ui.tableWidget.setItem(row,2,origenY_widget)
            self.ui.tableWidget.setItem(row,3,destinoX_widget)
            self.ui.tableWidget.setItem(row,4,destinoY_widget)
            self.ui.tableWidget.setItem(row,5,velocidad_widget)
            self.ui.tableWidget.setItem(row,6,red_widget)
            self.ui.tableWidget.setItem(row,7,green_widget)
            self.ui.tableWidget.setItem(row,8,blue_widget)
            self.ui.tableWidget.setItem(row,9,distancia_widget)
            row += 1
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
