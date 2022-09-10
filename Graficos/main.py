

from time import strftime
from PyQt5.QtGui import QIcon,QColor,QFont
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer, QUrl
from PyQt5 import QtWidgets, uic
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import sys, os
from juego import Juego
from score import Score
from funciones_juego import reproductor, sonido



class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("Mainwindow.ui",self)
        self.setWindowTitle("Juego del Ahorcado")
        self.Salir.clicked.connect(self.salir)
        self.NuevaPartida.clicked.connect(self.nueva)
        self.ScoreBoard.clicked.connect(self.score)
        self.Volumen.setIcon(QIcon(f"{os.getcwd()}"+"\src\ico\ico.png"))
        self.Volumen.clicked.connect(self.pausa)
        self.Next.setIcon(QIcon(f"{os.getcwd()}"+"\src\ico\\next.png"))
        self.Next.clicked.connect(self.next)
        reproductor(self)
    def next(self):
        reproductor(self,"next")
    def pausa(self):
        reproductor(self,"pausa")
    def salir(self):
        self.close()
    def nueva(self):
        nuevo = Juego()
        nuevo.exec_()
    def score(self):
        sco = Score()
        sco.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Main()
    ventana.show()
    sys.exit(app.exec_())

