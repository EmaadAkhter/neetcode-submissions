class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        max_price=-1

        for price in prices:
            min_price=min(min_price,price)
            max_price=max(price-min_price,max_price)
        
        return max_price
        