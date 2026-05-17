# MY DSA PROBLEMS FOR YT

# ---------------------------------------------------------------------------------------------------------------------------

# TIME COMPLEXITY
# logn > n > nlogn > n^2 > n^2logn .........

# ----------------------------------------------------------------------------------------------------------------------------

# EXTRACTION OF DIGITS

# First we will extract the last digits from the number input which will be used in all extraction

n=2357
num = n 

while num != 0:
    lastDigit = lastDigit%10
    print(lastDigit)
    num = num//10
    
# 1. COUNT DIGITS

n = 23567
num = n
count = 0
while num != 0:
    count +=1
    num = num//10
print(count)

# 2. CHECK PALINDROME  CHECK ARMSTRONG NUMBER


def a(n):
    num = n
    count = 0
    nod = len(str(n))
    while num!= 0:
        lastDigit = num%10
        count = count+(lastDigit**nod)
        num = num//10
    return count==n

print(a(153))

# CHECK FACTORS
# 217
# 242
# 169
# 1
# 349
# 1207  
# 49
# 560
# 3
# 128


# [0,1,2,3,4,5]
# [1,2,3,4,5,6]
# [0,1,2,3,4,5,6,7,8]
# [1,2,2,3,3,4,5,5,6]

for i in range (0, n):
    print ("Enter the number")
    if n>n/2:
        print("  ")
