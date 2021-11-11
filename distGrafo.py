# Cristian Aurelio Ramirez Anzaldo A01066337

from collections import defaultdict
from pyvis.network import Network
import math


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.dist = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # functon to set distance
    def setDist(self, u, dist):
        self.dist[u] = dist

    def getDist(self, u):
        return self.dist[u]

    def bfs_dist(self, s):
        queue = []

        for u in self.graph:
            self.setDist(u, math.inf)

        self.setDist(s, 0)

        queue.append(s)

        while queue:
            s = queue.pop(0)

            for i in self.graph[s]:
                if self.getDist(i) == math.inf:
                    queue.append(i)
                    self.setDist(i, self.getDist(s) + 1)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


network = Network()

nodes = [j for j in range(28)]
network.add_nodes(nodes)

places = {0: "El Rosario",
          1: "Instituto del Petroleo",
          2: "Deportivo 18 de Marzo",
          3: "Martin Carrera",
          4: "La Raza",
          5: "Consulado",
          6: "Tacuba",
          7: "Guerrero",
          8: "Garibaldi",
          9: "Oceania",
          10: "Hidalgo",
          11: "Bellas Artes",
          12: "Morelos",
          13: "San Lazaro",
          14: "Balderas",
          15: "Salto del Agua",
          16: "Pino Suarez",
          17: "Candelaria",
          18: "Tacubaya",
          19: "Centro Medico",
          20: "Chabacano",
          21: "Jamaica",
          22: "Panititlan",
          23: "Santa Anita",
          24: "Mixcoac",
          25: "Zapata",
          26: "Ermita",
          27: "Atlalilco"}


g = Graph()

# 0: "El Rosario"
g.addEdge(0, 1)
network.add_edge(0, 1)
g.addEdge(0, 6)
network.add_edge(0, 6)

# 1: "Instituto del Petroleo",
g.addEdge(1, 0)
network.add_edge(1, 0)
g.addEdge(1, 4)
network.add_edge(1, 4)
g.addEdge(1, 2)
network.add_edge(1, 2)

# 2: "Deportivo 18 de Marzo",
g.addEdge(2, 1)
network.add_edge(2, 1)
g.addEdge(2, 4)
network.add_edge(2, 4)
g.addEdge(2, 3)
network.add_edge(2, 3)

# 3: "Martin Carrera",
g.addEdge(3, 2)
network.add_edge(3, 2)
g.addEdge(3, 5)
network.add_edge(3, 5)

# 4: "La Raza",
g.addEdge(4, 1)
network.add_edge(4, 1)
g.addEdge(4, 2)
network.add_edge(4, 2)
g.addEdge(4, 5)
network.add_edge(4, 5)

# 5: "Consulado",
g.addEdge(5, 3)
network.add_edge(5, 3)
g.addEdge(5, 4)
network.add_edge(5, 4)
g.addEdge(5, 12)
network.add_edge(5, 12)
g.addEdge(5, 9)
network.add_edge(5, 9)

# 6: "Tacuba",
g.addEdge(6, 0)
network.add_edge(6, 0)
g.addEdge(6, 10)
network.add_edge(6, 10)
g.addEdge(6, 18)
network.add_edge(6, 18)

# 7: "Guerrero",
g.addEdge(7, 4)
network.add_edge(7, 4)
g.addEdge(7, 8)
network.add_edge(7, 8)
g.addEdge(7, 10)
network.add_edge(7, 10)

# 8: "Garibaldi",
g.addEdge(8, 7)
network.add_edge(8, 7)
g.addEdge(8, 11)
network.add_edge(8, 11)
g.addEdge(8, 12)
network.add_edge(8, 12)

# 9: "Oceania",
g.addEdge(9, 5)
network.add_edge(9, 5)
g.addEdge(9, 13)
network.add_edge(9, 13)
g.addEdge(9, 22)
network.add_edge(9, 22)

# 10: "Hidalgo",
g.addEdge(10, 6)
network.add_edge(10, 6)
g.addEdge(10, 7)
network.add_edge(10, 7)
g.addEdge(10, 14)
network.add_edge(10, 14)
g.addEdge(10, 11)
network.add_edge(10, 11)

# 11: "Bellas Artes",
g.addEdge(11, 10)
network.add_edge(11, 10)
g.addEdge(11, 8)
network.add_edge(11, 8)
g.addEdge(11, 15)
network.add_edge(11, 15)
g.addEdge(11, 16)
network.add_edge(11, 16)

# 12: "Morelos",
g.addEdge(12, 8)
network.add_edge(12, 8)
g.addEdge(12, 5)
network.add_edge(12, 5)
g.addEdge(12, 13)
network.add_edge(12, 13)
g.addEdge(12, 17)
network.add_edge(12, 17)

# 13: "San Lazaro",
g.addEdge(13, 12) # Morelos
network.add_edge(13, 12)
g.addEdge(13, 9) # Oceania
network.add_edge(13, 9)
g.addEdge(13, 17) # Candelaria
network.add_edge(13, 17)
g.addEdge(13, 22) # Pantitlan
network.add_edge(13, 22)

# 14: "Balderas",
g.addEdge(14, 18) #Tacubaya
network.add_edge(14, 18)
g.addEdge(14, 10) # Hidalgo
network.add_edge(14, 10)
g.addEdge(14, 15)
network.add_edge(14, 15)
g.addEdge(14, 19) # Centro Medico
network.add_edge(14, 19)

# 15: "Salto del Agua",
g.addEdge(15, 11)
network.add_edge(15, 11)
g.addEdge(15, 14)
network.add_edge(15, 14)
g.addEdge(15, 16)
network.add_edge(15, 16)
g.addEdge(15, 20)
network.add_edge(15, 20)

# 16: "Pino Suarez",
g.addEdge(16, 15)
network.add_edge(16, 15)
g.addEdge(16, 11)
network.add_edge(16, 11)
g.addEdge(16, 17)
network.add_edge(16, 17)
g.addEdge(16, 20)
network.add_edge(16, 20)

# 17: "Candelaria",
g.addEdge(17, 12)
network.add_edge(17, 12)
g.addEdge(17, 16)
network.add_edge(17, 16)
g.addEdge(17, 13)
network.add_edge(17, 13)
g.addEdge(17, 21)
network.add_edge(17, 21)

# 18: "Tacubaya",
g.addEdge(18, 6)
network.add_edge(18, 6)
g.addEdge(18, 14)
network.add_edge(18, 14)
g.addEdge(18, 19)
network.add_edge(18, 19)
g.addEdge(18, 24)
network.add_edge(18, 24)

# 19: "Centro Medico",
g.addEdge(19, 14)
network.add_edge(19, 14)
g.addEdge(19, 18)
network.add_edge(19, 18)
g.addEdge(19, 20)
network.add_edge(19, 20)
g.addEdge(19, 25)
network.add_edge(19, 25)

# 20: "Chabacano",
g.addEdge(20, 19)
network.add_edge(20, 19)
g.addEdge(20, 15)
network.add_edge(20, 15)
g.addEdge(20, 16)
network.add_edge(20, 16)
g.addEdge(20, 21)
network.add_edge(20, 21)
g.addEdge(20, 23)
network.add_edge(20, 23)
g.addEdge(20, 26)
network.add_edge(20, 26)

# 21: "Jamaica",
g.addEdge(21, 20)
network.add_edge(21, 20)
g.addEdge(21, 17)
network.add_edge(21, 17)
g.addEdge(21, 22)
network.add_edge(21, 22)
g.addEdge(21, 23)
network.add_edge(21, 23)

# 22: "Panititlan",
g.addEdge(22, 21)
network.add_edge(22, 21)
g.addEdge(22, 13)
network.add_edge(22, 13)
g.addEdge(22, 9)
network.add_edge(22, 9)


# 23: "Santa Anita",
g.addEdge(23, 20)
network.add_edge(23, 20)
g.addEdge(23, 21)
network.add_edge(23, 21)
g.addEdge(23, 27)
network.add_edge(23, 27)

# 24: "Mixcoac",
g.addEdge(24, 18)
network.add_edge(24, 18)
g.addEdge(24, 25)
network.add_edge(24, 25)

# 25: "Zapata",
g.addEdge(25, 24)
network.add_edge(25, 24)
g.addEdge(25, 19)
network.add_edge(25, 19)
g.addEdge(25, 26)
network.add_edge(25, 26)

# 26: "Ermita",
g.addEdge(26, 25)
network.add_edge(26, 25)
g.addEdge(26, 20)
network.add_edge(26, 20)
g.addEdge(26, 27)
network.add_edge(26, 27)

# 27: "Atlalilco
g.addEdge(27, 26)
network.add_edge(27, 26)
g.addEdge(27, 23)
network.add_edge(27, 23)

place_selected = 0
g.bfs_dist(place_selected)

network.toggle_physics(True)
network.show('mygraph.html')
network.show_buttons(filter_=['physics'])

print("Distances from " + places[place_selected] + "\n")

for i in places:
    print(places[place_selected] + " -> " + places[i] + "   " + str(g.dist[i]))
print("\n" + str(g.dist))
# This code is contributed by Neelam Yadav
