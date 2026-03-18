#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        # code here
        aPoints = set()
        visited = [0 for i in range(V)]
        tin = [0 for i in range(V)]
        low = [0 for i in range(V)]
        time = 0
        def dfs(i, parent):
            nonlocal time
            visited[i] = 1
            tin[i] = low[i] = time
            time += 1
            children = 0
            for newNode in adj[i]:
                if newNode != parent:
                    if not visited[newNode]:
                        children += 1
                        dfs(newNode, i)
                        low[i] = min(low[i], low[newNode])
                        if low[newNode] >= tin[i] and parent != -1:
                            aPoints.add(i)
                    else:
                        low[i] = min(low[i], tin[newNode])
            if children > 1 and parent == -1:
                aPoints.add(i)

        for i in range(V):
            if not visited[i]:
                dfs(i, -1)
                
        if aPoints == set():
            return [-1]
        
        return sorted(list(aPoints))