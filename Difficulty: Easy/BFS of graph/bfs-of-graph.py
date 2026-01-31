class Solution:
    def bfs(self, adj):
        # code here
        visited = [0] * len(adj)
        queue = deque([0])
        visited[0] = 1
        bfs = []
        while queue:
            node = queue.popleft()
            bfs.append(node)
            for i in adj[node]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = 1
        return bfs