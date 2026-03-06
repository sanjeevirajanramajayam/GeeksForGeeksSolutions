import heapq
class Solution:
    def spanningTree(self, V, edges):
        # code here
        visited = [ 0 for i in range(V)]
        mst_edges = []
        pq = [(0, 0, -1)]
        totalWt = 0
        adjList = [[] for i in range(V)]
        
        for startNode, endNode, wt in edges:
            adjList[startNode].append((endNode, wt))
            adjList[endNode].append((startNode, wt))
            
        while pq:
            wt, node, parent = heapq.heappop(pq)
            
            if visited[node] == 1:
                continue
            
            visited[node] = 1
            totalWt += wt
            
            if parent != -1:
                mst_edges.append((parent, node, wt))
            
            for newNode, dist in adjList[node]:
                if visited[newNode] != 1:
                    heapq.heappush(pq, (dist, newNode, node))
        # print(mst_edges)
        return totalWt