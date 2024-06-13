nums = [2,7,11,15]
target = 9

class Solution(object):
    def twoSum(self, nums, target):
        prev_map = dict()

        for i, num in enumerate(nums):
            if target - num in prev_map:
                return [i, prev_map[target-num]]
            else:
                prev_map.update({num: i})
        return -1 
        

Sol = Solution()
print(Sol.twoSum(nums, target))