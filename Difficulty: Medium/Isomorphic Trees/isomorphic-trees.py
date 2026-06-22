'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    def isIsomorphic(self, p, q): 
        def isSame(p, q):
            if p == None:
                return p == q
            if q == None:
                return p == q
            return p.data == q.data and ((isSame(p.right, q.right)  and isSame(p.left, q.left))  or (isSame(p.right, q.left) and isSame(p.left, q.right))) 
        return isSame(p, q)