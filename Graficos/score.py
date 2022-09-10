from time import strftime
from PyQt5.QtGui import QIcon,QColor,QFont
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer, Qt
from PyQt5 import QtWidgets, uic
import sys
from funciones_juego import *


class Score(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Score.ui",self)
        self.setWindowTitle("ScoreBoard")
        self.ScoreBoard = cargar()
        self.Recargar.clicked.connect(self.actualizar)
        self.actualizar()
    def actualizar(self):
        self.Tabla.setRowCount(0)
        for linea in self.ScoreBoard:
            self.Tabla.insertRow(self.Tabla.rowCount())
            self.Tabla.setItem(self.Tabla.rowCount()-1,0,QTableWidgetItem(linea[0]))
            self.Tabla.setItem(self.Tabla.rowCount()-1,1,QTableWidgetItem(str(linea[1])))
            self.Tabla.setItem(self.Tabla.rowCount()-1,2,QTableWidgetItem(str(linea[2])))
            self.Tabla.setItem(self.Tabla.rowCount()-1,3,QTableWidgetItem(linea[3]))
            self.Tabla.setItem(self.Tabla.rowCount()-1,4,QTableWidgetItem(str(linea[4])))
        self.Tabla.sortItems(4,order=Qt.DescendingOrder)
