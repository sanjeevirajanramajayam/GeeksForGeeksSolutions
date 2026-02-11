import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        adjList = [[] for i in range((V))]
        for startNode, endNode, weight in edges:
            adjList[startNode].append((endNode, weight))
            adjList[endNode].append((startNode, weight))
        
        pq = []
        heapq.heappush(pq, (0, src))
        
        distList = [float('inf') for i in range(V)]
        distList[src] = 0
        
        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distList[node]:
                continue
            for newNode, weight in adjList[node]:
                # print(dist, weight, distList[newNode])
                if dist + weight < distList[newNode]:
                    distList[newNode] = dist + weight
                    heapq.heappush(pq, (distList[newNode], newNode))
        
        return distList