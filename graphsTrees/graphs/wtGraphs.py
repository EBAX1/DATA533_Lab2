#Vertices and edges as above. weights must be a list of numbers of same length as edge set, and applies 
#Weights to edges in index-wise fashion
import numpy as np
import pandas as pd

import graphsTrees.graphs.graphs as gr

class wtGraph(gr.Graph):
    def __init__(self, vertices, edges, weights):
        gr.Graph.__init__(self, vertices, edges)
        self.weights = weights
        for i in weights:
            try:
                float(i)
            except:
                raise TypeError('Weights must be numbers')
        
    #Adjust the adjMatrix function to incorperate weights
    def adjMatrix(self): # Gives the adjacency matrix of the graph. Used in other functions
        #Make an n by n zero matrix
        matrix = np.zeros(len(self.vertices)*len(self.vertices)).reshape(len(self.vertices), len(self.vertices))
        for edge in self.edges:
            matrix[edge[0]][edge[1]] = self.weights[self.edges.index(edge)] #Graph is undirected and weighted
            matrix[edge[1]][edge[0]] = self.weights[self.edges.index(edge)]
        return matrix
    
    # I couldn't figure this out, and the code doesn't work when the graph has cycles.
    # Using the hasCycles method in a loop proved too much for my brain 
    def kruskal(self):
        vertices = self.vertices
        kruskEdges = self.edges
        kruskWeights = self.weights
        tree = []
        if self.isConnected() == True:
            while len(tree) < len(vertices) - 2:
                #This is a horrible way of  using the index from the weights list in the edges list
                #If adding the edge makes a cycle, just remove it. else, add to tree
                if wtGraph(len(vertices), tree + [edges[weights.index(min(weights))]], weights).hasCycles():
                    edges.remove(edges[weights.index(min(weights))])
                    weights.remove(min(weights))
                else:
                    tree.append(edges[weights.index(min(weights))])
                    edges.remove(edges[weights.index(min(weights))])
                    weights.remove(min(weights))
            #This adds the last edge
            tree.append(edges[weights.index(min(weights))])
            return tree
        else:
            print('Graph is disconnected, and there is no spanning tree')
    

    def totalWeight(self):
        return sum(self.weights)