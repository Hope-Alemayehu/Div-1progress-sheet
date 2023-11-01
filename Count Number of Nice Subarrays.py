class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
       #Time complexity=O(N)
       #space complexity=O(N)
       #count the number of nice subarray
        count = 0
        #to keep track of cumulative count of odd numbers at each index
        prefix=[0]
        #the number of odd numbers found
        oddC=0

        for num in nums:
           oddC+=num%2
           prefix.append(oddC)
        #to check if the diffenece betwee current cumulative sum and k  has 
        freq = defaultdict(int)

        for val in prefix:
            if val-k in freq:
                count+=freq[val-k]
            freq[val]+=1
        return count
