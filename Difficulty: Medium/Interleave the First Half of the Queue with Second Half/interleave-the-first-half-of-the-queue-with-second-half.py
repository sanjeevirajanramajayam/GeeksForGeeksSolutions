class Solution:
    def rearrangeQueue(self, q):
        #code here 
        g1 = deque([])
        g2 = deque([])
        n = len(q)
        for i in range(len(q)//2):
            g1.append(q.popleft())
        while q:
            g2.append(q.popleft())
        ans = []
        # print(g1, g2)
        for i in range(n//2):
            x1 = g1.popleft()
            x2 = g2.popleft()
            # print(x1, x2)
            q.append(x1)
            q.append(x2)
        # q = list(q)
        # print(q)
        # print(ans)
        # return list(q)