arr = [2,10,3,4,10,4,17,0,1,5]

target = 14

class Solution(object):
    def twoSum(self, nums, target):
        result = list()
        n = len(nums)
        if n < 2:
            return
        
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i]+nums[j] == target:
                    if i and j in result:
                        continue
                    elif i in result:
                        result.append(j)
                    elif j in result:
                        result.append(i)
                    else:
                        result.append(i)
                        result.append(j)
            
        
        return result
    
Sol = Solution()
print(Sol.twoSum(arr, target))


