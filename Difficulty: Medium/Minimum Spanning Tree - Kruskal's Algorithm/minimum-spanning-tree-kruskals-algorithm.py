from typing import List

class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        # code here
        class DSU:
            def __init__(self):
                self.parent = [i for i in range(V)]
                self.rank = [0 for i in range(V)]
            
            def find_parent(self, node):
                if node == self.parent[node]:
                    return node
                self.parent[node] = self.find_parent(self.parent[node])
                return self.parent[node]
            
            def union(self, u, v):
                Upar = self.find_parent(u)
                Vpar = self.find_parent(v)
                
                if Upar == Vpar:
                    return
                
                if self.rank[Upar] > self.rank[Vpar]:
                    self.parent[Vpar] = Upar
                elif self.rank[Upar] < self.rank[Vpar]:
                    self.parent[Upar] = Vpar
                else:
                    self.parent[Upar] = Vpar
                    self.rank[Vpar] += 1
        
        dsu = DSU()
        ans = 0
        edges.sort(key=lambda x: (x[2]))
        for startNode, endNode, wt in edges:
            if dsu.find_parent(startNode) == dsu.find_parent(endNode):
                continue
            dsu.union(startNode, endNode)
            ans += wt
        return ans
                    