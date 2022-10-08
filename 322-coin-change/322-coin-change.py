class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        mem = [amount+1]*(amount+1)
        mem[0] = 0
        
        for i in range(amount+1):
            for coin in coins:
                if (i-coin) >= 0:
                    mem[i] = min(mem[i-coin]+1, mem[i])
            
        if mem[amount] == (amount+1):
            return -1
        else:
            return mem[amount]            
