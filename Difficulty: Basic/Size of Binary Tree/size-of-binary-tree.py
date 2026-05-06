"""
Definition for Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
class Solution:
    def getSize(self, root):
        # code here
        cnt = 0
        def traverse(root):
            nonlocal cnt
            if root == None:
                return None
            cnt += 1
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return cnt