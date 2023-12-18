#para probar primero ejecutar en el terminal:
#$pip install networkx
#$pip install matplotlib
import networkx as nx
import matplotlib.pyplot as grafico 

# Función para visualizar la centralidad de vector propio con un tono rojo más oscuro
def centralidadEnColores(graph, title):
    # Calcular la centralidad de vector propio
    eigenvector_centrality = nx.eigenvector_centrality(graph)

    nodes = graph.nodes()
    valores = [eigenvector_centrality[node] for node in nodes]

    # Dibujar el grafo con colores basados en la centralidad de vector propio
    grafico.figure(figsize=(10, 8))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=800,
            node_color=valores, cmap=grafico.cm.Reds, vmin=0, vmax=0.8, edge_color='gray')
    grafico.title(title)
    grafico.show()

# Función para encontrar los tres nodos con la mayor centralidad de vector propio
def top3YUltimos3Centralidad(graph):
    centralidadesLista = nx.eigenvector_centrality(graph)
    nodosOrdenadosMayores = sorted(centralidadesLista, key=centralidadesLista.get, reverse=True)
    nodosOrdenadosMenores = sorted(centralidadesLista, key=centralidadesLista.get)
    top3 = nodosOrdenadosMayores[:3]
    ultimos3 = nodosOrdenadosMenores[:3]
    return top3, ultimos3

#Karate Club
KarateClub = nx.karate_club_graph()
nx.draw_networkx(KarateClub)
grafico.show()

#Florentine Families
FlorentineFamilies = nx.florentine_families_graph()
nx.draw_networkx(FlorentineFamilies)
grafico.show()

# Visualizar el grafo con nodos coloreados según la centralidad de vector propio (rojo oscuro)
centralidadEnColores(KarateClub, 'Centralidad Vector Propio - Karate Club')

# Visualizar el grafo con nodos coloreados según la centralidad de vector propio (rojo oscuro)
centralidadEnColores(FlorentineFamilies, 'Centralidad Vector Propio - Florentine Families')

top3Karate, ultimos3Karate = top3YUltimos3Centralidad(KarateClub)
print("Top3 KarateClub:", top3Karate, "Ultimos 3 KarateClub: ",  ultimos3Karate)

top3Florentine,ultimos3Florenitnes = top3YUltimos3Centralidad(FlorentineFamilies)
print("Top3 Florentine: ", top3Florentine, "Ultimos 3 Florentine: ",  ultimos3Florenitnes)