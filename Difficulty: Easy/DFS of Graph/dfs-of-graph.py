class Solution:
    def dfs(self, adj):
        # code here
        visited = [0] * len(adj)
        visited[0] = 1
        dfs = []
        def DepthSearch(node):
            visited[node] = 1
            dfs.append(node)
            
            for i in adj[node]:
                if not visited[i]:
                    DepthSearch(i)
        
        DepthSearch(0)
        
        return dfs