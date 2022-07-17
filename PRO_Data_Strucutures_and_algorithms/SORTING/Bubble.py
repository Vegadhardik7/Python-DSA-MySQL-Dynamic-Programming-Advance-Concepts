def bubblesort(A):
    for i in range(len(A)-1, 0, -1):
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

A = [85,6,15,24,36]
print("Before Sorting:",A)
bubblesort(A)
print("After Sorting:",A)