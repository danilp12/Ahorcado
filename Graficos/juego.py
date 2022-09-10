
from time import strftime
from turtle import color
from typing import final
from PyQt5.QtGui import QIcon,QColor,QFont
from PyQt5.QtWidgets import  QPushButton, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer
from PyQt5 import QtWidgets, uic
import sys, time
from datetime import datetime as dt
from funciones_juego import *


def hora():
    return dt.now().strftime('%H:%M:%S') 
ScoreBoard = cargar()

class Juego(QDialog):
    timer = QTimer()
    intentos = 6
    
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Juego.ui",self)
        self.setWindowTitle("Nueva Partida - Ahorcado")
        self.palabra,self.pista,self.adivinarpalabra,self.palabraoculta,self.letrasusadas = sortearpalabra()
        self.nombre = self.getNombre()
        dibujar(self,self.intentos)
        self.tiempo()
        self.actualizarintentos()
        self.Palabra.setText(str(self.palabraoculta))
        self.LetrasIngresadas.setText(str(self.letrasusadas))
        self.Pista.setText(self.pista)
        self.Ingresar.clicked.connect(self.ingresoletra)
        self.Continuar.clicked.connect(self.continuar)
        self.Rendirse.clicked.connect(self.rendirse)
    def rendirse(self):
        if QMessageBox.question(self,"Rendirse","Estas seguro que desea rendirse?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No) == QMessageBox.Yes:
            self.close()
    def getNombre(self):
        sonido(self,"nueva.mp3")
        nombre, ok =QInputDialog.getText(self,"Antes de Comenzar","Ingresar Nombre:")
        if ok:
            self.Nombre.setText(nombre)
        else:
            self.Nombre.setText("------")
    def ingresoletra(self):
        try:
            # global palabraoculta
            letra = self.Letra.text().upper()
            if letra.isalpha():
                if letra != "" and len(letra) == 1:
                    if letra in self.palabra:
                        if letra not in self.palabraoculta:
                            sonido(self,"acierto.mp3")
                            self.LetraIngresada.setText("La Letra ingresada es Correcta")
                            self.LetraIngresada.setStyleSheet("color:green")
                            for i in range(len(self.palabra)):
                                if self.Letra.text().upper() == self.palabra[i]:
                                    self.palabraoculta[i] = letra
                                    self.Palabra.setText(str(self.palabraoculta))
                                    self.comprobarpalabra()
                        else:
                            self.LetraIngresada.setText(f"La Letra {letra} ya la habias ingresado")
                            self.LetraIngresada.setStyleSheet("color:green")
                    else:
                        if letra not in self.letrasusadas:
                            sonido(self,"nop.mp3")
                            self.LetraIngresada.setText("La Letra ingresada es Incorrecta")
                            self.LetraIngresada.setStyleSheet("color:red")
                            # global intentos
                            self.intentos -= 1
                            self.actualizarintentos()
                            dibujar(self,self.intentos)
                            self.comprobarintentos()
                            self.letrasusadas.append(letra)
                            self.LetrasIngresadas.setText(str(self.letrasusadas))
                        else:
                            self.LetraIngresada.setText(f"La Letra {letra} ya la habias ingresado")
                            self.LetraIngresada.setStyleSheet("color:black")
                else:
                    self.LetraIngresada.setText("Ingresaste mal la letra")
                    self.LetraIngresada.setStyleSheet("color:black")
            else:
                self.LetraIngresada.setText("Solo Letras")
                self.LetraIngresada.setStyleSheet("color:yellow")
        except Exception as e:
            QMessageBox.warning(self,"Error",f"{e}")
        finally:
            self.Letra.setText("")
    def actualizar_tiempo(self,inicio):
        fin = dt.now()
        actual = fin - inicio
        self.Tiempo.setText(str(actual)[0:7])
    def tiempo(self):
        inicio = dt.now()
        self.timer.start(1000)
        self.timer.timeout.connect(lambda : self.actualizar_tiempo(inicio))
    def actualizarintentos(self):
        self.Intentos.setText(str(self.intentos))
    def comprobarpalabra(self):
        if self.palabraoculta == self.adivinarpalabra:
            sonido(self,"victoria.mp3")
            QMessageBox.information(self,"Partida Finalizada",f"Has Ganado!!\nNombre: {self.Nombre.text()}\nIntentos Restantes: {self.intentos}\nTiempo: {self.Tiempo.text()} segundos\nPalabra: {self.palabra}\nPuntaje: {puntaje(self.modtiempo(),self.intentos)}")
            self.Continuar.setEnabled(True)
            self.Ingresar.setEnabled(False)
            self.Rendirse.setEnabled(False)
            ScoreBoard.append([self.Nombre.text(),self.intentos,self.modtiempo(),self.palabra,puntaje(self.modtiempo(),self.intentos)])
            guardar(ScoreBoard)
    def comprobarintentos(self):
        if self.intentos == 0:
            sonido(self,"derrota.mp3")
            QMessageBox.information(self,"Partida Finalizada",f"Lo siento, Has perdido - La palabra era: {self.palabra}")
            self.Continuar.setEnabled(True)
            self.Ingresar.setEnabled(False)
            self.Rendirse.setEnabled(False)
            ScoreBoard.append([self.Nombre.text(),self.intentos,self.modtiempo(),self.palabra,0])
            guardar(ScoreBoard)
        elif 3 >= self.intentos:
            self.Intentos.setStyleSheet("color:red")
    def modtiempo(self):
        tiempo = self.Tiempo.text()
        t= []
        for i in range(len(tiempo)):
            if tiempo[i] == ":":
                pass
            else:
                t.append(tiempo[i])
        return int("".join(t))
    def continuar(self):
        self.Palabra.setText("")
        self.LetrasIngresadas.setText("")
        self.Pista.setText("")
        self.close()
        
    

    

