class Solution:
    def topoSort(self, V, edges):
        # Code here
        
        adjList = [[] for i in range(V)]
        
        for startNode, endNode in edges:
            adjList[startNode].append(endNode)
        
        visited = [-1 for i in range(V)]
        topo_sort = []
        res = []
        
        def dfs(node):
            visited[node] = 1
            for i in adjList[node]:
                if visited[i] == -1:
                    dfs(i)
            topo_sort.append(node)
        
        for i in range(V):
            if visited[i] == -1:
                dfs(i)
            
        return topo_sort[::-1]