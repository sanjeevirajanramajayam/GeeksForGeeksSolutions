from functools import cmp_to_key
class Solution:
	def findLargest(self, arr):
	    # code here
        arr = [str(i) for i in arr]
        arr = sorted(arr, reverse=True, key=lambda x: x * 10)
        if sum([int(x) for x in arr]) == 0:
            return "0"
        return "".join(arr)