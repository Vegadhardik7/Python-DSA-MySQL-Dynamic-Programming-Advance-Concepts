def insertion_sort(A):
    for i in range(1, len(A)):
        val = A[i]
        pos = i

        while pos > 0 and A[pos-1] > val:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = val


A = [84,21,5,96,15]
print("Original Array: ", A)
insertion_sort(A)
print("Sorted Array: ",A)