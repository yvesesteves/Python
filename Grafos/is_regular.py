import networkx as nx
import matplotlib.pyplot as plt

G = nx.cycle_graph(6)
nx.draw_circular(G, with_labels=True)
plt.title("Grafo ciclo com 6 vértices (grau 2)")
plt.show()

print("Regular?", nx.is_regular(G))


H = nx.Graph()
H.add_edges_from([
    (0, 1), (0, 2), (1, 2),  # Parte do grafo com vértices de grau 2
    (3, 4),  # Esses dois têm grau 1
])
nx.draw(H, with_labels=True)
plt.title("Grafo não regular")
plt.show()

print("É regular?", nx.is_regular(H))


DG = nx.DiGraph()
DG.add_edges_from([(0, 1), (1, 2), (2, 0)])

pos = nx.circular_layout(DG)  # Layout em círculo
nx.draw(DG, pos, with_labels=True, node_color='lightgreen', node_size=1000,
        arrows=True, arrowstyle='->', arrowsize=20, edge_color='gray')

plt.title("Grafo Direcionado Regular (grau de entrada e saída = 1)")
plt.show()

print("Grafo direcionado é regular?", nx.is_regular(DG))