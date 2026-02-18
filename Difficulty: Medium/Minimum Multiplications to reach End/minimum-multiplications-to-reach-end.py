#User function Template for python3

from typing import List
from collections import deque
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        
        queue = deque([(0, start)])
        distArray = [float('inf') for i in range(100000)]
        distArray[start] = 0
        while queue:
            stops, num = queue.popleft()
            for i in arr:
                mul = (i * num) % 100000
                if stops + 1 < distArray[mul]:
                    distArray[mul] = stops + 1
                    queue.append((stops + 1, mul))
        
        if distArray[end] == float('inf'):
            return -1
        
        return distArray[end]