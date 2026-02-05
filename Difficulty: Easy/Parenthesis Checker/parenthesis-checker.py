class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        
        openClose = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        for i in range(len(s)):
            if s[i] in openClose:
                stack.append(s[i])
            else:
                if stack and openClose[stack[-1]] != s[i]:
                    return False
                elif not stack:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0