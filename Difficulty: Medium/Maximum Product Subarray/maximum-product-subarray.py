class Solution:
	def maxProduct(self,arr):
		# code here
		prefixProd = 1
		suffixProd = 1
		maxProd = float('-inf')
		for i in range(len(arr)):
		    prefixProd *= arr[i]
		    suffixProd *= arr[len(arr) - i - 1]
		  #  print(prefixProd, suffixProd)
		    maxProd = max(maxProd, prefixProd, suffixProd)
		    if not prefixProd:
		        prefixProd = 1
		    if not suffixProd:
		        suffixProd = 1
		
		return maxProd