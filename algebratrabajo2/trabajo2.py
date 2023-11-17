#Uso la librería networkx para el hacer el algoritmo de Louvain y matplot para visualizar.
#para probar primero ejecutar en el terminal:
#$pip install community
#$pip install  python-louvain
#$pip install networkx
#$pip install matplotlib
from community import community_louvain
import networkx as nx
import matplotlib.pyplot as grafico 
import matplotlib.cm as graficoacolor

# Definimos las aristas del grafo o red:
aristasGrafo = [(1,2),(1,3),(1,4),(1,5),(1,6),(2,7),(2,8),(2,9),(2,10),(2,11),(2,12),(2,13),(2,14),(4,42),(4,45),(4,51),(4,52)]
GrafoNuevo = nx.Graph()
GrafoNuevo.add_edges_from(aristasGrafo)

# Devuelve la mejor particion en un listado o diccionario:
mejorParticion = community_louvain.best_partition(GrafoNuevo)

# Visualizamos los datos
posicion  = nx.spring_layout(GrafoNuevo)
cmap = graficoacolor.get_cmap('viridis', max(mejorParticion.values()) + 1) 

#pintamos los nodos de colores según la partición en la que esté
nx.draw_networkx_nodes(GrafoNuevo, posicion, mejorParticion.keys(), node_size=100,cmap=cmap, node_color=list(mejorParticion.values()))
nx.draw_networkx_edges(GrafoNuevo, posicion, alpha=0.5) 
grafico.title('Particiones Usando el algoritmo de Louvain')

grafico.show()
