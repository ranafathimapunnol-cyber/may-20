class Solution:
    def twoSum(self, nums, target):  # Changed from twoSum_brute to twoSum
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []