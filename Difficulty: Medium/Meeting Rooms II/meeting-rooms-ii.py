class Solution:
    def minMeetingRooms(self, start, end):
        # code here
        s1 = 0
        s2 = 0
        n = len(start)
        cnt = 0
        maxCnt = 0
        start.sort()
        end.sort()
        while s1 < n and s2 < n:
            if start[s1] < end[s2]:
                cnt += 1
                maxCnt = max(maxCnt, cnt)
                s1 += 1
            elif start[s1] >= end[s2]:
                cnt -= 1
                s2 += 1
        return maxCnt