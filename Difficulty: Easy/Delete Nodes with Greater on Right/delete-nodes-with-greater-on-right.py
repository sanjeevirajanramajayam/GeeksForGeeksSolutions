'''
Structure of linked list node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        # code here
        currMax = float('-inf')
        
        prev = None
        curr = head
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        
        
        prev2 = None
        newHead = prev
        while prev:
            if prev.data >= currMax:
                currMax = prev.data
                prev2 = prev
                prev = prev.next
            else:
                # print(prev.data)
                prev2.next = prev.next
                prev = prev2.next
        
        prev = None
        curr = newHead
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        return prev