#                           SORTING
#                              /\
#                             /  \
#                            /    \
#                           /      \
#                          /        \
#                         /          \
#           Comparision-based      Non-comparison based

# Comparision-based=> Compare the elements inside the array
# Non-comparison based=> No comparision within the element

# CB=> Bubble Sort, Selection Sort, Insertion Sort, Quick Sort, Merge Sort, Heap Sort, Shell Sort
# NCB=> Count Sort, Radix Sort, Bucket Sort

# Bubble Sort=> TIME COMPLEXITY=> O(n^2)
# Selection Sort=> TIME COMPLEXITY=> O(n^2)

# INTERVIEW IMPORTANT QUESTION
# Given a scenario, array is sorted or almost sorted so which sorting algorithm is preferrable and why??
# Insertion Sort=> O(n)

# Which sorting algo is preffered when the array is highly unsorted?
# Quick Sort

# --------------------------------------------------------------------------------------------------------------------------

#                     Heap Data Structure
#                             /\
#                            /  \
#                           /    \
#                          /      \
#                      Maxheap   Minheap

# Tree Data Structure--> Non-Linear Data Structure

# Binary Tree

# Top Element--> Root Node
# Middle Element--> Internal Node
# Last Element--> Leaf Node

# IMPORTANT INFORM/ INTERVIEW IMPORTANT QUESTION
# Full Binary Tree(Perfect Binary Tree) VS Almost Complete Binary Tree VS Complete Binary tree?

# Common for above three different binary tree
# 1. Insertion of Node--> (left to right)
# 2. Upper level nodes will be filled up before coming to the lower level


# Heap--> Complete Binary Tree 
# time complexity: O(1)
# 1.Minheap--> Parent node
#              Data < Child node

# 2.Maxheap--> Parent node
#              Data > Child node

# VERY INMPORTANT INFORMATION ABOUT STORING DATA OF BINARY TREE INTO ARRAY
#                        (10) 0
#                         /\
#                        /  \
#           2*i + 1 = 1 /    \ 2*i + 2 = 2
#                    (20)    (30)
#                     /\
#                    /  \
#       2*i + 1 = 3 /    \ 2*i + 1 = 4
#                 (40)   (50)

#              [10, 20, 30, 40, 50]

# ------------------------------------------------

#                        (10) 0
#                         /
#           2*i + 1 = 1  /    
#                    (20)    
#                     / 
#       2*i + 1 = 3  /    
#                 (40)   
#                  /  
#     2*i + 1 = 7 /    
#              (50)

# [10, 20,  , 40,  ,  ,  , 50]
# There is very wastage of space in array so that's why we use LINKED LIST

# --------------------------------------------------------------------------------------------------------------------------

# INSERTION

# Height of CBT-> Minheap/ Maxheap
# Time Complexity-> O(logn)

# 1. number of nodes = 2^h -1
# At default Level = 0
#            Height = 1
# Time Complexity
#    h = log2(n+1) ................... 2 is in the Base
#    l = log2(n+1) ................... 2 is in the Base

# But it can also be start at Level = 1
# Dont argue the interviewer
# Time Complexity-> O(logn) 

# DELETION
# Time Complexity-> O(logn) 

# ---------------------------------------

# HEAPSORT
# 1. Delete the element from minheap and store it.
# n.(Delete)
# Sorted Array(Ascending Order)
# Time Complexity-> O(nlogn)

# ------------------------------------------------------------------------------------------------------------------------

# BUILD OF MINHEAP
# 123, 234, 45, 3, 34, 567, 36, 12

# V.V.V.IMPORTANT INTERVIEW QUESTION
# For bulid of minheap
# Time Complexity-> O(n)

# -----------------------------------------------------------------------------------------------------------------------

# Assignment
#  arr = [1, 3, 7, 9, 12, 10, 8, 16, 18, 22, 27]
# create a bulidHeap method that returns a minheap

# new file will be added 

# ---------------------------------------------------------------------------------------------------------------------------

# New concept DIVIDE, CONQUER, COMBINE

# Psuedocode

# divide And conquer(arr, p, 2):
# if (small (arr, p, q)):
#       return solution
# else:

#           two parts
# Divide    m = Divide(arr,p,q) 
#               Recursion
# Conquer   { b = divideAndconquer(arr, p, m) 
#           { c = divide And conquer (arr, m+1, q)

# Combine   return combine(b,c) 


# 

# Psuedocode
# Actual implementation of code 


# find MaxAndMin(arr, i, j):
#   if i== j: ==> single element
#       min = arr(i)
#       max = arr(i)
#   elif i == j-1: ==> double element
#       if arr(i) < arr (j):
#           max = arr(j)
#           min = arr(i)
#       else:
#           max = arr(i)
#           min = arr(j)
#   else:
#       mid = i +(j-1)//2
#       min1, max1 = find max And min (arr, i, mid)
#       min2, max2 = find max And min (arr, mid+1, 3)
# Combine
#       if min1 < min2:
#           min = min1
#       else:
#           min = min2
#       if max1 < max2:
#           max = max2
#       else:
#           max = max1
#   return(max,min)

# -------------------------------------------------------------------------------------------

# VERY IMPORTANT INTERVIEW ASKED QUESTION IN AMAZON

# Finding of power of an element 


# --------------------------------------------------------------------------------------------------


# MERGE SORT

# It is stable sorting
# Best Case => # comparisons = min(m, n)

# Time Complexity --> # comparisons + # move
#                 --> O(nlogn)
# Space Complexity --> O(N)

# -----------------------

# Pseudocode

# merge Sort (arr, p, q):
# if p == q:
#   return arr(p)
# else:
#   mid = p + (q-p)//2
#   right = mergeSort(arr, p, mid)
#   left = mergeSort(arr, mid+1, q)
#   mergeProcedure(arr, p, mid, q)
# return arr
