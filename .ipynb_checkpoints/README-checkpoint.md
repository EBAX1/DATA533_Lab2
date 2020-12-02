# DATA533_Lab2
Eric Baxter and Aditya Saluja Lab 2

## Graphs Subpackage
This subpackage contains two modules, one for unweighted graphs and one for weighted graphs. 
Both are implemented in a user friendly and intuitive way that does not require knowledge of adjacency lists or adjacency matrices.

### Graphs.py

Contains the Graph class for unweighted graphs. 
Inputs:
- vertices: an integer (n) representing the number of vertices in the graph. vertices will be labelled from 0 to n-1
- edges: A list of two element lists. Element [i,j] represents an edge from vertex i tp vertex j (unweighted, undirected)

Functions:

Function Name|Inputs|Use|Example
---|---|---
addEdge|integers i, j| adds an edge from vertex i to vertex j. Fails if there is no vertex i or j|G.addEdge(0,2) adds edge from vertex 0 to vertex 2
addVertex|None|adds a vertex n to a graph of size n|G.addVertex(). If G has 4 vertices [0,1,2,3] will add vertex labelled 4
rmEdge|integers i,j| Removes the edge between vetex i and vertex j| G.rmEdge(0,1) removes edge between vertex 0 and vertex 1
printGraph|None|Prints the edge set and vertex set of the graph| G.printGraph()
adjMatrix|None| Returns the adjacency matrix of the graph| G.adjMatrix()
DFS| integer i| Performs a depth first search on the graph starting from vertex i | G.DFS(0)
isConnected| None| Returns True if the graph is connected, false otherwise| G.isConnected()
hasCycles| None | Returns True if the graph has cycles, false otherwise| G.hasCycles()

### wtGraphs.py

Contains the wtGraph class for weighted graphs. Inherits from Graph class
Inputs:
- vertices: as in Graph
- edges: as in Graph
- weights: A list of numbers, where weights[i] is the weight of edge edges[i]

Functions:

All from Graph, plus: 

Function Name|Inputs|Use|Example
---|---|---
adjMatrix|None| Modifies adjMatrix function from Graph class to include weights| G.adjMatrix()
kruskal|None| Performs Kruskals algorithm for a minimal spanning tree. Returns a list of edges that form this tree| G.kruskal()
totalWeight| None| Gives the sum of all the weights of a graph| G.totalWeight()