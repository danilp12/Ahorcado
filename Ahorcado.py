
from funciones_ahorcado import *
import os,time
run =True
LetraPalabra = []
intentos = 6
ListaAcumulada =[]
ScoreBoard = cargar()
Palabra = str(input("Ingresar la palabra: ")).upper()
if Palabra == "RANDOM":
    Palabra,pista = PalabraRandom()
else:
    pista= input("Ingresar Pista: ")
if Palabra == "SCORE":
    ListarScore()
    run = False
    input("Presione una tecla para Continuar")
for x in range(len(Palabra)):
    LetraPalabra.append(Palabra[x].upper())

LetrasAcertadas = []
for i in range(len(LetraPalabra)):
    x = "_"
    LetrasAcertadas.append(x)
os.system("cls")
while run:
    print("---Iniciando Juego----")
    time.sleep(1)
    print("Juego del Ahorcado")
    nombre = input("Ingrese Su Nombre: ")
    iniciar()
    tiempoinicio = time.time()
    os.system("cls")
    while intentos >0:
        print("---------------Juego del Ahorcado---------------")
        print(f"Pista:{pista}         Tiempo Actual:{tiempo(tiempoinicio)} segundos")
        print("-"*60)
        dibujar(intentos) 
        print("-"*60)
        print(f"Tenes {intentos} intentos restantes!")
        print("Palabra: "+ str(LetrasAcertadas))
        print("-"*60)
        letra = str(input("Ingresar letra: ")).upper()
        if letra.isalpha():
            if len(letra)>1:
                print("Ingresaste mas de una letra!")
                continue
            if letra in list(LetraPalabra):
                if letra not in list(LetrasAcertadas):
                    print("\x1b[1;32m"+f"La letra {letra} es acertada! "+'\033[0;m')
                    intentos +=1
                    cantidad = LetraPalabra.count(letra)
                    print("La letra se repite "+str(cantidad)+" de veces!")
                    posicion = LetraPalabra.index(letra)
                    LetrasAcertadas.pop(posicion)
                    LetrasAcertadas.insert(posicion,letra.upper())
                    if cantidad >1:
                        for j in range (len(LetraPalabra)):
                            if LetraPalabra[j] == letra:
                                LetrasAcertadas.pop(j)
                                LetrasAcertadas.insert(j, letra.upper())
                else:
                    print(f"La letra {letra.upper()} Es correta pero ya la habias usado")
                    intentos +=1
            elif letra in list(ListaAcumulada):
                print(f"La letra {letra.upper()} ya la habias usado antes!")
                ListaAcumulada.append(letra)
                intentos +=1
            elif letra == " ":
                print("El Espacio no esta permitido")
                intentos +=1
            else:
                print("\x1b[1;31m"+f"La letra {letra} es incorrecta!"+'\033[0;m')
                ListaAcumulada.append(letra)
            intentos -=1
            if LetrasAcertadas == LetraPalabra:
                print("-"*60)
                print("\x1b[1;32m"+"Felicidades! Has ganado! :)"+'\033[0;m')
                print("La palabra era: "+"".join(LetraPalabra).upper())
                print("-"*60)
                tiempofin = str(time.time() - tiempoinicio)
                tiempofin = tiempofin[0:4]
                print(f"El tiempo fue de: {tiempofin} segundos")
                puntaje = str((1000-float(tiempofin))*intentos)
                puntaje = puntaje[0:4]
                print(f"Su puntaje es de: {puntaje}")
                print("-"*60)
                try:
                    score = [nombre,intentos,float(tiempofin),Palabra,int(puntaje)]
                    ScoreBoard.append(score)
                except:
                    score = [nombre,intentos,float(tiempofin),Palabra,int(puntaje[0:3])]
                    ScoreBoard.append(score)
                run = False
                guardar(ScoreBoard)
                break
        else:
            print("\x1b[1;31m"+"Solo se pueden ingresar letras"+'\033[0;m')
        
        
    if intentos == 0:
        dibujar(intentos)
        print("-"*60)
        print("Lo siento! Game Over! :'(")
        print(f"la palabra era: {Palabra} ")
        print("-"*60)
        tiempofin = str(time.time() - tiempoinicio)
        tiempofin = tiempofin[0:4]
        print(f"El tiempo fue de: {tiempofin} segundos")
        print("-"*60)
        score = [nombre,intentos,tiempofin,Palabra,0]
        ScoreBoard.append(score)
        guardar(ScoreBoard)
        break
input("Proceso Finalizado - Presione una tecla")

#Comentario test.


