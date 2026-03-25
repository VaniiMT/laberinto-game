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
def encontrar_salida(laberinto, inicio, salida, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    if inicio == salida:
        return [inicio]
    for vecino in laberinto.get(inicio, []):
        if vecino not in visitados:
            camino = encontrar_salida(laberinto, vecino, salida, visitados)
            if camino:
                return [inicio] + camino
    visitados.remove(inicio)
    return None

camino = encontrar_salida(Laberinto, "Entrada", "Salida")
print("Camino encontrado:", camino)





