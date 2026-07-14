from collections import defaultdict, deque
class Solution:
    def findOrder(self, words):
        # code here
        inorder = {}
        adjList = defaultdict(list)
        
        for word in words:
            for ch in word:
                inorder[ch] = 0
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            if len(word1) > len(word2):
                same = True
                j = 0
                while j < len(word2):
                    if word1[j] != word2[j]:
                        same = False
                        break
                    j += 1
                if same:
                    return ""
                    
            length = min(len(word1), len(word2))
            j=0
            while j < length:
                if word1[j] != word2[j]:
                    if word2[j] not in adjList[word1[j]]:
                        adjList[word1[j]].append(word2[j])
                        inorder[word2[j]] += 1
                    break
                j += 1
        # print(adjList, inorder)
        # return ""
        visited = set()
        queue = deque([])
        for x in inorder:
            if inorder[x] == 0:
                queue.append(x)
                # visited.add(x)
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for x in adjList[node]:
                # if x not in visited:
                inorder[x] -= 1
                if inorder[x] == 0:
                    queue.append(x)
                    # visited.add(x)
        if len(ans) != len(inorder):
            return ""
        # print(ans)
        return "".join(ans)
        