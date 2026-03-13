class Solution:

    def kosaraju(self, V, edges):
        # code here
        
        adj = [[] for i in range(V)]
        
        for startNode, endNode in edges:
            adj[startNode].append(endNode)
            
        visited = [0 for i in range(V)]

        stack = []
        def dfs(node, adj):
            visited[node] = 1
            for newNode in adj[node]:
                if not visited[newNode]:
                    dfs(newNode, adj)
            stack.append(node)
            
        for i in range(V):
            if not visited[i]:
                dfs(i, adj)

        adj2 = [[] for i in range(V)]
        
        for startNode in range(V):
            for node in adj[startNode]:
                adj2[node].append(startNode)
        
        cnt = 0
        visited = [0 for i in range(V)]
        while stack:
            i = stack.pop()
            if not visited[i]:
                dfs(i, adj2)
                cnt += 1
        return cnt