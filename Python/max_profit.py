# Written by Jake Foiles, Mar. 2023
# A solution to the most basic maxium stock profit DSA question

prices = [7,1,5,3,6,4]

# Naive solution (O(n*logn)?)
# def max_profit(prices):
#     temp, max = 0, 0
#     for i in range(len(prices) - 1):
#         for j in range(i + 1, len(prices)):
#             temp = prices[j] - prices[i]
#             if temp > max:
#                 max = temp
#     return max

def max_profit(prices):
    l, r = 0, 1 # Pointers for buying and selling, respectively
    temp, max = 0, 0 # Current profit, all-time max profit

    while r < len(prices):
        temp = prices[r] - prices[l]

        if temp > 0 and temp > max:
            max = temp
        elif temp < 0:
            l = r
        r += 1
    
    return max

print(max_profit(prices))