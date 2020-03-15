"""
Ejercicio 1, incisos a y b
Implementación del método de César, donde se prueban todas las llaves posibles
para encontrar un mensaje legible
Autores: Páes Alcalá Alma Rosa y Valderrama Silva Alejandro Tonatiuh
Fecha: Febrero 2020
"""

alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
NUM_ALFABETO = len(alphabet)
renglon1 = list("XNXAFNIIYNLNWSKBRGETQPZIIRXVMZHINNYABÑOFGMAUVUUXVI")
renglon10 = list("XNXAF")
renglon2 = list("PXUKANBVNLQXBZDNJLDBJQBJTJUDRNABQVAJIXV")
renglon3 = list("GOTVZÑOVÑZTLWGVTFTONJTWGNÑAIOIFDLGOIBÑSGLITNILWTLFG")
renglon4 = list("DZBNJDNLEMMWDFAWKOJYWQLRFGDFLDDZDFUIHCDZLLIG")


#Mensaje a descifrar
mensaje = renglon2

for k in range(0,NUM_ALFABETO):
    print("Llave: " + str(k))
    claro = []
    for m in mensaje:
        num = alphabet.index(m)
        #print(num)
        #num = num - 65
        #print(num)
        num = num - k
        modulo = num % NUM_ALFABETO
        newNumber = modulo
        #print(newNumber)
        claro.append(alphabet[newNumber])
    print(claro)