from collections import deque
class Solution:
	def isCycle(self, V, edges):
		#Code here
		adjList = [[] for i in range(V + 1)]
		
		for i in range(1, len(edges)):
		    adjList[edges[i][0]].append(edges[i][1])
		    adjList[edges[i][1]].append(edges[i][0])
		    
		visited = [0 for i in range(V + 1)]
		    
		def bfs(givenNode):
    		queue = deque([(givenNode, -1)])
    		visited[givenNode] = 1

    		while queue:
    		    node, parent = queue.popleft()
    		    for neighbour in adjList[node]:
    		        if neighbour != parent and visited[neighbour] == 1:
    		          #  print(node, neighbour, parent)
    		            return True
    		        if not visited[neighbour]:
        		        queue.append((neighbour, node))
        		        visited[neighbour] = 1
        	return False
        
        for i in range(1, V + 1):
            if not visited[i]:
                if bfs(i):
                    return True
	
        return False