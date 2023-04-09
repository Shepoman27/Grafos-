import networkx as nx

G = nx.DiGraph()
camino3 = [""]
#Espacio para nodos

nodos_G = ['a','b','c','d','f','g'] #Creamos los nodos
G.add_nodes_from(nodos_G) #Añadimos los nodos al grapho



#Espacio aristas

#Creamos las uniones que existen entre todos los nodos
lados_G = [('a','b',5),('b','c',6),('b','f',7),('b','e',8),('c','d',9),('c','f',10),('c','g',11),('e','g',12),('e','c',13),('d','f',14),('f','g',15)]
G.add_weighted_edges_from(lados_G) #Agregamos dichas uniones al grafo
G.size()


# Encontramos el camino más corto desde el nodo 'a' a todos los demás nodos utilizando el algoritmo de Dijkstra
distancia, camino = nx.single_source_dijkstra(G, 'a')


hay_letra = False
# Imprimimos las distancias y los caminos más cortos desde el nodo 'a' a todos los demás nodos
for nodo in distancia:

    print('Distancia desde "a" hasta "{}": {}'.format(nodo, distancia[nodo]))
    print('Camino desde "a" hasta "{}": {}'.format(nodo, camino[nodo]))

            




edge_colors = ['black' if e == ('a', 'b') else 'black' for e in G.edges()]
nx.draw_circular(G, with_labels=True, node_color='red', edge_color=edge_colors)