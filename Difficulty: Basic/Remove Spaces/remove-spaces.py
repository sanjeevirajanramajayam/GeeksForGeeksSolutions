class Solution:
    def removeSpaces(self, s):
        # code here
        news = []
        for i in s:
            if i != ' ':
                news.append(i)
        return "".join(news)