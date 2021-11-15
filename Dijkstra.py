'''
Cristian Aurelio Ramirez Anzaldo
Dijkstra
A01066337
'''

import math

class Graph:
    def __init__(self, vertices, places):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.P = places

    def print_solution(self, origin, dist):
        print("Shortest distances from: ", self.P[origin])
        for node in range(self.V):
            print(self.P[origin], "-> ", self.P[int(node)], "=", dist[node])

    def min_distance(self, dist, visited):
        # infinite as max number
        min = math.inf
        min_index = 0
        # Checking every distance in the node
        for v in range(self.V):
            if dist[v] < min and visited[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, origin):
        dist = [math.inf] * self.V
        dist[origin] = 0
        visited = [False] * self.V

        for node in range(self.V):
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and visited[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(origin, dist)


# Places in the image
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


g = Graph(len(places), places)
        #   0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27
g.graph = [[0, 6, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0 El rosario
           [6, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 1 Instituo del Petroleo
           [0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 2 Deportivo 18 de marzo
           [0, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 3 Martin Carreta
           [0, 2, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 4 La raza
           [0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 5 Consulado
           [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 6 Tacuba
           [0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 7 Guerrero
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 8 Garibaldi
           [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0], # 9 Oceania
           [0, 0, 0, 0, 0, 0, 7, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 10 Hidalgo
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 11 Bellas Artes
           [0, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 12 Morelos
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0], # 13 San Lazaro
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 6, 3, 0, 0, 0, 0, 0, 0, 0, 0], # 14 Balderas
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0], # 15 Saldo del Agua
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0], # 16 Pino Suarez
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0], # 17 Candelaria
           [0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0], # 18 Tacubaya
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 2, 0, 0, 0, 0, 4, 0, 0], # 19 Centro Medico
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 0, 0, 2, 0, 1, 0, 2, 0, 0, 6, 0], # 20 Chabacano
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 5, 1, 0, 0, 0, 0], # 21 Jamaica
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0], # 22 Panititlan
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 6], # 23 Santa Anita
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0], # 24 Mixcoac
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 3, 0, 3, 0], # 25 Zapata
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 3, 0, 2], # 26 Ermita
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 2, 0]] # 27 Atlalilco
          # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27



g.dijkstra(0)