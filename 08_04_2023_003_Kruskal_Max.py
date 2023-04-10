import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo con pesos
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=8)
G.add_edge('C', 'D', weight=7)
G.add_edge('D', 'E', weight=9)
G.add_edge('E', 'F', weight=10)
G.add_edge('F', 'G', weight=2)
G.add_edge('G', 'H', weight=1)
G.add_edge('H', 'A', weight=8)
G.add_edge('B', 'H', weight=11)
G.add_edge('H', 'I', weight=7)
G.add_edge('I', 'C', weight=2)
G.add_edge('I', 'G', weight=6)
G.add_edge('C', 'F', weight=4)
G.add_edge('D', 'F', weight=14)

# Obtenemos el Árbol de Máximo Kruskal
T = nx.maximum_spanning_tree(G)

# Dibujamos el grafo original y el árbol resultante
pos = nx.spring_layout(G)  #Distribuimos los nodos graficamente
nx.draw_networkx_nodes(G, pos, node_color='w') #Dibujamos los nodos del grafo
nx.draw_networkx_edges(G, pos, edge_color='k') #Dibujamos las aristas del grafos
nx.draw_networkx_labels(G, pos) #Dibujamos el peso de cada arista
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, label_pos=0.3)
nx.draw_networkx_edges(T, pos, edge_color='r', width=2)
plt.axis('off') #Eliminamos los ejes de la figura
plt.show()