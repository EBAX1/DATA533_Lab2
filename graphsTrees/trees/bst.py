from node import Node
from tree import Tree

class BST(Tree):
    
    def search_node(self,node,key):
        if node is None:
            return False
        if node.key == key:
            return True
        if node.key<key:
            return self.search_node(node.right,key)
        else:
            return self.search_node(node.left,key)
