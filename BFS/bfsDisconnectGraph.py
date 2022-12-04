'''
Generic Function for BFS traversal of a Graph
(valid for directed as well as undirected graphs
which can have multiple disconnected components)
-- Inputs --
-> V - represents number of vertices in the Graph
-> adj[] - represents adjacency list for the Graph
-- Output --
-> bfs_traversal - a vector containing bfs traversal
for entire graph
'''


# This code is contributed by Abhijeet Kumar(abhijeet19403)


# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.

# This class represents a directed graph
# using adjacency list representation
from collections import defaultdict


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph

    def bfsOfGraph(v, adj):

        bfs_traversal = []
        vis = [False] * v
        for i in range(v):

            # To check if already visited
            if (vis[i] == False):
                q = []
                vis[i] = True
                q.append(i)

                # BFS starting from ith node
                while (len(q) > 0):
                    g_node = q.pop(0)

                    bfs_traversal.append(g_node)
                    for it in adj[g_node]:
                        if (vis[it] == False):
                            vis[it] = True
                            q.append(it)

        return bfs_traversal

# Driver code


# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.bfsOfGraph(2)

# This code is contributed by Neelam Yadav
