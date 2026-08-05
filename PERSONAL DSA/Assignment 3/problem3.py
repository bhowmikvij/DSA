# An e-commerce site tracks the purchases made each day. The product that is
# purchased the most one day is the featured product for the following day.
# If there is a tie for the product purchased most frequently, 
# those product names are ordered alphabetically ascending and the last name in the list is chosen. [Amazon]

# ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat', 'pinkHat', 'blackShirt', 'yellowShirt', 'greenPants', 'greenPants', 'greenPants']
# 'yellowShirt' - 2
# 'redHat' - 2
# 'blackShirt' - 2
# 'bluePants' - 1
# 'greenPants' - 3
# 'pinkHat' - 1

# Output - greenPants

def featuredProduct(products):
    # Write your logic here
    freq = {}

    # Count frequency
    for product in products:
        if product in freq:
            freq[product] += 1
        else:
            freq[product] = 1

    # Find maximum frequency
    max_freq = max(freq.values())

    # Store products having maximum frequency
    ans = []

    for product in freq:
        if freq[product] == max_freq:
            ans.append(product)

    # Sort alphabetically
    ans.sort()

    # Return the last product
    return ans[-1]
    


# Driver Code
products = ["yellowShirt", "redHat", "blackShirt", "bluePants", "redHat", "pinkHat", "blackShirt", "yellowShirt", "greenPants", "greenPants", "greenPants"]
result = featuredProduct(products)
print(result)