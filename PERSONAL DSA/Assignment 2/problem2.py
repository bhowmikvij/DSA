# Given an array of string words and n integer k, return the k most frequent words.
# Your Output should be in lexicographical order.
# Words = ["priya", "bhatia", "akshay", "arpit", "priya", "arpit"]
# k=3
# Output = ["arpit", "akshay", "priya"]

import heapq

def top_k_frequent(words, k):

    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    heap = []

    for word, count in frequency.items():
        heapq.heappush(heap, (count, word))

        if len(heap) > k:
            heapq.heappop(heap)

    result = []

    while heap:
        result.append(heapq.heappop(heap)[1])

    result.sort()

    return result


words = ['priya', 'bhatia', 'akshay', 'arpit', 'priya', 'arpit']
k = 3
result = top_k_frequent(words, k)
print(result)