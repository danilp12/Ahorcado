import json, random, time
from re import T
from prettytable import PrettyTable

def cargar():
    with open("ScoreBoard.json","r") as file:
        ScoreBoard = list(json.load(file))
        return ScoreBoard
def guardar(ScoreBoard):
        with open ("ScoreBoard.json","w")as f:
            json.dump(ScoreBoard,f)
            print("Guardado con Exito")
def dibujar(intentos):
    if intentos == 6:
        print("")
    elif intentos == 5:
        print("\x1b[1;31m"+"        O"+'\033[0;m') 
    elif intentos ==4:
        print("\x1b[1;31m"+"""        O
        |"""+'\033[0;m')
    elif intentos == 3:
        print("\x1b[1;31m"+"""         O
        /|"""+'\033[0;m')
    elif intentos == 2:
        print("\x1b[1;31m"+"""         O
        /|\\"""+'\033[0;m')
    elif intentos == 1:
        print("\x1b[1;31m"+"""         O
        /|\\
        /"""+'\033[0;m')
    else:
        print("\x1b[1;31m"+"""         O
        /|\\
        / \\"""+'\033[0;m')
              
def ListarScore():
    tabla = PrettyTable()
    with open("ScoreBoard.json","r") as file:
        ScoreBoard = list(json.load(file))
        
        tabla.field_names =["Nombre","Intentos Restantes","Tiempo (Seg)","Palabra","Puntaje"]
        for i in range(len(ScoreBoard)):
            tabla.add_row(ScoreBoard[i])
        tabla.sortby="Puntaje"
        tabla.reversesort=True
        
        print(tabla)
def PalabraRandom():
    listado = ["pelota","paleta","pileta","ventana","palindromo","celular","algoritmo","Auriculares"]
    pistas =["Objeto que rebota","Se usa para jugar con una pelota","Lugar para refrescarse","Abertura de una vivienda","Palabra que se lee de derecho y reves","Dispositivo Movil","Conjunto de instrucciones de programacion","Accesorio para escuchar musica"]
    num = random.randint(0,len(listado)-1)
    return listado[num].upper(), pistas[num]
def iniciar():
    con = 3
    while con != 0:
        print(f"Iniciando en {con}")
        time.sleep(1)
        con -=1
def tiempo(a):
    t = str(time.time() - a)
    t = t[0:4]
    return t

