"""
Ejercicio 1, incisos a y b
Implementación del método de César, donde se prueban todas las llaves posibles
para encontrar un mensaje legible
Autores: Páes Alcalá Alma Rosa y Valderrama Silva Alejandro Tonatiuh
Fecha: Febrero 2020
"""

from utils import *
import math

alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
NUM_ALFABETO = len(alphabet)
renglon1 = list("XNXAFNIIYNLNWSKBRGETQPZIIRXVMZHINNYABÑOFGMAUVUUXVI")
renglon3 = list("GOTVZÑOVÑZTLWGVTFTONJTWGNÑAIOIFDLGOIBÑSGLITNILWTLFG")
renglon4 = list("DZBNJDNLEMMWDFAWKOJYWQLRFGDFLDDZDFUIHCDZLLIG")


#Mensaje a descifrar
mensaje = renglon1
m = mensaje[0]

llavesA = []
llavesB = []


for k in range(0,NUM_ALFABETO):
    claro = []
    newNumber = 0
    num = alphabet.index(m)
    num = num - k #c-b
    divisores = divisors(num)
    for d in divisores:
        inverso = inverse(d,NUM_ALFABETO)
        if inverso is None:
            continue
        else:
            print("Llave 1: " + str(inverso))
            print("Llave 2: " + str(k))
            llavesA.append(inverso)
            llavesB.append(k)
 
    