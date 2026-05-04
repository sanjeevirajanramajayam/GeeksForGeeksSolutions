class Solution:
    def isBinaryPalindrome(self, n):
        # code here
        return (bin(n)[2:] == bin(n)[2:][::-1])