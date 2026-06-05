'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        fast = head
        slow = head
        cnt = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = slow.next
                cnt += 1
                while fast != slow:
                    slow = slow.next
                    cnt += 1
                return cnt
        return cnt
                