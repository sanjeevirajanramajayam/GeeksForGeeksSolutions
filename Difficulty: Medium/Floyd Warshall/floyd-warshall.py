#User function template for Python

class Solution:
	def floydWarshall(self, dist):
		#Code here
		for i in range(len(dist)):
            for j in range(len(dist)):
		        if dist[i][j] == 100000000:
		            dist[i][j] = float('inf')
		for via in range(len(dist)):
		    for i in range(len(dist)):
		        for j in range(len(dist)):
		            dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])
		for i in range(len(dist)):
            for j in range(len(dist)):
		        if dist[i][j] == float('inf'):
		            dist[i][j] = 100000000
	    return dist