class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Two Pointers
        left = 0  #buy
        right = 1 #sell
        max_profit = 0 # max profit

        while right < len(prices):
            
            #check if price of buying is smaller than selling
            if prices[left] < prices[right]:
                
                #check if price is profitable
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)

            #if not then the buying price shifts to selling price
            else:
                left  =  right
            
            # This must happen EVERY iteration to keep exploring
            right += 1
        
        return max_profit

