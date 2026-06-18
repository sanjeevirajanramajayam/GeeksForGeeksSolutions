class Solution:
    def findCoverage(self, mat):
        # code here
        rows = [0] * len(mat)
        cols = [0] * len(mat[0])
        ROWS = len(mat)
        COLS = len(mat[0])
        ans = 0
        for i in range(len(mat)):
            rowSum = sum(mat[i])
            currSum = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    if rowSum > 0:
                        ans += 1
                    if currSum > 0:
                        ans += 1
                else:
                    currSum += 1
                    rowSum -= 1
                    
        for i in range(len(mat[0])):
            colSum = 0
            currSum = 0
            for j in range(len(mat)):
                colSum +=  mat[j][i] 
            for j in range(len(mat)):
                # print(i, j, mat[i][j], colSum, currSum)
                if mat[j][i] == 0:
                    if colSum > 0:
                        ans += 1
                    if currSum > 0:
                        ans += 1
                else:
                    currSum += 1
                    colSum -= 1
        return ans
                