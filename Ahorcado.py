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
    nombre = input("Ingrese Su Nick: ")
    tiempoinicio = time.time()
    while intentos >0:
        print(f"Pista:{pista}")
        dibujar(intentos)
        print(f"Tenes {intentos} intentos restantes!")
        print("Palabra: "+ str(LetrasAcertadas))
        letra = str(input("Ingresar letra: ")).upper()
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
            print("\x1b[1;32m"+"Felicidades! Has ganado! :)"+'\033[0;m')
            print("La palabra era: ")
            print("".join(LetraPalabra).upper())
            tiempofin = str(time.time() - tiempoinicio)
            tiempofin = tiempofin[0:4]
            print(f"El tiempo fue de: {tiempofin}")
            puntaje = str((1000-float(tiempofin))*intentos)
            puntaje = puntaje[0:4]
            print(f"Su puntaje es de: {puntaje}")
            score = [nombre,intentos,float(tiempofin),Palabra,int(puntaje)]
            ScoreBoard.append(score)
            run = False
            guardar(ScoreBoard)
            break
        
        
    if intentos == 0:
        dibujar(intentos)
        print("Lo siento! Game Over! :'(")
        print(f"la palabra era: {Palabra} ")
        tiempofin = str(time.time() - tiempoinicio)
        tiempofin = tiempofin[0:4]
        print(f"El tiempo fue de: {tiempofin}")
        score = [nombre,intentos,tiempofin,Palabra,0]
        ScoreBoard.append(score)
        guardar(ScoreBoard)
        break
input("Proceso Finalizado - Presione una tecla")

#Comentario test.