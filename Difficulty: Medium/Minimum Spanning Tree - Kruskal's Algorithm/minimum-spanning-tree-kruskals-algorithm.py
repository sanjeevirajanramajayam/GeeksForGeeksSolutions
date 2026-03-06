#User function Template for python3
from typing import List

class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        # code here
        class DSU:
            def __init__(self):
                self.rank = [0 for i in range(V)]
                self.parent = [i for i in range(V)]
                self.totalWt = 0

            def find_parent(self, node):
                if node == self.parent[node]:
                    return node
                self.parent[node] = self.find_parent(self.parent[node])
                return self.parent[node]
            
            def union(self, x, y, wt):
                xP = self.find_parent(x)
                yP = self.find_parent(y)
                
                if xP == yP:
                    return 
                self.totalWt += wt
                if self.rank[xP] > self.rank[yP]:
                    self.parent[yP] = xP
                elif self.rank[xP] < self.rank[yP]:
                    self.parent[xP] = yP
                else:
                    self.parent[xP] = yP
                    self.rank[yP] += 1
        
        dsu = DSU()
        
        edges = sorted(edges, key=lambda x: x[2])
        
        for startNode, endNode, wt in edges:
            dsu.union(startNode, endNode, wt)
        
        return dsu.totalWt