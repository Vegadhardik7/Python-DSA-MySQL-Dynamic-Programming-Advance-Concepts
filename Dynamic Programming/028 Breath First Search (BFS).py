'''

Python3 Program to print BFS traversal from a given source vertex.
BFS(int s) traverses vertices list representation

'''


# This class represents a directed graph using adjacency list representation
from collections import defaultdict
class Graph:
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edget to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # function to print a BFS of graph
    def BFS(self,s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph)+1)

        queue = [] # Create queue for BFS

        # Mark the source node as visited and enqueue it
        queue.append(s)

        visited[s] = True

        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end = " ")
            # Get all adjacent vertices of the dequeued vertex s.
            # if a adjacent has not been visited, then make it visited and enqueue it

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

g.BFS(1)