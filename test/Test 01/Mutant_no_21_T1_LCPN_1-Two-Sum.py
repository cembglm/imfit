class Solution:
    def twoSum(nums, target):
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff is not prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


print(Solution.twoSum(nums = [2,7,11,15], target= 9))