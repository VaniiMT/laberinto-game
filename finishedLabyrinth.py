import matplotlib.pyplot as plt
import networkx as nx

# Mapa del laberinto
labyrinth = {
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
    "M": [],
    "Salida": []
}
#datillos
dead_ends = ["D", "F", "G", "H", "K", "M"]
MAX_tries = 6

# Estado al empezar
state = {
    "current": "Entrada",
    "discovered": {"Entrada": labyrinth["Entrada"]},
    "tries": 0,
    "game_over": False,
    "win": False
}

def draw():
    plt.clf()  #Limpiar
    #Añadir Nodos al descubrir
    G = nx.DiGraph()
    for room, exits in state["discovered"].items():
        for e in exits:
            G.add_edge(room, e)
    
    # rojo para actual,,azul para otras
    colors = ["red" if n == state["current"] else "lightblue" for n in G.nodes()]
    nx.draw(G, node_color=colors, node_size=1500, font_size=10, edge_color="gray", arrows=True, with_labels=True)
    
    plt.title(f"{state['current']} | Intentos: {state['tries']}/{MAX_tries}") #No funciona idk
    plt.draw()
    plt.pause(0.1) #Esto ayuda actualizar el laberinto

def move_to(room):
    if room not in state["discovered"].get(state["current"], []):
        print("No puedes")
        return
    state["current"] = room
    if room not in state["discovered"]:
        state["discovered"][room] = labyrinth[room][:]
        print(f"descubriste {room}")
    if room in dead_ends:
        state["tries"] += 1
        print(f"Dead end yikes! ({state["tries"]}/{MAX_tries})")
        state["current"] = "Entrada"
        
    if state["current"] == "Salida":
        state["win"] = True
        state["game_over"] = True
        print("ESCAPASTE!")
    elif state["tries"] >= MAX_tries:
        state["game_over"] = True
        print("GAME OVER")
    draw()

print("Comandos: nombre de sala / q=salir")
while not state["game_over"]:
    cmd = input("").strip()
    if cmd == "q":
        break
    elif cmd in state["discovered"].get(state["current"], []):
        move_to(cmd)
    else:
        print("no se puede hacer TP en este juego :sob:")

if state["win"]:
    print("VICTORIA!")
else:
    print("Fin del juego")