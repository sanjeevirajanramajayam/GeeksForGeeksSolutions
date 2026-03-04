#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        distArray = [float('inf') for i in range(V)]
        distArray[src] = 0
        for i in range(V - 1):
            for j in range(len(edges)):
                startNode, endNode, wt = edges[j]
                if distArray[startNode] + wt < distArray[endNode]:
                    distArray[endNode] = distArray[startNode] + wt
            # print(distArray)
        for j in range(len(edges)):
            startNode, endNode, wt = edges[j]
            if distArray[startNode] + wt < distArray[endNode]:
                distArray[endNode] = distArray[startNode] + wt
                return [-1]
        for i in range(len(distArray)):
            if distArray[i] == float('inf'):
                distArray[i] = int(10e7)
        return distArray