from collections import defaultdict, deque
class Solution:
    def findOrder(self, words):
        # code here
        inorder = {}
        for word in words:
            for ch in word:
                inorder[ch] = 0
        adjList = defaultdict(list)
        
        for i in range(1, len(words)):
            word2 = words[i]
            word1 = words[i-1]
            
            if len(word1) > len(word2):
                flag = True
                j = 0
                while j < len(word2):
                    if word1[j] != word2[j]:
                        flag = False
                        break
                    j += 1
                if flag:
                    return ""
        
            length = min(len(word1), len(word2))
            j = 0
            while j < length:
                if word1[j] != word2[j]:
                    if word2[j] not in adjList[word1[j]]:
                        adjList[word1[j]].append(word2[j])
                        inorder[word2[j]] += 1
                    break
                j += 1
        
        # print(adjList, inorder)
        # return "abcd"
        queue = deque([])
        for i in inorder:
            if inorder[i] == 0:
                queue.append(i)
        # queue = deque()
        ans = ""
        while queue:
            node = queue.popleft()                    
            ans += (node)

            for nnode in adjList[node]:
                inorder[nnode] -= 1
                if inorder[nnode] == 0:
                    queue.append(nnode)
        # print(ans)
        if len(ans) != len(inorder):
            return ""
        return ans