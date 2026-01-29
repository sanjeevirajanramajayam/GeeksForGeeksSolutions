from collections import deque
class Solution:
	def firstNonRepeating(self, s):
		# code here
		queue = deque([])
		hashFreq = {}
		ans = ""
		for i in range(len(s)):
		    hashFreq[s[i]] = hashFreq.get(s[i], 0) + 1
		    if hashFreq[s[i]] == 1:
		        queue.append(s[i])
		    
		    while queue and hashFreq[queue[0]] > 1:
		        queue.popleft()
		    
		    if queue:
		        ans += queue[0]
		    else:
		        ans += "#"
	    return ans