class Node:
    def __init__(self, key):
        self.key    = key
        self.left   = None 
        self.right  = None   
class Tree:
   
    def create_node(self,key):
        return Node(key)
    
    def insert(self, node, key):
        if node is None:
            return self.create_node(key)
        else:
            node.left = self.insert(node.left, key)
        return node
    
    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print(node.key)
            self.inorder(node.right)
    
    def preorder(self, node):
        if node is not None:
            print(node.key)
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):
        if node is not None: 
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key)
