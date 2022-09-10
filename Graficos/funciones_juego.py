import random, json, os
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap,QIcon
Reproducir = True
def PalabraRandom():
    listado = ["pelota","paleta","pileta","ventana","palindromo","celular","algoritmo","Auriculares"]
    pistas =["Objeto que rebota","Se usa para jugar con una pelota","Lugar para refrescarse","Abertura de una vivienda","Palabra que se lee de derecho y reves","Dispositivo Movil","Conjunto de instrucciones de programacion","Accesorio para escuchar musica"]
    num = random.randint(0,len(listado)-1)
    return listado[num].upper(), pistas[num]
def puntaje(tiempo,intentos):
    puntaje = (1000-tiempo)*intentos
    if len(str(puntaje)) == 3:
        puntaje = f"0{puntaje}"
        return str(puntaje)
    else: return str(puntaje)

                
def cargar():
    with open("ScoreBoard.json","r") as file:
        ScoreBoard = list(json.load(file))
        return ScoreBoard
def guardar(ScoreBoard):
        with open ("ScoreBoard.json","w")as f:
            json.dump(ScoreBoard,f)
            print("Guardado con Exito")
def dibujar(self,intentos):
    filepath = os.path.join(os.getcwd()+"\\src\\ico\\")
    if intentos == 6:
        dibujo = QPixmap(f"{filepath}"+"fondo.png")
        self.Dibujo.setPixmap(dibujo)
    elif intentos == 5:
        dibujo = QPixmap(f"{filepath}"+"5.png")
        self.Dibujo.setPixmap(dibujo) 
    elif intentos ==4:
        dibujo = QPixmap(f"{filepath}"+"4.png")
        self.Dibujo.setPixmap(dibujo)
    elif intentos == 3:
        dibujo = QPixmap(f"{filepath}"+"3.png")
        self.Dibujo.setPixmap(dibujo)
    elif intentos == 2:
        dibujo = QPixmap(f"{filepath}"+"2.png")
        self.Dibujo.setPixmap(dibujo)
    elif intentos == 1:
        dibujo = QPixmap(f"{filepath}"+"1.png")
        self.Dibujo.setPixmap(dibujo)
    else:
        dibujo = QPixmap(f"{filepath}"+"0.png")
        self.Dibujo.setPixmap(dibujo)
def sortearpalabra():
    palabra, pista = PalabraRandom()
    adivinarpalabra = []
    palabraoculta = []
    letrasusadas= []
    for i in range(len(palabra)):
        adivinarpalabra.append(palabra[i])
        palabraoculta.append("-")
    return palabra,pista,adivinarpalabra,palabraoculta,letrasusadas
def sonido(self,song):
    self.player = QMediaPlayer()
    filepath = os.path.join(os.getcwd()+"\\src\\audio\\", song)
    url = QUrl.fromLocalFile(filepath)
    content = QMediaContent(url)
    self.player.setMedia(content)
    self.player.play()
def reproductor(self,estado = None):
    if estado == "pausa":
        global Reproducir
        if Reproducir:
            self.player.pause()
            self.Volumen.setIcon(QIcon(f"{os.getcwd()}"+"\src\ico\mute.png"))
            Reproducir = False
            return Reproducir
        if not Reproducir:
            self.Volumen.setIcon(QIcon(f"{os.getcwd()}"+"\src\ico\ico.png"))
            self.player.play()
            
            Reproducir = True
            return Reproducir
    if estado == "next":
        song = sortearmusica()
        filepath = os.path.join(os.getcwd()+"\\src\\audio\\"+f"{song}")
        url = QUrl.fromLocalFile(filepath)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
    if estado == None:
        self.player = QMediaPlayer()
        filepath = os.path.join(os.getcwd()+"\\src\\audio\\"+"Song.mp3")
        url = QUrl.fromLocalFile(filepath)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
def sortearmusica():
    lista = ["Song.mp3","Song1.mp3","Song2.mp3","Song3.mp3"]
    tema = lista[random.randint(0,len(lista)-1)]
    return tema