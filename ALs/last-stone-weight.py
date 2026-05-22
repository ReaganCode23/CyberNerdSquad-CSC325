import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            y = -stones[0]
            heapq.heappop(stones)
            x = -stones[0]
            heapq.heappop(stones)

            if y != x:
                r = -(y - x)
                heapq.heappush(stones, r)

        if len(stones) == 1:
            stones[0] = -stones[0]
            return stones[0]
        else:
            return 0