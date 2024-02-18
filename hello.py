class UndirectedGraph:
    def __init__(self, size):
        self.size = size
        self.graph = [[] for _ in range(size)]

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * self.size
        queue = [s]
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def DFSrecursionfunction(self, v, visited):
        visited.append(v)
        print(v, end=' ')
        for nextItem in self.graph[v]:
            if nextItem not in visited:
                self.DFSrecursionfunction(nextItem, visited)

    def DFS(self, v):
        visited = [[]]
        self.DFSrecursionfunction(v, visited)


if __name__ == '__main__':
    g = UndirectedGraph(10)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print("here is bfs")
    g.BFS(1)
    print('\n','\bhere it is dfs')
    g.DFS(2)
    print()
