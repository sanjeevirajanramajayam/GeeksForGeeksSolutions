'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        # code here
        def fn(root):
            if (root == None):
                # print("None")
                return True
                
            if (not root.left and not root.right):
                # print("No Children")
                return True
            
            # print(root.data)

            
            leftval = 0
            rightval = 0
                
            if (root.left):
                leftval = root.left.data
                
            
            if (root.right):
                rightval = root.right.data
                
            # print(root.data == leftval + rightval , fn(root.left) , (root.right))
                
                
            return root.data == leftval + rightval and fn(root.left) and fn(root.right)
            
        return fn(root)