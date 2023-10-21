class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Calculate products to the left of each element
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]

        # Calculate products to the right of each element and multiply with the left product
        right_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
