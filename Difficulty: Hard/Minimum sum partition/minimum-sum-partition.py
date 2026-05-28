class Solution:
	def minDifference(self, arr):
		# code here
		prev = [False for j in range(sum(arr) + 2)] 
		curr = [False for j in range(sum(arr) + 2)] 

        prev[0] = True
	    curr[0] = True
	    
	    prev[arr[0]] = True
        curr[arr[0]] = True

	    
	    for i in range(1, len(arr)):
	        for j in range(sum(arr) + 2):
	            take = False
	            if arr[i] <= j:
	                take = prev[j - arr[i]]
	            not_take = prev[j]
	            curr[j] = take or not_take
	        prev = curr[:]
	    mini = float('inf');

        for i in range(len(prev)):
            if prev[i] == True:
                s2 = sum(arr) - i
                mini = min(mini, abs(i - s2))
        return mini
		    