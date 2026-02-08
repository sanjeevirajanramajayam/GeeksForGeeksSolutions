class Solution:
    def isCyclic(self, V, edges):
        # code here
        adjList = [[] for i in range(V + 1)]
        
        for startNode, endNode in edges:
            adjList[startNode].append(endNode)

        # print(adjList)
        
        visited = [0 for i in range(V + 1)]
        pathAlong = [0 for i in range(V + 1)]
        
        def dfsCheck(node):
            visited[node] = 1
            pathAlong[node] = 1
            for i in adjList[node]:
                if not visited[i]:
                    if dfsCheck(i):
                        return True
                if pathAlong[i]:
                    return True
            pathAlong[node] = 0
            return False
        
        for i in range(len(visited)):
            if not visited[i]:
                if dfsCheck(i):
                    return True
        
        return False
                
                
        
        # def dfsCheck(node):
        #     visited[node] = 1
        #     for i rnage