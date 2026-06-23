'''Structure for a Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findCommon(self, r1, r2):
        # code here
        def inorder(root, s):
            if root == None:
                return None
            inorder(root.left, s)
            s.add(root.data)
            inorder(root.right, s)
        
        s1 = set()
        s2 = set()
        inorder(r1, s1)
        inorder(r2, s2)
        return sorted(list(s1.intersection(s2)))