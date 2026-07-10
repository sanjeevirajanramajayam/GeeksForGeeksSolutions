from collections import deque
class Solution:
	def isCycle(self, V, edges):
		#Code here
		def bfs(node, parent):
		    queue = deque([(node, parent)])
		    while queue:
		       node, parent = queue.popleft()
		       for i in adjList[node]:
		          # bfs(i, node)
		          if i != parent and i in visited:
		              return True
		          
		          if i not in visited:
		              #bfs(i, node)
		              queue.append((i, node))
		              visited.add(i)
		    return False
		    
		adjList = [[] for i in range(V)]
		visited = set([])
		for startNode, endNode in edges:
		    adjList[startNode].append(endNode)
		    adjList[endNode].append(startNode)
		
		for i in range(V):
		    if i not in visited:
		        visited.add(i)
		        if bfs(i, -1) == True:
		            return True
		
		return False