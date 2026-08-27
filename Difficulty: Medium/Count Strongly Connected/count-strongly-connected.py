class Solution:

    def kosaraju(self, V, edges):
        # code here
        
        adj = [[] for i in range(V)]
            
        for startNode, endNode in edges:
            adj[startNode].append(endNode)
            
        visited = set()
        stack = []
        def dfs(node, adj):
            nonlocal stack
            visited.add(node)
            for nnode in adj[node]:
                if nnode not in visited:
                     dfs(nnode, adj)
            stack.append(node)
        
        for i in range(V):
            if i not in visited:
                dfs(i, adj)
        
        adjList2 = [[] for i in range(V)]
        
        for node in range(V):
            for nnode in adj[node]:
                adjList2[nnode].append(node)
        
        visited = set()
        ans = 0
        while stack:
            pop = stack.pop()
            if pop not in visited:
                ans += 1
                dfs(pop, adjList2)
        return ans
        