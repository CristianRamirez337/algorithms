# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
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
    def setDist(self, u, v, dist):
        self.dist[u][v] = dist

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

nodes = [j for j in range(4)]
network.add_nodes(nodes)

g = Graph()
g.addEdge(0, 1)
network.add_edge(0, 1)
g.addEdge(0, 2)
network.add_edge(0, 2)
g.addEdge(1, 2)
network.add_edge(1, 2)
g.addEdge(2, 0)
network.add_edge(2, 0)
g.addEdge(2, 3)
network.add_edge(2, 3)
g.addEdge(3, 3)
network.add_edge(3, 3)



network.toggle_physics(True)
network.show('mygraph.html')
network.show_buttons(filter_=['physics'])

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)
print(g.graph)

# This code is contributed by Neelam Yadav
