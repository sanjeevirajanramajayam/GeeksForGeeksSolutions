class Solution:
    def dfs(self, adj):
        # code here
        def dfs(i):
            ans.append(i)
            visited.add(i)
            for node in adj[i]:
                if node not in visited:
                    dfs(node)
                    
        visited = set()
        ans = []
        
        for i in range(len(adj)):
            if i not in visited:
                dfs(i)
        return ans