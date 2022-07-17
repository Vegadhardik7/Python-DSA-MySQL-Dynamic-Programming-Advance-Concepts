from Queue_using_linked_list import LinkedQueue
import numpy as np
class Graph:
    def __init__(self, vertices):
        self._adjMat = np.zeros((vertices, vertices))
        self._vertices = vertices

    def insert_edge(self, u, v, w=1):             # w : weights
        self._adjMat[u][v] = w

    def delete_edge(self, u, v):
        self._adjMat[u][v] = 0

    def get_edge(self, u, v):
        return self._adjMat[u][v]

    def vertices_count(self):
        return self._vertices

    def edges_count(self):
        cnt = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if not self._adjMat[i][j] == 0:
                    cnt += 1
        return cnt

    def indegree(self, u):
        cnt = 0
        for i in range(self._vertices):
            if not self._adjMat[i][u] == 0:
                cnt += 1
        return cnt

    def outdegree(self, u):
        cnt = 0
        for i in range(self._vertices):
            if not self._adjMat[u][i] == 0:
                cnt += 1
        return cnt

    def display(self):
        print(self._adjMat)

    def BFS(self, source):
        i = source
        q = LinkedQueue()
        visited = [0] * self._vertices
        print(i, end = " - ")
        visited[i] = 1
        q.enqueue(i)

        while not q.is_empty():
            i = q.dequeue()
            for j in range(self._vertices):
                if self._adjMat[i][j] == 1 and visited[j] == 0:
                    print(j , end=" - ")
                    visited[j] = 1
                    q.enqueue(j)

G = Graph(7)              # Graph of 7 vertices
G.insert_edge(0,1)
G.insert_edge(0,5)
G.insert_edge(0,6)
G.insert_edge(1,0)
G.insert_edge(1,2)
G.insert_edge(1,5)
G.insert_edge(1,6)
G.insert_edge(2,3)
G.insert_edge(2,4)
G.insert_edge(2,6)
G.insert_edge(3,4)
G.insert_edge(4,2)
G.insert_edge(4,5)
G.insert_edge(5,2)
G.insert_edge(5,3)
G.insert_edge(6,3)
G.BFS(0)