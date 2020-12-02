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

Methods:

addEdge
- Input: integers i, j
- adds an edge from vertex i to vertex j. Fails if there is no vertex i or j
- Example: G.addEdge(0,2) adds edge from vertex 0 to vertex 2

addVertex
- Input: None
- Adds a vertex n to a graph of size n
- Example: G.addVertex(). If G has 4 vertices [0,1,2,3] will add vertex labelled 4

rmEdge
- Input: integers i,j
- Removes the edge between vetex i and vertex j
- Example: G.rmEdge(0,1) removes edge between vertex 0 and vertex 1

printGraph
- Input: None
- Prints the edge set and vertex set of the graph

adjMatrix
- Input: None
- Returns the adjacency matrix of the graph

DFS
- Input: integer i
- Performs a depth first search on the graph starting from vertex i

isConnected
- Input: None
- Returns True if the graph is connected, false otherwise

hasCycles
- Input: None
- Returns True if the graph has cycles, false otherwise

### wtGraphs.py

Contains the wtGraph class for weighted graphs. Inherits from Graph class

Inputs:
- vertices: as in Graph
- edges: as in Graph
- weights: A list of numbers, where weights[i] is the weight of edge edges[i]

Methods:

All methods from Graph class

adjMatrix
- Input: None
- Modifies adjMatrix function from Graph class to include weights

kruskal
- Input: None
- Performs Kruskals algorithm for a minimal spanning tree. Returns a list of edges that form this tree

totalWeight
- Input: None
- Gives the sum of all the weights of a graph| G.totalWeight()
