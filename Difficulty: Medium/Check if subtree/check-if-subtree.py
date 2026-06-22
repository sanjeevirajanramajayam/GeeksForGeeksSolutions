'''
Structure of a Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSubTree(self, root, subRoot):
        # code here
        def isSameTree(root1, root2):
            if root1 == None:
                return root1 == root2
            if root2 == None:
                return root1 == root2
            return root1.data == root2.data and isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        
        def preorder(root):
            if root == None:
                return

            if isSameTree(root, subRoot) is True:
                return True
            
            if preorder(root.left) is True:
                return True
            
            if preorder(root.right) is True:
                return True

            return False
        return preorder(root)