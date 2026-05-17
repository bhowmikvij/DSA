# take a number digits sum

num = int(input("Enter the number:"))
sum=0

while num!=0:
    lastdigit = num%10
    sum = sum+lastdigit
    num = num//10
print(sum)

# ------------------------------------------------------------------------------

# # take a number and reverse it

num = int(input("Enter the number:"))
rev=0

while num!=0:
    lastdigit = num%10
    rev = rev*10 + lastdigit
    num = num//10
print(rev)


# --------------------------------------------------------------------------------



# check whether a num is palindrome or not

num = int(input("Enter a number: "))
temp = num
rev = 0

while num!=0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev==temp)  #  (==) is an boolean automatically gives true or false


# -------------------------------------------------------------------------



# check whether a num is prime or not



num = int(input("Enter the number to check:"))
for i in range (2,num):
    if num%i==0:
        print("Not Prime")
        break
else:
    print("Prime")


# ----------------------------------------------------


# # for 3 digit number.

num=int(input("input number:"))
print(f"number is {num}")
lastdigit=num%10
print(lastdigit)
secondlastdigit=num//10
thirdlastdigit=secondlastdigit//10
print(thirdlastdigit)
truesecondlastdigit=secondlastdigit-thirdlastdigit*10
print(truesecondlastdigit)
print(f"sum of every digit {lastdigit+truesecondlastdigit+thirdlastdigit}")



# ------------------------------------------------------------


# # Asks for a number and prints the REVERSE of its digits.

num=int(input("input number:"))
print(f"number is {num}")
rev=0
while num!=0:
    lastdigit=num%10
    rev=rev*10+lastdigit
    num=num//10
print(rev)



# ---------------------------------------------------------------



# # Asks for a number and prints the sum of its digits.

num=int(input("input number:"))
print(f"number is {num}")
sum=0
while num!=0:
    lastdigit=num%10
    sum=sum+lastdigit
    num=num//10
print(sum)


# --------------------------------------------------------------



# # Asks for a number and check its PALINDROME or not.

num=int(input("input number:"))
n=num
print(f"number is {num}")
rev=0
while num!=0:
    lastdigit=num%10
    rev=rev*10+lastdigit
    num=num//10
if n==rev:
    print(f"{n} is palindrome")
else:
    print(f"{n} is not palindrome")


# ----------------------------------------------------------------




# # Asks for a number and check its PRIME or not.

num=int(input("input number:"))
print(f"number is {num}")
for i in range(2,num):
    if num%i==0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")



# ---------------------------------------------------------




# Count number of digits in a number

a=int(input("Input Number: "))
count=0
while a!=0:
    count=count+1
    a=a//10
print(count)




# ----------------------------------------------------



# Check Armstrong number.

num=int(input("Input number: "))
n=num
digits=len(str(num))
sum=0
while num!=0:
    lastdigit=num%10
    sum=sum+lastdigit**digits
    num=num//10
if sum==n:
    print(f"{n} is Armstrong number")
else:
    print(f"{n} is not Armstrong number")


# -------------------------------------------------------



# Find factorial of a number

num=int(input("Input number: "))
n=1
for i in range (1,num+1):
    n*=i
print(f"factorial of {num} is {n}")



# ----------------------------------------------------------





n = int(input("Enter size: "))
lst = []

for i in range(n):
    lst.append(int(input()))

print(lst)

# ---------------------------------------------------------------


