# Two Sum II - Input Array Is Sorted
# Given a sorted array of integers and a target, find two numbers whose sum is equal to the target.
# Time Complexity: O(n)

def twoSum(numbers, target):
        
        start = 0
        end = len(numbers) - 1
            
        while start < end:

            result = numbers[start] + numbers[end]

            if result == target:
               return [start + 1, end + 1]
            elif result < target:
                start += 1
            else:
                end -= 1

        return [-1, -1]

# driver code
numbers = [2, 7, 11, 15]
target = 9
result = twoSum(numbers, target)
print(result)