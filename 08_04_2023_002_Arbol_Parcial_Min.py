import networkx as nx
import matplotlib.pyplot as plt

# Creamos el grafo con sus aristas y pesos
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'H', weight=8)
G.add_edge('B', 'C', weight=8)
G.add_edge('B', 'H', weight=11)
G.add_edge('C', 'D', weight=7)
G.add_edge('C', 'F', weight=4)
G.add_edge('C', 'I', weight=2)
G.add_edge('D', 'E', weight=9)
G.add_edge('D', 'F', weight=14)
G.add_edge('E', 'F', weight=10)
G.add_edge('F', 'G', weight=2)
G.add_edge('G', 'H', weight=1)
G.add_edge('G', 'I', weight=6)
G.add_edge('H', 'I', weight=7)

# Realizamos el algoritmo de Prim para encontrar el árbol de expansión mínima
T = nx.minimum_spanning_tree(G)

# Mostramos el árbol resultante
pos = nx.spring_layout(G) #Distribuimo los nodos graficamente
nx.draw_networkx_nodes(G, pos, node_color='w') #Dibujamos los nodos del grafo
nx.draw_networkx_edges(G, pos, edge_color='k') #Dibujamos las aristas del grafos
nx.draw_networkx_labels(G, pos) #Dibujamos el peso de cada arista
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, label_pos=0.3) #Dibujamos las aristas del arbol minimo
nx.draw_networkx_edges(T, pos, edge_color='r', width=2)
plt.axis('off') #Eliominamos lops ejes de la figura
plt.show() #Mostramos la figuta