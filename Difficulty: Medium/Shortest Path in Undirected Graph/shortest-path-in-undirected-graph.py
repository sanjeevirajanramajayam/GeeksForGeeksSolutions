class Solution:
    def shortestPath(self, V, edges, src):
        # code here
        adjList = [[] for i in range(V)]
        for startNode, endNode in edges:
            adjList[startNode].append(endNode)
            adjList[endNode].append(startNode)
            
        distArray = [float('inf') for i in range(V)]
        
        queue = deque([])
        queue.append((src, 0))
        
        distArray[src] = 0
        
        while queue:
            node, dist = queue.popleft()
            newDist = dist + 1
            for i in adjList[node]:
                if newDist < distArray[i]:
                    distArray[i] = newDist
                    queue.append((i, newDist))
        
        for i in range(len(distArray)):
            if distArray[i] == float('inf'):
                distArray[i] = -1
            
        return distArray