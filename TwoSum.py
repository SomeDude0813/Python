class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i,v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [remaining, v]
            seen[i] = v
                            
        
solution = Solution()
print(solution.twoSum( [3, 4, 9, 6, 4], 8 )) # Array, target
