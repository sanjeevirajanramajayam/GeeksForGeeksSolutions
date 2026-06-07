'''
class Node:
    def __init__(self, d):
        self.data=d
        self.bottom=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        # code here
        dummy = Node(-1)
        head = dummy
        def merge(l1, l2):
            dummy = Node(-1)
            head = dummy
            while l1 and l2:
                if l1.data <= l2.data:
                    dummy.bottom = l1
                    l1 = l1.bottom
                    dummy = dummy.bottom
                else:
                    dummy.bottom = l2
                    l2 = l2.bottom
                    dummy = dummy.bottom
                    
            while l1:
                dummy.bottom = l1
                l1 = l1.bottom
                dummy = dummy.bottom
                
            while l2:
                dummy.bottom = l2
                l2 = l2.bottom
                dummy = dummy.bottom
            return head.bottom
        cnt = 0
        while root:
            dummy = merge(dummy, root)
            # return dummy
            root = root.next

        return head.bottom