class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[right] >  prices[left]:
                profit = max(profit, prices[right]-prices[left])
            else:
                left = right
            
            right += 1
        return profit
    
        

prices = [7,1,5,3,6,4]
sol = Solution()

result = sol.maxProfit(prices)
print(result)