#User function Template for python3

from typing import List
from collections import deque

class Solution:

    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
    
        adjList = [[] for i in range(V)]
        inDegree = [0 for i in range((V))]
        
        for startNode, endNode, weight in edges:
            adjList[startNode].append((endNode, weight))
            inDegree[endNode] += 1
        
        topo_sort = deque([])
        # visited = [-1 for i in range((V))] 
        
        queue = deque([])
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            topo_sort.append(node)
            for i in adjList[node]:
                inDegree[i[0]] -= 1
                if inDegree[i[0]] == 0:
                    queue.append(i[0])
        
        distArray = [float('inf') for i in range((V))]
        distArray[0] = 0
        
        while topo_sort:
            node = topo_sort.popleft()
            for newNode, weight in adjList[node]:
                if distArray[newNode] > distArray[node] + weight:
                    distArray[newNode] = distArray[node] + weight
        
        for i in range(len(distArray)):
            if distArray[i] == float('inf'):
                distArray[i] = -1
        
        return distArray
                
        return []