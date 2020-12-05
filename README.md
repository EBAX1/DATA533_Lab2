# DATA533_Lab2
Eric Baxter and Aditya Saluja Lab 2

## Graphs Subpackage
This sub-package contains two modules, one for un-weighted graphs and one for weighted graphs. 

### Graphs.py

Contains the Graph class for un-weighted graphs. 
Inputs:
- vertices: A positive integer n representing the number of vertices in the graph. 
- edges: A list of two element lists. Element [i,j] represents an edge from vertex i to vertex j (un-weighted, undirected)

The class implements the following methods:

addEdge
- Input: integers i, j
- adds an edge from vertex i to vertex j. Raises an error if there is no vertex i or j
- Usage: g.addEdge(0,4) adds edge from vertex 0 to vertex 4

addVertex
- Input: Takes no argument
- Adds a vertex n to a graph of size n
- Usage: g.addVertex(). If G has 4 vertices [0,1,2,3] will add vertex labeled 4

rmEdge
- Input: integers i,j
- Removes the edge between vertex i and vertex j
- Usage: g.rmEdge(1,3) removes edge between vertex 1 and vertex 3

adjMatrix
- Input: Takes no argument
- Returns the adjacency matrix of the graph

DFS
- Input: integer i
- Performs a depth first search on the graph starting from vertex i

isConnected
- Input: Takes no argument
- Returns True if the graph is connected, false otherwise

hasCycles
- Input: Takes no argument
- Returns True if the graph has cycles, false otherwise

printGraph
- Input: Takes no argument
- Prints the edge set and vertex set of the graph

### wtGraphs.py

The module contains the wtGraph class for weighted graphs. Inherits from Graph class

Inputs:
- vertices: as in Graph
- edges: as in Graph
- weights: A list of numbers, where weights[i] is the weight of edge edges[i]

Methods:

Inherits all methods from Graph class and adds the following:

adjMatrix
- Input: None
- Modifies adjMatrix function from Graph class to include weights

kruskal
- Input: None
- Performs Kruskal's algorithm for a minimal spanning tree. Returns a list of edges that form this tree

totalWeight
- Input: None
- Gives the sum of all the weights of a graph| g.totalWeight()
