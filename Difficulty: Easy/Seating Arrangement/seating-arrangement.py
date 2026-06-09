class Solution:
    def canSeatAllPeople(self, k, seats):
        # code here
        for i in range(len(seats)):
            if seats[max(0, i - 1)] != 1 and seats[i] != 1 and seats[min(i + 1, len(seats) - 1)] != 1:
                seats[i] = 1
                k -= 1
        # print(k, k <= 0)
        return k <= 0