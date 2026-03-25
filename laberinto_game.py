#numero de fallos permitidos para laberinto con función factorial

from math import factorial


def fallos_permitidos(dead_ends):
    n = dead_ends
    return factorial(n)

def calcular_fallos(fallos, n):
    if fallos >= fallos_permitidos:
        print("Has alcanzado el número máximo de fallos. Fin del juego.")
        return True
    

def registrar_fallo(n):
    fallos = 0
    ########lo que se cuenta como fallo
    print(f"Fallo {fallos} de {fallos_permitidos}")
    return registrar_fallo  


laberinto = {
    'Entrada':["A","B"],
    'A' : ["C","D"],
    "B" : ["E","F"],
    "C" : ["G,H"],
    "D" : [],
    "E" : ["I","K"],
    "F" : [],
    "G" : [],
    "H" : [],
    "I" : ["L","M"],
    "M" : [],
    "L" : ["SALIDA"]
}

