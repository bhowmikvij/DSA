def getSecondLargest(arr):
        
        largest_element = second_largest_element = -1
        
        for num in arr:
            if num > largest_element:
                second_largest_element = largest_element
                largest_element = num
                
            elif num > second_largest_element and num != largest_element:
                second_largest_element = num
        
        return second_largest_element

# Driver Code
arr = [12, 35, 1, 10, 34, 1]
result = getSecondLargest(arr)
print(result)