#numero de fallos permitidos para laberinto con función factorial

from math import factorial
Laberinto = {
    "Entrada": ["A", "B"],
    "A": ["C", "D"],
    "B": ["E", "F"],
    "C": ["G", "H"],
    "D": [],
    "E": ["I", "K"],
    "F": [],
    "G": [],
    "H": [],
    "I": ["L", "M"],
    "K": [],
    "L": ["Salida"],
    "M": []
}
def dfs(Laberinto,posicion_actual,visitados=None):
    if visitados is None:
        visitados = set()
    
    visitados.add(posicion_actual)
    print(f"visitando la posicion:{posicion_actual}")
    if Laberinto[posicion_actual] == "Salida":
         print("Has salido yupi")
         return True

    for vecino in Laberinto[posicion_actual]:
        if vecino not in visitados:
            if dfs[Laberinto, vecino, visitados]:
                return True
    return False
dfs[Laberinto, "Entrada"]
def fallos_permitidos(dead_ends):
    n = dead_ends
    return factorial(n)
#---------------------------------------------------------------

def calcular_fallos(fallos, n):
    if fallos >= fallos_permitidos:
        print("Has alcanzado el número máximo de fallos. Fin del juego.")
        return True
    
def registrar_fallo(n):
    fallos = 0
    ########lo que se cuenta como fallo
    print(f"Fallo {fallos} de {fallos_permitidos}")
    return registrar_fallo  

def encontrar_salida(Laberinto, inicio, salida, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    if inicio == salida:
        return [inicio]
    for vecino in Laberinto.get(inicio, []):
        if vecino not in visitados:
            camino = encontrar_salida(Laberinto, vecino, salida, visitados)
            if camino:
                return [inicio] + camino
    visitados.remove(inicio)
    return None

camino = encontrar_salida(Laberinto, "Entrada", "Salida")
print("Camino encontrado:", camino)

