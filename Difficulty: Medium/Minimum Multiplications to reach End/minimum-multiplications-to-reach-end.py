from collections import deque
class Solution:
    def minSteps(self, arr, start, end):
        # code here
        visited = [False] * 1001 
        queue = deque([(start, 0)])
        while queue:
            num, ops = queue.popleft()
            if num == end:
                return ops
            for x in arr:
                newNum = (num * x) % 1000
                if visited[newNum] is False:
                    queue.append((newNum, ops + 1))
                    visited[newNum] = True
        return -1