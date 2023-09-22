class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        prefix_sum = {0: -1}  # Store prefix sum and its corresponding index
        current_sum = 0  # Variable to track the current sum
        n = len(nums)
        
        for i in range(n):
            current_sum += nums[i]
            prefix_sum[current_sum] = i

        target_sum = current_sum - x
        current_sum = 0
        if target_sum < 0:
            return -1

        min_steps = float('inf')

        for i in range(n):
            current_sum += nums[i]
            if current_sum - target_sum in prefix_sum:
                min_steps = min(min_steps, n - (i - prefix_sum[current_sum - target_sum]))

        if min_steps == float('inf'):
            return -1

        return min_steps
