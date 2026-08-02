# Count of Number of Ways
# Example of Fibonacci Series

def possibilities(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # elif n == 2:
    #     return 1
    else:
        return possibilities(n-1) + possibilities(n-2)


n = 10
result = possibilities(n)
print(result)