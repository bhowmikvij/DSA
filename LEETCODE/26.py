# Remove Duplicates from Sorted Array
# 1.Remove duplicate elements in-place.
# 2. Keep only one occurrence of each number.
# 3. Keep the original sorted order.
# 4. Return k, where k is the number of unique elements.
# Time Complexity: O(n)

def removeDuplicates(nums):
        
        index = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1

        return index


# Driver Code
nums = [1, 1, 2, 2, 3, 3, 4]

index = removeDuplicates(nums)

print("Number of unique elements:", index)
print("Array after removing duplicates:", nums[:index])