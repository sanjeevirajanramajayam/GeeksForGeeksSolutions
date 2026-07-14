from collections import deque
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        adjList = [[] for i in range(V)]
        for startNode, endNode, wt in edges:
            adjList[startNode].append((endNode, wt))
            adjList[endNode].append((startNode, wt))
        pq = [(0, src)]
        dist = [float('inf')] * V
        dist[src] = 0
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for nei, wt in adjList[node]:
                # print(nei, wt)
                if d + wt < dist[nei]:
                    dist[nei] = d + wt
                    heapq.heappush(pq, (d + wt, nei))
                    # print(dist)
            # print(pq)
        # return 
        # print(dist)
        return dist