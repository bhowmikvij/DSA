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