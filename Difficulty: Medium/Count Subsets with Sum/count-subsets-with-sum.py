from functools import cache
class Solution:
	def perfectSum(self, arr, target):
		# code here
		@cache
		def fn(ind, target):


		    
		    if ind == 0:
		        if target == 0 and arr[ind] == 0:
		            return 2
		        if target == 0:
		            return 1
		        if arr[ind] == target:
		            return 1
		        else:
		            return 0
		    
		    take = 0
		    if arr[ind] <= target:
		        take = fn(ind - 1, target - arr[ind])
		    
		    not_take = fn(ind - 1, target)
		    
		    return take + not_take
	    
	    return fn(len(arr) - 1, target)