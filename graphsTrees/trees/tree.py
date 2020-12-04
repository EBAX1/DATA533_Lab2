from node import Node 

class Tree:
   
    def create_node(self,key):
        return Node(key)
    
    def insert(self, node, key):
        if node is None:
            return self.create_node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        return node
    
    def traverse_inorder(self,root):
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.key)
            self.traverse_inorder(root.right)
    
    def traverse_preorder(self, root):
        if root is not None:
            print(root.key)
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)
    
    def traverse_postorder(self, root):
        if root is not None: 
            self.traverse_postorder(root.left)
            self.traverse_postorder(root.right)
            print(root.key)