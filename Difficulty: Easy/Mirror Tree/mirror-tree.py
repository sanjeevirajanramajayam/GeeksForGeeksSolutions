'''
class Node:
    def _init_(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def mirror(self, root):
        # code here
        def preorder(root):
            if root == None:
                return None
            
            temp = root.left
            root.left = root.right
            root.right = temp
        
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return root