class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  
        
        current_sum = 0
        total_subarrays = 0
        
        for num in nums:
            current_sum += num

            total_subarrays += prefix_counts[current_sum - goal]

            prefix_counts[current_sum] += 1
            
        return total_subarrays