def Quick_Sort(A, low, high):
    if low < high:
        p = partition(A, low, high)
        Quick_Sort(A, low, p-1)
        Quick_Sort(A, p+1, high)

def partition(A, low, high):
    i = low-1
    pivot = A[high]
    for j in range(low, high):
        if A[j] <= pivot:
            i +=1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]

    return i+1

A = [84,12,5,66,95]
print("Original List:",A)
Quick_Sort(A, 0, len(A)-1)
print("Sorted List:",A)