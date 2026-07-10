from collections import deque
class Solution:
	def isCycle(self, V, edges):
	    adj = [[] for i in range ((V))]
	    for startNode, endNode in (edges):
	        adj[startNode].append(endNode)
	        adj[endNode].append(startNode)

        def dfs(i, parent):
            # ans.append(i)
            visited.add(i)
            for node in adj[i]:
                if node != parent and node in visited:
                    return True
                if node not in visited:
                    if dfs(node, i):
                        return True
            return False
                    
        visited = set()
        ans = []
        
        for i in range(len(adj)):
            if i not in visited:
                if dfs(i, -1):
                    return True
        return False