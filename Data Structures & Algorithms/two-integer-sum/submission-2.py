class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = {} 
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dt:
                return [dt[complement], i]
            dt[num] = i