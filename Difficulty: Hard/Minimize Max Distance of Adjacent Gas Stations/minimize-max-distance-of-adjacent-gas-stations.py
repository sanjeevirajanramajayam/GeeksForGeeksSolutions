import heapq
class Solution:
    def minMaxDist(self, stations, k):
        # Code here
        heap = []
        if len(stations) < 2:
            return 0.0
        for i in range(len(stations) - 1):
            heapq.heappush(heap, (-(stations[i + 1] - stations[i]), i))
        newStations = [0] * (len(stations) - 1)
        for i in range(k):
            dist, index = heapq.heappop(heap)
            newStations[index] += 1
            newDist = (stations[index + 1] - stations[index]) / (newStations[index] + 1)
            heapq.heappush(heap, (-newDist, index))
        maxi = float('-inf')
        # print(newStations)
        for i in range(len(stations) - 1):
            # print((stations[i + 1] - stations[i]) / (newStations[index] + 1))
            maxi = max(maxi, (stations[i + 1] - stations[i]) / (newStations[i] + 1))
        return maxi