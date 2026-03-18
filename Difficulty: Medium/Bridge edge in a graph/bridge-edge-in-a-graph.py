class Solution:
    def isBridge(self, V, edges, c, d):
        # code here 
        visited = set()
        time = 0
        adjList = [[] for i in range(V)]
        timeArr = [0 for i in range(V)]
        low = [0 for i in range(V)]
        
        for startNode, endNode in edges:
            adjList[startNode].append(endNode)
            adjList[endNode].append(startNode)

            
        def dfs(i, parent):
            nonlocal time
            visited.add(i)
            timeArr[i] = time
            low[i] = time
            time += 1
            for newNode in adjList[i]:
                if newNode == parent:
                    continue
                if newNode in visited:
                    low[i] = min(low[i], timeArr[newNode])
                else:
                    if dfs(newNode, i) == True:
                        return True
                    low[i] = min(low[i], low[newNode])
                    if low[newNode] > timeArr[i]:
                        if (i == c and newNode == d) or (newNode == c and i == d):
                            return True
            return False
            
        for i in range(V):
            if i not in visited:
                if dfs(i, -1):
                    return True
        return False
            