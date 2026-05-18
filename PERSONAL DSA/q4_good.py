# FUNCTION DEFINITION
# TIME COMPLEXITY: O(n)

def findMaxProfit(price):
    # initialization
    minPrice = float("inf")
    maxProfit = 0

    for i in range(len(price)):
        if price[i] < minPrice:
            minPrice = price[i]
        elif price[i] - minPrice > maxProfit:
            maxProfit = price[i] - minPrice
    return maxProfit

price = [7,4,5,8,9,16]
maxProfitValue = findMaxProfit(price) 
print("The maximum profit of buying and selling the stock is: ", maxProfitValue)