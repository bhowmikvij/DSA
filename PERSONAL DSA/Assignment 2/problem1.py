# arr = [9, 8, 7, 6, 5, 4, 3]
# Create a buildHeap method that returns a minheap

def heapify(arr, n, i):

    smallest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[left] < arr[smallest] :
        smallest = left

    if right < n and arr[right] < arr[smallest] :
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)
    return


def buildHeap(arr, n):

    startIndex = n//2 -1

    for i in range(startIndex, -1, -1) :
        heapify(arr, n, i)
    return arr


arr = [9, 8, 7, 6, 5, 4, 3]
n = len(arr)
result = buildHeap(arr, n)
print(result)