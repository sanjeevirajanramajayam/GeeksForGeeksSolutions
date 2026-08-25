class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        pq = [(0, 0, -1)]
              #wt  #node    #parent    
        visited = set()
        ans = 0
        adjList = [[] for i in range(V)]
        for startNode, endNode, wt in edges:
            adjList[startNode].append((endNode, wt))
            adjList[endNode].append((startNode, wt))

        while pq:
            wt, node, parent = heapq.heappop(pq)
            if node in visited:
                continue
            ans += wt
            visited.add(node)
            for nnode, nwt in adjList[node]:
                heapq.heappush(pq, (nwt, nnode, node))
        return ans