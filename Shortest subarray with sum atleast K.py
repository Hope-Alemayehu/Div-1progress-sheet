from typing import List
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        #time complexity=O(N)
        #space complexity=O(N)

        n = len(nums)
        dq = deque()
        total_sum = 0
        shortest = float("inf")

        for i in range(n):
            total_sum += nums[i]
            if total_sum >= k:
                shortest = min(shortest, i + 1)

            while dq and total_sum - dq[0][1] >= k:
                curr = dq.popleft()
                if curr[0] != float("-inf"):
                    shortest = min(shortest, i - curr[0])

            while dq and total_sum <= dq[-1][1]:
                dq.pop()

            dq.append((i, total_sum))
        
        return shortest if shortest != float("inf") else -1
