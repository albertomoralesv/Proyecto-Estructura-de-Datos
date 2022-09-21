import random
from time import sleep
import os
from Arbol import arbol

def clear():
    os.system('cls')

def validar(entrada, vi, vf, texto):
    while True:
            if entrada.isnumeric():
                entrada = int(entrada)
                if entrada>vi-1 and entrada<vf+1:
                    return entrada
                    break            
            print("Entrada no valida\n")
            entrada= input(f"{texto}: ")
        
def regresarHijo(nodo,color):
   if color=="rojo":
       if nodo.hijosRojos:
           if len(nodo.hijosRojos)==1:
               numero=0
           else:
               numero = random.randint(0, len(nodo.hijosRojos)-1)
           return(nodo.hijosRojos[numero].valor)
       else:
           if len(nodo.hijosAzules)==1:
               numero=0
           else:
               numero = random.randint(0, len(nodo.hijosAzules)-1) 
           return(nodo.hijosAzules[numero].valor)
   else:
       if nodo.hijosAzules:
           if len(nodo.hijosAzules)==1:
               numero=0
           else:
               numero = random.randint(0, len(nodo.hijosAzules)-1) 
           return(nodo.hijosAzules[numero].valor)
       else:
           if len(nodo.hijosRojos)==1:
               numero=0
           else:
               numero = random.randint(0, len(nodo.hijosRojos)-1)
           return(nodo.hijosRojos[numero].valor)


os.system('cls')
print("Preparando Juego")    
numFrijoles = (random.randint(21,25))
a = arbol(numFrijoles)
clear()
nodoActual = a.raiz.hijo1
turno = 1

print("Elige los jugadores: ")
print("1. Jugador vs Jugador")
print("2. Jugador vs Computadora")
print("3. Computadora vs Computadora")

jugadores = input("\nOpcion: ")
jugadores = validar(jugadores,1,3,"Opción")
print("\n")

print("Quien elige primero?")    
print("1. Seleccion automatica")
print("2. Elegir orden\n")

orden = input("Seleccion: ")
orden = validar(orden, 1, 2, "Seleccion: ")
print("\n")

if orden==1:
    if jugadores == 1:
        p1 = "Jugador1"
        p2 = "Jugador2"
    elif jugadores == 2:
        p1 = "Jugador"
        p2 = "Computadora"
    elif jugadores == 3:
        p1 = "Computadora1"
        p2 = "Computadora2"
else:
    if jugadores == 1:
        print("Quien elige primero?")
        print("1. Jugador1")
        print("2. Jugador2\n")
        primero = input("Primero en elegir: ")
        primero = validar(primero, 1, 2, "Primero en elegir: ")
        if primero==1:
            p2 = "Jugador1"
            p1 = "Jugador2"
        else:
            p1 = "Jugador1"
            p2 = "Jugador2"
    elif jugadores == 2:
        print("Quien elige primero?")
        print("1. Jugador")
        print("2. Computadora\n")
        primero = input("Primero en elegir: ")
        primero = validar(primero, 1, 2, "Primero en elegir: ")
        if primero==1:
            p1 = "Computadora"
            p2 = "Jugador"
        else:
            p1 = "Jugador"
            p2 = "Computadora"
    elif jugadores == 3:
        print("Quien elige primero?")
        print("1. Computadora1")
        print("2. Computadora2\n")
        primero = input("Primero en elegir: ")
        primero = validar(primero, 1, 2, "Primero en elegir: ")
        if primero==1:
            p2 = "Computadora1"
            p1 = "Computadora2"
        else:
            p1 = "Computadora1"
            p2 = "Computadora2"
    
print("\nSelecciona la dificultad del 1 al 10 de las eleecciones de la computadora:")
print("(1. Mayor probabilidad de perder de la computadora)")
print("(10. Mayor probabilidad de ganar de la computadora)")
dificultad = input("\nDificultad: ")
dificultad = validar(dificultad,1,10,"Dificultad")
print("\n")

sleep(1)
os.system('cls')    
print("El juego va a empezar")
    
while numFrijoles>0:
    sleep(2)
    os.system('cls')    
    print("Turno: ",turno)
    if turno%2!=0:
        print("Turno de:",p2)
        jugadorActual = p2
    else:
        print("Turno de:",p1)
        jugadorActual = p1
    print("Numero de Frijoles:", numFrijoles)
    
    print()
    if "Jugador" in jugadorActual:
        print("Que quieres hacer?")
        print("1. Seleccion manual")
        print("2. Seleccion automatica\n")
        seleccion = input("Seleccion: ")
        seleccion = validar(seleccion,1,2,"Seleccion")
    
        if seleccion==1:
            frijolesTomados = input("Elige cuantos frijoles tomar (min: 1, max: 3): ")
            if numFrijoles>3:
                maxfrijoles=3
            else:
                maxfrijoles=numFrijoles
            frijolesTomados = validar(frijolesTomados,1,maxfrijoles,"Elige cuantos frijoles tomar: ")
        
        if seleccion==2:
            probabilidad = random.randint(2, 10)
            if probabilidad>dificultad:
                if jugadorActual==p1:
                    frijolesTomados = numFrijoles-regresarHijo(nodoActual, "rojo")
                else:
                    frijolesTomados = numFrijoles-regresarHijo(nodoActual, "azul")
            else:
                if jugadorActual==p1:
                    frijolesTomados = numFrijoles-regresarHijo(nodoActual, "azul")
                else:
                    frijolesTomados = numFrijoles-regresarHijo(nodoActual, "rojo")
            if frijolesTomados==1:
                print(f"\nLa computadora a elegido {frijolesTomados} frijol por ti.")
            else:
                print(f"\nLa computadora a elegido {frijolesTomados} frijoles por ti.")
            sleep(3)
                    
    if "Computadora" in jugadorActual:
        probabilidad = random.randint(2, 10)
        if probabilidad>dificultad:
            if jugadorActual==p1:
                frijolesTomados = numFrijoles-regresarHijo(nodoActual, "rojo")
            else:
                frijolesTomados = numFrijoles-regresarHijo(nodoActual, "azul")
        else:
            if jugadorActual==p1:
                frijolesTomados = numFrijoles-regresarHijo(nodoActual, "azul")
            else:
                frijolesTomados = numFrijoles-regresarHijo(nodoActual, "rojo")
        sleep(1)
        if frijolesTomados==1:
            print(f"\nLa {jugadorActual} a elegido {frijolesTomados} frijol.")
        else:
            print(f"\nLa {jugadorActual} a elegido {frijolesTomados} frijoles.")
        sleep(3)
                
    
    if frijolesTomados==1:
        nodoActual = nodoActual.hijo1
    elif frijolesTomados==2:
        nodoActual = nodoActual.hijo2
    elif frijolesTomados==3:
        nodoActual = nodoActual.hijo3
        
    numFrijoles = numFrijoles-frijolesTomados
    turno+=1

sleep(2)
clear()
sleep(1)
if jugadorActual==p1:
    print(f"Gana {p2}")
else:
    print(f"Gana {p1}")    