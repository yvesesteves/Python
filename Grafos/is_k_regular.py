import matplotlib.pyplot as plt
import networkx as nx

G = nx.cycle_graph(6)  # Cada vértice tem grau 2
fig, ax = plt.subplots()
nx.draw_circular(G, with_labels=True, node_color='lightblue', node_size=1000, ax=ax)
ax.set_title("Grafo 2-Regular: Ciclo com 6 vértices")
print("\n---------------------------------------\nExemplo 1:")
plt.show()

print("Grafo G é 2-regular?", nx.is_k_regular(G, 2))  # Esperado: True
print("Grau de cada nó em G:", dict(G.degree()))


R = nx.random_regular_graph(d=3, n=6)  # Gera grafo aleatório 3-regular com 6 nós
fig, ax = plt.subplots()
nx.draw(R, with_labels=True, node_color='lightgray', node_size=1000, ax=ax)
ax.set_title("Grafo Aleatório 3-Regular")
print("\n---------------------------------------\nExemplo 3:")
plt.show()

print("Grafo R é 3-regular?", nx.is_k_regular(R, 3))  # Esperado: True
print("Grau de cada nó em R:", dict(R.degree()))


H = nx.Graph()
H.add_edges_from([
    (0, 1), (0, 2), (1, 2),  # Nós 0, 1 e 2 têm grau 2
    (3, 4)                   # Nós 3 e 4 têm grau 1
])
fig, ax = plt.subplots()
nx.draw(H, with_labels=True, node_color='salmon', node_size=1000, ax=ax)
print("\n---------------------------------------\nExemplo 4:")
ax.set_title("Grafo Não k-Regular")
plt.show()

print("Grafo H é 2-regular?", nx.is_k_regular(H, 2))  # Esperado: False
print("Grau de cada nó em H:", dict(H.degree()))



