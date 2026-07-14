class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        dist = [float('inf') for i in range(V)]
        dist[src] = 0
        adjList = [[] for i in range(V)]
        for startNode, endNode, wt in edges:
            adjList[startNode].append((endNode, wt))
        
        for _ in range(V - 1):
            for startNode, endNode, wt in edges:
                if dist[startNode] != float('inf') and dist[startNode] + wt < dist[endNode]:
                    dist[endNode] = dist[startNode] + wt
        
        for _ in range(1):
            for startNode, endNode, wt in edges:
                if dist[startNode] != float('inf') and dist[startNode] + wt < dist[endNode]:
                    return [-1]
        
        newDist = []
        for x in dist:
            if x == float('inf'):
                newDist.append(10 ** 8)
                continue
            newDist.append(x)
        
        return newDist